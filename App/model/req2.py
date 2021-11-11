import sys
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
import model.comp as cp
from DISClib.Algorithms.Sorting import mergesort as ms

def getDurationRange(catalog,inf,sup):
    """
    La funcion retorna el total de avistamientos dentro del rango y una lista con los 3 primeros y ultimos avistamientos
    sorteados por pais-ciudad.
    Se divide en 3 partes:
        Sacar total de avistamientos.
        Sacar y sortear primeros 3 primero por ciudad y luego por pais.
        Sacar y sortear los ultimos 3 primero por ciudad y luego por pais.
    Returns:
    totsights: numero con la cantidad de avistamientos
    final: lista con los 3 primeros y ultimos avistamientos
    sorteados por duracion->ciudad->pais.

    """
    duration=catalog['duration']
    duration_range=om.values(duration,inf,sup)
    totsights=0
    
    for sight in lt.iterator(duration_range):
        totsights+=lt.size(sight)

    #Este codigo si bien es mas largo, es mas eficiente. La eficiencia se nota mas si el rango de busqueda es muy grande.
    keyset=om.keys(duration,inf,sup)

    firstIndex=om.get(duration,lt.firstElement(keyset))['value'] 
    ms.sort(firstIndex,compareCity)
    final=lt.subList(firstIndex,1,3)
    ms.sort(final,compareCountry)
   
    lastIndex=om.get(duration,lt.lastElement(keyset))['value']
    
    if lt.size(lastIndex)<3: #Esto es en casos MUYYYY especificos.
        last=lt.newList(datastructure='SINGLE_LINKED')
        reverse_key=1
        while lt.size(last)<3: #SOLO en el caso donde la ultima llave no tenga 3 avistamientos, se recorre para atras las llaves
            for a in lt.iterator(lastIndex):
                if lt.size(last)==3:
                    break
                lt.addFirst(last,a) 
            lastIndex=om.get(duration,lt.getElement(keyset,lt.size(keyset)-reverse_key))['value']
            ms.sort(lastIndex,rcompareCity)
            reverse_key+=1
        
        #Al tener los ultimos tres elementos ahora se sortea por pais y luego ciudad, sin embargo el sorteo por duracion es lo que mas prioridad tiene.
        #Last esta ordenado de menor a mayor por duracion 
        max_duration=lt.lastElement(keyset)
        for a in lt.iterator(last): #Quitar duraciones distintas a max.
            if float(a['duration (seconds)'])<max_duration:
                lt.addLast(final,a)
                lt.removeFirst(last)
        ms.sort(last,compareCity)
        for b in lt.iterator(last):
            lt.addLast(final,b)
    else:
        ms.sort(lastIndex,compareCity)
        last=lt.subList(lastIndex,lt.size(lastIndex)-2,3)
        ms.sort(last,compareCountry)
        for k in lt.iterator(last):
            lt.addLast(final,k)
            


            

    #Forma simple pero ineficiente-Quitar el counter del for loop y añadir todo a una lista.
    # total=lt.subList(match,1,3)
    # last=lt.subList(match,lt.size(match)-3,3)
    # for a in lt.iterator(last):
    #     lt.addLast(total,a)
    
    return totsights, final

def compareCity(city1,city2):
    return city1['city'] < city2['city'] #Menor a mayor
def compareCountry(country1,country2):
    return country1['country'] < country2['country'] #Menor a mayor

def rcompareCity(city1,city2):
    return city1['city'] > city2['city']
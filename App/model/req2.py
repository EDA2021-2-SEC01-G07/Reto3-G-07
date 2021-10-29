import sys
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import model.comp as cp

def getDurationRange(catalog,inf,sup):
    """
    """
    duration=catalog['duration']
    
    duration_range=om.values(duration,inf,sup)
    totsights=0
    counter=1
    match=lt.newList(datastructure='ARRAY_LIST')
    for sight in lt.iterator(duration_range):
        totsights+=lt.size(sight)
        for a in lt.iterator(sight):
            if counter>3:
                continue
            lt.addLast(match,a)
            counter+=1

    #Este codigo si bien es mas largo, es mas eficiente. La eficiencia se nota mas si el rango de busqueda es muy grande.
    keyset=om.keys(duration,inf,sup)
    lastIndex=om.get(duration,lt.lastElement(keyset))['value']
    last=lt.newList(datastructure='SINGLE_LINKED')
    while lt.size(last)<3: #SOLO en el caso donde la ultima llave no tenga 3 avistamientos, se recorre para atras las llaves
        for a in lt.iterator(lastIndex):
            if lt.size(last)==3:
                continue
            lt.addFirst(last,a) 
        lastIndex=om.get(duration,lt.getElement(keyset,lt.size(keyset)-1))['value']
    for a in lt.iterator(last):
        lt.addLast(match,a)

    #Forma simple pero ineficiente-Quitar el counter del for loop y añadir todo a una lista.
    # total=lt.subList(match,1,3)
    # last=lt.subList(match,lt.size(match)-3,3)
    # for a in lt.iterator(last):
    #     lt.addLast(total,a)
    
    return totsights, match
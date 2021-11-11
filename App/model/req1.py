import sys
from DISClib.DataStructures.bst import keySet
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import orderedmap as om
import datetime as datetime
import model.comp as cp

def getCitySightings(catalog,city):
    """
    Dado una ciudad retrona la cantidad de avistamientos en la ciudad y los primeros/ultimos 3
    Return:
    total: Cantidad de avistamientos
    joined: Lista con los primeros y ultimos 3 avistamientos.
    max_sightings: La cantidad mas alta de avistamientos
    max_city: La ciudad con mayor cantidad de avistamientos.
    """
    cities=catalog['cities']
    keyset=om.keySet(cities)
    selected_city=om.get(cities,city)['value']
    match=lt.newList(datastructure='ARRAY_LIST')
    max_sightings=0
    max_city=""
    #Para obtener la ciudad con mas cantidad de avistamientos toca recorrer todo el arbol.
    #De esto se encarga el siguiente for-
    for c in lt.iterator(keyset):
        city_sightings=lt.size(om.get(cities, c)['value'])
        if city_sightings>max_sightings:
            max_sightings=city_sightings
            max_city=c
            
    #Añade todo los avistamientos de la ciudad ingresada a una lista.
    for sight in lt.iterator(selected_city):
        lt.addLast(match,sight)
    total=lt.size(match)
    ms.sort(match,compareDateTime)
    
    #Hacer la lista en caso de que halla mas que 6
    if total>6:
        joined=lt.subList(match,1,3)
        last=lt.subList(match,total-3,3)
        for a in lt.iterator(last):
            lt.addLast(joined, a)
    else:
        joined=lt.subList(match,1,total)
    return total, joined, max_sightings, max_city

def compareDateTime(date1,date2):
    date1=datetime.datetime.strptime(date1['datetime'], '%Y-%m-%d %H:%M:%S')
    date2=datetime.datetime.strptime(date2['datetime'], '%Y-%m-%d %H:%M:%S')
    
    return date1 < date2 #Menor a mayor
    
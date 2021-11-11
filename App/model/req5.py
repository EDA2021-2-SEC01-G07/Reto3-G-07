import sys
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import orderedmap as om
import model.comp as cp

def getLocationRange(catalog, ltmin, ltmax, lgmin, lgmax):

    latitude = catalog['latitude']
    longitude = catalog['longitude']

    total_sightings = lt.newList('ARRAY_LIST')

    values = lt.newList('ARRAY_LIST')

    latitude_values = om.values(latitude, ltmin, ltmax)

    for list in lt.iterator(latitude_values):
        filtered_list = lt.newList('ARRAY_LIST')
        for value in lt.iterator(list):
            if value > lgmin and value < lgmax:
                lt.addLast(filtered_list, value)
        ms.sort(filtered_list, lambda value1, value2: float(value1['longitude']) > float(value2['longitude']))
        for value in lt.iterator(filtered_list):
            lt.addLast(values, value)
    
    samples = lt.subList(values, 1, 5)

    last_samples = lt.subList(values, lt.size(values)-2, 5)

    for value in lt.iterator(last_samples):
        lt.addLast(samples, value)
    
    return samples ,lt.size(values)

        
    

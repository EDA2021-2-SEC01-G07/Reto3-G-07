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
        
        for value in lt.iterator(list):
            lt.addLast()
    

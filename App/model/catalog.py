import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import model.comp as cp
assert cf

def newCatalog():
    catalog = {
        "cities": om.newMap(comparefunction=cp.comparePrimitives),
        "duration": om.newMap(comparefunction=cp.comparePrimitives),
        "hours": om.newMap(comparefunction=cp.compareHours),
        "dates": om.newMap(comparefunction=cp.compareDates),
        "latitude": om.newMap(comparefunction=cp.comparePrimitives),
        "longitude": om.newMap(comparefunction=cp.comparePrimitives),
        "sightings": lt.newList(datastructure='ARRAY_LIST')
    }
    return catalog

def addCatalog(catalog, sighting):
    pass

def addSighting(catalog, sighting):
    lt.addLast(catalog['sightings'], sighting)

    cities = catalog['cities']
    entry = om.get(cities, sighting["city"])
    array = None

    if entry != None:
        array = me.getValue(entry)
    else:
        array = lt.newList()
        om.put(cities, sighting["city"], array)
        
    lt.addLast(array, sighting)
    return catalog

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
        "cities": om.newMap(comparefunction=cp.compareCities),
        "duration": om.newMap(comparefunction=cp.compareDurations),
        "hours": om.newMap(comparefunction=cp.compareHours),
        "sightings": lt.newList(datastructure='ARRAY_LIST')
    }
    return catalog

def addCatalog(catalog, sighting):
    pass

def addSighting():
    pass
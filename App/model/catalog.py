import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import model.comp as cp
import datetime
assert cf

def newCatalog():
    catalog = {
        "cities": om.newMap(omaptype='RDT',comparefunction=cp.comparePrimitives),
        "duration": om.newMap(omaptype='RDT',comparefunction=cp.comparePrimitives),
        "hours": om.newMap(omaptype='RDT',comparefunction=cp.compareHours),
        "dates": om.newMap(omaptype='RDT',comparefunction=cp.compareDates),
        "latitude": om.newMap(omaptype='RDT',comparefunction=cp.comparePrimitives),
        "sightings": lt.newList(datastructure='ARRAY_LIST')
    }
    return catalog



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
    
    updateDurationIndex(catalog['duration'],sighting )
    updateDateIndex(catalog['dates'],sighting)
    updateHourIndex(catalog['hours'],sighting)
    return catalog

def updateDurationIndex(map, sighting):
    """
    Se toma la duracion del avistamiento y se busca si ya existe dentro del arbol.
    En caso de que si se adiciona a su su lista de avistamientos y se actualiza el indice.

    En caso de que no, crea el nodo y actualiza el indice de tipo duracion.
    """
    duration=float(sighting['duration (seconds)'])
    entry = om.get(map, duration)
    if entry != None:
        duration_entry = me.getValue(entry)
    else:
        duration_entry = lt.newList(datastructure="ARRAY_LIST")
        om.put(map, duration, duration_entry)
    lt.addLast(duration_entry,sighting)
    return map

def updateDateIndex(map,sighting):
    """
    Se toma solo el dia del avistamiento y se busca si ya existe dentro del arbol.
    En caso de que si se adiciona a su su lista de avistamientos y se actualiza el indice.

    En caso de que no, crea el nodo y actualiza el indice de tipo date.
    """
    ufodatetime=sighting['datetime']
    ufodate= datetime.datetime.strptime(ufodatetime, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map,ufodate.date())
    if entry != None:
        date_entry=me.getValue(entry)
    else:
        date_entry = lt.newList(datastructure="ARRAY_LIST")
        om.put(map, ufodate.date(), date_entry)
    lt.addLast(date_entry,sighting)
    return map

def updateHourIndex(map,sighting):
    """
    Se toma solo el dia del avistamiento y se busca si ya existe dentro del arbol.
    En caso de que si se adiciona a su su lista de avistamientos y se actualiza el indice.

    En caso de que no, crea el nodo y actualiza el indice de tipo date.
    """
    ufodatetime=sighting['datetime']
    ufodate= datetime.datetime.strptime(ufodatetime.split(" ")[1], '%H:%M:%S').time()
    entry = om.get(map,ufodate)
    if entry != None:
        date_entry=me.getValue(entry)
    else:
        date_entry = lt.newList(datastructure="ARRAY_LIST")
        om.put(map, ufodate, date_entry)
    lt.addLast(date_entry,sighting)
    return map

def updateLocationIndex(map,sighting):
    """
    Se toma solo el dia del avistamiento y se busca si ya existe dentro del arbol.
    En caso de que si se adiciona a su su lista de avistamientos y se actualiza el indice.

    En caso de que no, crea el nodo y actualiza el indice de tipo date.
    """
    ufolatitude=sighting['latitude']

    entry = om.get(map, ufolatitude)
    if entry != None:
        date_entry=me.getValue(entry)
    else:
        date_entry = lt.newList(datastructure="ARRAY_LIST")
        om.put(map, ufolatitude, date_entry)
    lt.addLast(date_entry,sighting)

    return map
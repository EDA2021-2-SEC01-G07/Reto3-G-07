import sys
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import model.comp as cp

def getHourRange(catalog, initial, final):

    hours = catalog['hours']

    range_values = om.values(hours, initial, final)

    first_values = getElementsDeepList(range_values, 1, 3, False)
    last_values = getElementsDeepList(range_values, lt.size(range_values), 3, True)

    total_values = lt.newList("ARRAY_LIST")

    for value in lt.iterator(first_values):
        lt.addLast(total_values, value)
    
    for value in lt.iterator(last_values):
        lt.addLast(total_values, value)
    
    return total_values, lt.size(range_values)


def getElementsDeepList(lst,index,size,backwards):
    elements_obtained = lt.newList()

    while lt.size(elements_obtained) < size and index <= lt.size(lst):
        element_to_check = lt.getElement(lst, index)
        element_iterator = lt.iterator(element_to_check)

        next_value = next(element_iterator, None)

        while next_value is not None and lt.size(elements_obtained) < size:
            lt.addLast(elements_obtained, next_value)
            next_value = next(element_iterator, None)

        index = index-1 if backwards else index+1
    
    return elements_obtained
    
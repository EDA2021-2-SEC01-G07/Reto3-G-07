import datetime as dt

def compareHours(datetime1, datetime2)->int:
    pass

def compareCities(city1, city2)->int:
    if (city1 == city2):
        return 0
    elif (city1 > city2):
        return 1
    else:
        return -1

def compareDurations(duration1, duration2)->int:
    if (duration1 == duration2):
        return 0
    elif (duration1 > duration2):
        return 1
    else:
        return -1

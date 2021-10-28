
def compareDates(datetime1, datetime2)->int:
    date1 = datetime1.date()
    date2 = datetime2.date()
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareHours(datetime1, datetime2)->int:
    time1 = datetime1.hour*60 + datetime1.minute
    time2 = datetime2.hour*60 + datetime2.minute
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1

def comparePrimitives(primitive1, primitive2)->int:
    if (primitive1 == primitive2):
        return 0
    elif (primitive1 > primitive2):
        return 1
    else:
        return -1

"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
import prettytable as pt
from DISClib.ADT import orderedmap as om
from prettytable import PrettyTable
import datetime
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- (Req1) Avistamientos por ciudad")
    print("3- (Req2) Avistamientos por duracion")
    print("4- (Req3) Avistamientos por hora/minuto del dia")
    print("5- (Req4) Avistamientos por rango de fechas")
    print("6- (Req5) Avistamientos por zona geografia")
    print("7- (Req6) Visualizar avistamientos de una zona geografica")
    print("")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    entry = int(input('Seleccione una opción para continuar\n'))
    if entry == 1:
        print("Cargando información de los archivos ....")
        start_time = time.process_time()
        catalog = controller.newCatalog()
        controller.loadData(catalog)
        end_time=(time.process_time() - start_time)*1000
        print('El total de avistamientos cargados es de :',str(lt.size(catalog['sightings'])))
        table=pt.PrettyTable(hrules=pt.ALL)
        table.field_names=['DateTime','City','State','Country','Shape','Duration(sec)','Duration(h)','Comments','Date Posted', 'Latitude','Longitude']
        total=lt.subList(catalog['sightings'],1,5)
        last=lt.subList(catalog['sightings'],lt.size(catalog['sightings'])-4,5)

        for a in lt.iterator(last):
            lt.addLast(total,a)
        table._max_width={'DateTime':30,'City':10,'State':10,'Country':10,'Shape':10,'Duration(sec)':10,'Duration(h)':10,'Comments':20,'Date Posted':30, 'Latitude':10,'Longitude':10}
        
        for row in lt.iterator(total):
            table.add_row([row['datetime'],row['city'],row['state'],row['country'],row['shape'],row['duration (seconds)'],row['duration (hours/min)'],row['comments'],row['date posted'], round(float(row['latitude']),2),round(float(row['longitude']),2)])
        print('Primeros y ultimos 5 avistamientos son: \n')
        print(table)
        print("The processing time is: ",end_time, " ms.")
        
    elif entry == 2:
        print('La altura del arbol es: ',str(om.height(catalog['cities'])))
        print('El tamaño del arbol es de :',str(om.size(catalog['cities'])))
        city=input('Ciudad que desea consultar: ')
        start_time = time.process_time()
        result=controller.getCitySightings(catalog,city)
        cities=catalog['cities']
        end_time=(time.process_time() - start_time)*1000

        print('='*15,'Req No. 1 Inputs','='*15)
        print('UFO sightings in the city of:', city)
        print('='*15,'Req No. 1 Answers','='*15)
        print('There are',int(lt.size(om.keySet(cities))),'diferent cities with UFO sightings...')

        print('The city with most UFO sightings is:')
        table1=PrettyTable(hrules=pt.ALL)
        table1.field_names = ['City','Count']
        table1.add_row([result[3],result[2]])
        print(table1)

        print('The first 3 and last 3 UFO sightings in the duration time are:')
        table2=PrettyTable(hrules=pt.ALL)
        table2.field_names = ['DateTime','City','State','Country','Shape','Duration (seconds)']
        for row in lt.iterator(result[1]):
            table2.add_row([row['datetime'],row['city'],row['state'],row['country'],row['shape'],row['duration (seconds)']])
        table2._max_width={'DateTime':30,'City':30,'State':30,'Country':30,'Shape':30,'Duration (seconds)':30}
        print(table2)
        print("The processing time is: ",end_time, " ms.")
        pass
    elif entry == 3:
        inf=float(input('Limite inferior de la duracion del avistamiento: '))
        sup=float(input('Limite superior de la duracion del avistamiento: '))
        start_time = time.process_time()
        result=controller.getDurationRange(catalog,inf,sup)
        duration=catalog['duration']

        print('='*15,'Req No. 2 Inputs','='*15)
        print('UFO sightings between', inf,'and',sup,'\n')
        print('='*15,'Req No. 2 Answers','='*15)
        print('There are',int(lt.size(om.keySet(duration))),'diferent durations of UFO sightings...')

        print('The longest UFO sighting is:')
        longest=om.maxKey(duration)
        longest_count=lt.size(om.get(duration,longest)['value'])
        end_time=(time.process_time() - start_time)*1000
        table1=PrettyTable(hrules=pt.ALL)
        table1.field_names = ['Duration (seconds)','Count']
        table1.add_row([longest,longest_count])
        print(table1)

        print('\nThere are',str(result[0]),'sightings between', inf,'and',sup)
        print('The first 3 and last 3 UFO sightings in the duration time are:')
        table2=PrettyTable(hrules=pt.ALL)
        table2.field_names = ['DateTime','City','State','Country','Shape','Duration (seconds)']
        for row in lt.iterator(result[1]):
            table2.add_row([row['datetime'],row['city'],row['state'],row['country'],row['shape'],row['duration (seconds)']])
        table2._max_width={'DateTime':30,'City':30,'State':30,'Country':30,'Shape':30,'Duration (seconds)':30}
        print(table2)
        print("The processing time is: ",end_time, " ms.")
    elif entry == 4:
        pass


    elif entry == 5:
        inf = input('Ingrese la fecha incial del rango (YYYY-MM-DD): ')
        sup = input('Ingrese la fecha final del rango (YYYY-MM-DD): ')
        start_time = time.process_time()
        result=controller.getDateRange(catalog,inf,sup)
        dates=catalog['dates']
        longest=om.minKey(dates)
        longest_count=lt.size(om.get(dates,longest)['value'])
        end_time=(time.process_time() - start_time)*1000

        print('='*15,'Req No. 4 Inputs','='*15)
        print('UFO sightings between', inf,'and',sup,'\n')
        print('='*15,'Req No. 2 Answers','='*15)
        print('There are',int(lt.size(om.keySet(dates))),' with diferent dates [YYYY-MM-DD]...')

        print('The oldest UFO sightings date is:')
        table1=PrettyTable(hrules=pt.ALL)
        table1.field_names = ['Date','Count']
        table1.add_row([longest,longest_count])
        print(table1)

        print('\nThere are',str(result[0]),'sightings between', inf,'and',sup)
        print('The first 3 and last 3 UFO sightings in this time are:')
        table2=PrettyTable(hrules=pt.ALL)
        table2.field_names = ['DateTime','Date','City','State','Country','Shape','Duration (seconds)']
        for row in lt.iterator(result[1]):
            a=datetime.datetime.strptime(row['datetime'], '%Y-%m-%d %H:%M:%S')
            table2.add_row([row['datetime'],a.date(),row['city'],row['state'],row['country'],row['shape'],row['duration (seconds)']])
        table2._max_width={'DateTime':30,'Date':20,'City':30,'State':30,'Country':30,'Shape':30,'Duration (seconds)':30}
        print(table2)
        
        print("The processing time is: ",end_time, " ms.")
    else:
        sys.exit(0)
sys.exit(0)

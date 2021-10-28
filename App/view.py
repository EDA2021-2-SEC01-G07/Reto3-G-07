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
from DISClib.ADT import list as lt
import prettytable as pt
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
    print("2- Avistamientos por ciudad")
    print("3- Avistamientos por duracion")
    print("4- Avistamientos por hora/minuto del dia")
    print("5- Avistamientos por rango de fechas")
    print("6- Avistamientos por zona geografia")
    print("7- Visualizar avistamientos de una zona geografica")
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
        catalog = controller.newCatalog()
        controller.loadData(catalog)
        print('El total de avistamientos cargados es de :',str(lt.size(catalog['sightings'])))
        table=pt.PrettyTable(hrules=pt.ALL)
        table.field_names=['DateTime','City','State','Country','Shape','Duration(sec)','Duration(h)','Comments','Date Posted', 'Latitude','Longitude']
        total=lt.subList(catalog['sightings'],1,5)
        last=lt.subList(catalog['sightings'],lt.size(catalog['sightings'])-4,5)

        for a in lt.iterator(last):
            lt.addLast(total,a)
        table._max_width={'DateTime':30,'City':10,'State':10,'Country':10,'Shape':10,'Duration(sec)':10,'Duration(h)':10,'Comments':30,'Date Posted':30, 'Latitude':30,'Longitude':30}
        
        for row in lt.iterator(total):
            table.add_row([row['datetime'],row['city'],row['state'],row['country'],row['shape'],row['duration (seconds)'],row['duration (hours/min)'],row['comments'],row['date posted'], row['latitude'],row['longitude']])
        print('Primeros y ultimos 5 avistamientos son: \n')
        print(table)
    elif entry == 2:
        pass
    elif entry == 3:
        pass
    elif entry == 4:
        pass
    elif entry == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)

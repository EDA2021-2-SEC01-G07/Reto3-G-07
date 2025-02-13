﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import csv
import model.catalog as ct
import model.req1 as rq1
import model.req2 as rq2
import model.req3 as rq3
import model.req4 as rq4
import model.req5 as rq5
import datetime
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def newCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = ct.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    ufofile = cf.data_dir + 'UFOS-utf8-10pct.csv'
    input_file = csv.DictReader(open(ufofile, encoding='utf-8'))
    for sighting in input_file:
        ct.addSighting(catalog, sighting)
    return catalog

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def getCitySightings(catalog,city):
    return rq1.getCitySightings(catalog,city)
def getDurationRange(catalog,inf,sup):
    return rq2.getDurationRange(catalog,inf,sup)

def getHourRange(catalog,inf,sup):
    initial = datetime.datetime.strptime(inf, '%H:%M').time()
    final = datetime.datetime.strptime(sup, '%H:%M').time()
    return rq3.getHourRange(catalog,initial,final)

def getDateRange(catalog,sup,inf):
    initial = datetime.datetime.strptime(sup, '%Y-%m-%d').date()
    final = datetime.datetime.strptime(inf, '%Y-%m-%d').date()
    return rq4.getDateRange(catalog,initial,final)

def getLocationRange(catalog, ltmin, ltmax, lgmin, lgmax):
    return rq5.getLocationRange(catalog, ltmin, ltmax, lgmin, lgmax)

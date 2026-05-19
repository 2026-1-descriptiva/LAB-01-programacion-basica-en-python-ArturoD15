"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_01():
    leer = open("files/input/data.csv")
    suma = 0
    for columna in leer:
        partes = columna.split("\t")
        partes[1]
        suma += int(partes[1])
    return suma
 
"""
retorne la suma de la segunda columna

Rta/
214

"""

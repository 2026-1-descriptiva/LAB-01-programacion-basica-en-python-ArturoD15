"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    leer = open("files/input/data.csv")
    tuplas=[]
    for letras in leer:
        partes_letras= letras.split("\t")
        elementos1= len(partes_letras[3].split(","))
        elementos2= len(partes_letras[4].split(","))
        tuplas.append((partes_letras[0], elementos1, elementos2))
    return tuplas

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    leer = open("files/input/data.csv")
    conteo ={}
    for sep in leer:
        columnas= sep.split("\t")
        numeros= int(columnas[1])
        partes_letras=columnas[3].split(",")
        for letra in partes_letras:
            if letra in conteo:
                conteo[letra] += numeros
            else:
                conteo[letra] = numeros
    return conteo

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

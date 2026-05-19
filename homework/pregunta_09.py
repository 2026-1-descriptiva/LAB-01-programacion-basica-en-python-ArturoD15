"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    leer = open("files/input/data.csv")
    conteo ={}
    for clave in leer:
        claves= clave.split("\t")
        partes_claves= claves[4].split(",")
        for valor in partes_claves:
            valores= valor.split(":")
            if valores [0] in conteo:
                conteo[valores[0]]+= 1
            else:
                conteo[valores[0]]= 1
    return conteo

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    leer = open("files/input/data.csv")
    conteo ={}
    for max_min in leer:
        partes_letras= max_min.split("\t")
        numero= int(partes_letras[1])
        letra= partes_letras[0]
        if letra in conteo:
            if numero > conteo[letra][0]:
                conteo[letra][0] = numero
            if numero < conteo[letra][1]:
                conteo[letra][1] = numero
        else:
            conteo[letra]= [numero,numero]

    return sorted([(letra, v[0], v[1]) for letra, v in conteo.items()])

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

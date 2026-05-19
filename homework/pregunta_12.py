"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    leer = open("files/input/data.csv")
    conteo ={}
    for sep in leer:
        columnas= sep.split("\t")
        letras= columnas[0]
        partir_col5= columnas[4].split(",")
        for par in partir_col5:
            valor= par.split(":")
            num= int(valor[1])
            if letras in conteo:
                conteo[letras]+= num
            else:
                conteo[letras]= num
    return conteo
        
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

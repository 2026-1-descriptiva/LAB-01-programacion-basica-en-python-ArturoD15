"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    leer = open("files/input/data.csv")
    conteo_mes ={}
    for fecha in leer:
        partes= fecha.split("\t")
        fecha_mes= partes[2].split("-")
        if fecha_mes[1] in conteo_mes:
            conteo_mes[fecha_mes[1]]+= 1
        else:
            conteo_mes[fecha_mes[1]]= 1
    return sorted(conteo_mes.items())

    

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """

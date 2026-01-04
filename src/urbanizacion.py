from typing import NamedTuple
from datetime import datetime,date
import csv

Mejora = NamedTuple("Mejora",
        [("denominacion", str),
        ("coste", int),
        ("fecha ", date)])


Vivienda = NamedTuple("Vivienda",
        [("propietario", str),
        ("calle", str),
        ("fecha_adquisicion", date),
        ("numero", int),
        ("metros",float),
        ("precio",int),
        ("mejoras", list[Mejora])]) 


#EJERCICIO 1

#FUNCIONES AUXILIARES

def parsea_mejoras(mejoras_str:str) -> list[Mejora]:
    res = []
    if len(mejoras_str) > 1:
        mejoras_separadas = mejoras_str.split("*")
        res = [parsea_mejora(mejora) for mejora in mejoras_separadas]
    return res
    

def parsea_mejora(mejoras_str):
    denominacion, coste, fecha = mejoras_str.split("-")
    denominacion = str(denominacion)
    coste = int(coste)
    fecha = parsea_fecha(fecha)
    return Mejora(denominacion, coste, fecha)
    
    
def parsea_fecha(fecha_str: str) -> date:
    return datetime.strptime(fecha_str, "%d/%m/%Y").date()            
        
#LECTURA        
    
def lee_viviendas(ruta: str) -> list[Vivienda]:
    res = []
    with open(ruta, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        for propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras in lector:
            fecha_adquisicion = parsea_fecha(fecha_adquisicion)
            numero = int(numero)
            metros = float(metros)
            precio = int(precio)
            mejoras = parsea_mejoras(mejoras)
            tupla = Vivienda(propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras)
            res.append(tupl
























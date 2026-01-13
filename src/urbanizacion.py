from typing import NamedTuple
from datetime import datetime,date
import csv
from collections import defaultdict

Mejora = NamedTuple("Mejora",
        [("denominacion", str),
        ("coste", int),
        ("fecha", date)])


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
        for propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras in lector:
            numero = int(numero)
            fecha_adquisicion = parsea_fecha(fecha_adquisicion)
            metros = float(metros)
            precio = int(precio)
            mejoras = parsea_mejoras(mejoras)
            tupla = Vivienda(propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras)
            res.append(tupla)
    return res


#Ejercicio 2
def total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    res = dict()
    for e in viviendas:
        if (e.numero % 2 == 0 and par_impar.lower() == "par") or (e.numero % 2 != 0 and par_impar.lower() == "impar"):
            if e.calle not in res:    
                res[e.calle] = 0
            res[e.calle] += len(e.mejoras)
    return res

#Ejercicio 3

def tiempo_hasta_mejora(fecha_adquisicion, fecha_mejora):
    tiempo = (fecha_mejora - fecha_adquisicion).days
    return tiempo

def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> tuple[str,str,int,int,str]:
    candidatos = []
    for e in viviendas:
        for m in e.mejoras:
            dias = tiempo_hasta_mejora(e.fecha_adquisicion, m.fecha)
            candidatos.append((e, dias, m))
    minimo = min(candidatos, key= lambda x: x[1])
    v_ganadora, dias_ganador, m_ganadora = minimo
    
    return (v_ganadora.propietario, v_ganadora.calle, v_ganadora.numero, dias_ganador, m_ganadora.denominacion)
        
        
#Ejercicio 4

def calle_mayor_diferencia_precios(viviendas: list[Vivienda]) -> str:
    diferencias = defaultdict(int)
    
    for e in viviendas:
        if e.numero % 2 != 0:   #Es impar
            diferencias[e.calle] += e.precio
        else:
            diferencias[e.calle] -= e.precio
    
    return max(diferencias, key= lambda calle: abs(diferencias[calle]))    


#Ejercicio 5

def calculo_valor_vivienda(viviendas):
    valor_mejoras = sum(e.coste for e in viviendas.mejoras)
    return viviendas.precio + valor_mejoras

def n_viviendas_top_valoradas_por_calle(viviendas: list[Vivienda], fecha: date|None = None, n: int = 3) -> dict[str,list]:
    calles = defaultdict(list)
    for e in viviendas:
        if fecha == None or e.fecha_adquisicion >= fecha:
            valor_total = calculo_valor_vivienda(e)
            calles[e.calle].append((e.propietario, e.numero, valor_total))
    return {c: sorted(e, key= lambda x: x[2], reverse= True)[:n] for c, e in calles.items()}
    

#Ejercicio 6


def media_metro_cuadrado(vivienda: Vivienda) -> float:
        return vivienda.precio/vivienda.metros
    
def agrupa_calles_con_valor(lista_viviendas_anyo: list[Vivienda]) -> list[tuple[str, float]]:
    aux = defaultdict(list)
    for e in lista_viviendas_anyo:
        media = media_metro_cuadrado(e)
        aux[e.calle].append(media)
        
    res = []
    for calle, precio in aux.items():
        media = sum(precio) / len(precio)
        res.append((calle, media))    
    
    return sorted(res, key= lambda x: x[1], reverse=True)
             
    
def valor_metro_cuadrado_por_calle_y_año(viviendas: list[Vivienda]) -> list[tuple[int,list[tuple[str,float]]]]:
    anyos_calles = defaultdict(list)
    for e in viviendas:
        anyos_calles[e.fecha_adquisicion.year].append(e)
    
    res = []
    for anyo, lista_viviendas in anyos_calles.items():
        datos_calles = agrupa_calles_con_valor(lista_viviendas)
        res.append((anyo, datos_calles))
    
    return sorted(res)
        
    
    




    




















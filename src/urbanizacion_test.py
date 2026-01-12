from urbanizacion import *

def separador_linea(simbolo):
    print(simbolo*120)
    
def separar_resultados(iterable):
    for elem in iterable:
        print(f"\t{elem}")

def test_lee_viviendas(ruta: str)-> list[Vivienda]:
    print(f"Test de lee viviendas con {len(lee_viviendas(ruta))} registros leidos:")
    print("Mostrando los 5 primeros registros:")
    separar_resultados(viviendas[:5])
    separador_linea("=")
    print("Mostrando los 5 ultimos registros:")
    separar_resultados(viviendas[-5:])
    
    
def test_total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str) -> None:
    print(f"Test de total de mejoras por calle con numero {par_impar}:")
    res = total_mejoras_por_calle(viviendas, par_impar)
    separar_resultados(res.items())


def test_vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> None:
    res = vivienda_con_mejora_mas_rapida(viviendas)
    print(f"La vivienda que hizo una mejora en menos tiempo es: {res}")
    
def test_calle_mayor_diferencia_precios(viviendas: list[Vivienda]):
    res = calle_mayor_diferencia_precios(viviendas)
    print(f"La calle con mayor diferencia de precios es {res}")

def test_n_viviendas_top_valoradas_por_calle(viviendas: list[Vivienda], fecha: date|None = None, n: int = 3) -> None:
    res = n_viviendas_top_valoradas_por_calle(viviendas, fecha, n)
    print(f"Para n={4} y fecha {fecha} son:")
    for calle, lista_viviendas in res.items():
        print(f"{calle} --> {lista_viviendas}")




if __name__ == "__main__":
    
    ruta = "data\CSV de la sesión 2.csv"
    viviendas = lee_viviendas(ruta)
    
    #test_lee_viviendas(ruta)
    
    #test_total_mejoras_por_calle(viviendas, "par")
    #test_total_mejoras_por_calle(viviendas, "impar")
    
    #test_vivienda_con_mejora_mas_rapida(viviendas)
    
    #test_calle_mayor_diferencia_precios(viviendas)
    
    #test_n_viviendas_top_valoradas_por_calle(viviendas, date(2020,1 ,1), 4)
    #test_n_viviendas_top_valoradas_por_calle(viviendas)  #CON PARAMETROS POR DEFECTO
    
    
    
    
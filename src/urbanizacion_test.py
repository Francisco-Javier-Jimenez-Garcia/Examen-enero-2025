from urbanizacion import *

def separador_linea(simbolo):
    print(simbolo*120)

def test_lee_viviendas(ruta: str)-> list[Vivienda]:
    print(f"Test de lee viviendas con {len(lee_viviendas(ruta))} registros leidos:")
    print("Mostrando los 5 primeros registros:")
    print(lee_viviendas(ruta)[:5])
    separador_linea("=")
    print(lee_viviendas(ruta)[-5:])
    
    












if __name__ == "__main__":
    
    ruta = "data\CSV de la sesión 2.csv"
    test_lee_viviendas(ruta)
    
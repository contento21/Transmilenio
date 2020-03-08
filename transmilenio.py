import xml.etree.ElementTree as ET
from math import radians, cos, sin, asin, sqrt
from haversine import haversine, Unit

def main():
    print ("Bienvenido Transmilenio")
    print ("Leyendo estaciones de Transmilenio")
    transmiRutas = leerRutas()
    for estacion in transmiRutas:
        print(estacion)

    print("Ingrese la estacion uno: ")
    nomEstacionUno = input()
    print("Ingrese la estacion dos:")
    nomEstacionDos = input()

    calcularDistancia(nomEstacionUno, nomEstacionDos, transmiRutas)


def leerRutas():
    rutas = []
    arbol = ET.parse('transmilenio.xml')
    raiz = arbol.getroot()
    print(raiz.tag)
    for rama in raiz:
        print(rama.tag, rama.attrib)
        for estacion in rama:
            detalleEstacion = []
            for detalle in estacion:
                detalleEstacion.append(detalle.text)
            rutas.append(detalleEstacion)
    return rutas


def calcularDistancia(estacionUno, estacionDos, rutas):
    detalleEstacionUno = []
    detalleEstacionDos = []
    print(rutas)
    for estacion in rutas:
        if(len(estacion) > 0):
            print(estacion)
            if (estacionUno == estacion[0]):
                detalleEstacionUno = estacion
            if (estacionDos == estacion[0]):
                detalleEstacionDos = estacion

    print(detalleEstacionUno)
    print(detalleEstacionDos)
    print("Distanciaa entre estaciones")
    distancia = haversine1(float(detalleEstacionUno[1]), float(detalleEstacionUno[2]), float(detalleEstacionDos[1]), float(detalleEstacionDos[2]))
    print("Los kilometros son:")
    print("Metodo uno",distancia, "Km")
    distancia1 = haversine2(float(detalleEstacionUno[1]), float(detalleEstacionUno[2]), float(detalleEstacionDos[1]), float(detalleEstacionDos[2]))
    print("Metodo dos",distancia1, "Km")


def haversine1(lat1, lon1, lat2, lon2):
    #R = 3959.87433  # this is in miles.  For Earth radius in kilometers use 6372.8 km
    R = 6372.8

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return (R * c)


def haversine2 (lon1, lat1, lon2, lat2):
    EstacionUno = (lon1, lat1)
    EstacionDos = (lon2, lat2)
    resultado = haversine (EstacionUno,EstacionDos)
    return resultado


main()
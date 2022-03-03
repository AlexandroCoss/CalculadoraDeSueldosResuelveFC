import json
import funciones

golesMetaPorNivel = {'A':5,'B':10,'C':15,'Cuauh':20}

jsonDeJugadores = open("jsonEntrada.json", "r")
informacionDelJsonDeJugadores = jsonDeJugadores.read()

listaDeJugadores = json.loads(informacionDelJsonDeJugadores)


cantidadDeGolesMetaPorEquipo= funciones.obtenerMetaGolesPorEquipo(listaDeJugadores)
cantidadDeGolesPorEquipo= funciones.obtenerGolesPorEquipo(listaDeJugadores)
listadeJugadores= funciones.asignarSueldoAJugadores(listaDeJugadores,cantidadDeGolesPorEquipo,cantidadDeGolesMetaPorEquipo)
jsonDeJugadores.close()

jsonFinal = open("jsonSalida.json", "r+")
json.dump(listaDeJugadores, jsonFinal, indent=4)
print (listaDeJugadores)
jsonFinal.close()





"""for jugador in listaDeJugadores["jugadores"]:
    nivel = jugador["nivel"]
    cantidadDeGolesMetaPorEquipo = int(cantidadDeGolesMetaPorEquipo) + int(golesMetaPorNivel.get(nivel))
    cantidadDeGolesPorEquipo=int(cantidadDeGolesPorEquipo) + int(jugador["goles"])
print (cantidadDeGolesMetaPorEquipo)
print (cantidadDeGolesPorEquipo) 



for jugador in listaDeJugadores["jugadores"]:
    sueldoFinal=0
    nivel = jugador["nivel"]
    print (nivel)
    golesMeta= golesMetaPorNivel.get(nivel)
    print (golesMeta)
    sueldoBase= jugador["sueldo"]
    bonoMaximo= jugador["bono"]
    goles= jugador["goles"]
    cantidadDeBonoIndividual= (goles*bonoMaximo)/golesMeta
    cantidadDeBonoPorEquipo= (cantidadDeGolesPorEquipo*bonoMaximo)/cantidadDeGolesMetaPorEquipo
    print (cantidadDeBonoIndividual)
    print (cantidadDeBonoPorEquipo)
    bonoTotal = (cantidadDeBonoPorEquipo + cantidadDeBonoIndividual)/2
    print (bonoTotal)
    jugador["sueldo_completo"] = int(jugador["sueldo"]) + bonoTotal"""




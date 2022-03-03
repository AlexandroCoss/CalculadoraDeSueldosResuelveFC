def sumaSuma (numero1, numero2):
    resultado=numero1+numero2
    return resultado 

golesMetaPorNivel = {'A':5,'B':10,'C':15,'Cuauh':20}

def obtenerMetaGolesPorEquipo(listaDeJugadores):
    cantidadDeGolesMetaPorEquipo='0'
    for jugador in listaDeJugadores["jugadores"]:
        nivel = jugador["nivel"]
        cantidadDeGolesMetaPorEquipo = int(cantidadDeGolesMetaPorEquipo) + int(golesMetaPorNivel.get(nivel))
    return cantidadDeGolesMetaPorEquipo

def obtenerGolesPorEquipo (listaDeJugadores):
    cantidadDeGolesPorEquipo='0'
    for jugador in listaDeJugadores["jugadores"]:
        cantidadDeGolesPorEquipo=int(cantidadDeGolesPorEquipo) + int(jugador["goles"])
    return cantidadDeGolesPorEquipo


def asignarSueldoAJugadores(listaDeJugadores,cantidadDeGolesPorEquipo, cantidadDeGolesMetaPorEquipo):
    for jugador in listaDeJugadores["jugadores"]:
        nivel = jugador["nivel"]
        golesMeta= golesMetaPorNivel.get(nivel)
        sueldoBase= jugador["sueldo"]
        bonoMaximo= jugador["bono"]
        goles= jugador["goles"]
        cantidadDeBonoIndividual= (goles*bonoMaximo)/golesMeta
        cantidadDeBonoPorEquipo= (cantidadDeGolesPorEquipo*bonoMaximo)/cantidadDeGolesMetaPorEquipo
        bonoTotal = (cantidadDeBonoPorEquipo + cantidadDeBonoIndividual)/2
        jugador["sueldo_completo"] = int(jugador["sueldo"]) + bonoTotal
    return listaDeJugadores
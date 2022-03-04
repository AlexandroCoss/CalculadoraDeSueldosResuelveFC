import json

jsonDeNiveles = open("niveles.json", "r+")
informacionDelJsonDeNiveles = jsonDeNiveles.read()
niveles = json.loads(informacionDelJsonDeNiveles)


#metodo Para obtener la Meta de goles por equipo
def obtenerMetaGolesPorEquipo(listaDeJugadores):
    cantidadDeGolesMetaPorEquipo='0'
    #recorremos el la lista de jugadores y sumamos cada meta propia dependiendo del nivel de cada jugador
    for jugador in listaDeJugadores["jugadores"]:
        nivel = jugador["nivel"]
        cantidadDeGolesMetaPorEquipo = int(cantidadDeGolesMetaPorEquipo) + int(niveles[nivel])
    return cantidadDeGolesMetaPorEquipo

#metodo para obtener los goles por equipo
def obtenerGolesPorEquipo (listaDeJugadores):
    cantidadDeGolesPorEquipo='0'
    #recorremos la lista y sumamos a una variable los goles anotados por cada jugador 
    for jugador in listaDeJugadores["jugadores"]:
        cantidadDeGolesPorEquipo=int(cantidadDeGolesPorEquipo) + int(jugador["goles"])
    return cantidadDeGolesPorEquipo

#metodo para calcular y asignar el sueldo final de cada jugador
def asignarSueldoAJugadores(listaDeJugadores,cantidadDeGolesPorEquipo, cantidadDeGolesMetaPorEquipo):
    #asignamos a variables independientes la informacion de cada jugador desde el objeto que optuvimos del jsonEntrada
    for jugador in listaDeJugadores["jugadores"]:
        nivel = jugador["nivel"]
        golesMeta= niveles[nivel]
        sueldoBase= jugador["sueldo"]
        bonoMaximo= jugador["bono"]
        goles= jugador["goles"]
        #calculamos el porcentaje de bono que corresponde a cada jugador dependiendo de sus goles meta y su bono propio
        cantidadDeBonoIndividual= (goles*bonoMaximo)/golesMeta
        cantidadDeBonoPorEquipo= (cantidadDeGolesPorEquipo*bonoMaximo)/cantidadDeGolesMetaPorEquipo
        bonoTotal = (cantidadDeBonoPorEquipo + cantidadDeBonoIndividual)/2
        #sumamos al sueldo base del jugador el bono correspondinte y lo agregamos al objeto en la seccion "sueldo_completo"
        jugador["sueldo_completo"] = int(jugador["sueldo"]) + bonoTotal
    return listaDeJugadores

jsonDeNiveles.close()


import json
import funciones



#El programa empieza recibiendo un archivo Json como entrada, para simular esta entrada agregue al proyecto un archivo Json
#con la informacion de los jugadores
#ademas del Json con la informacion de los jugadores hice un json aparte con la informacion de las metas por gol de cada clase
#de esta forma si se necesita agregar nuevas metas o modificar las existentes, puedes modificarse unicamente ese json
jsonDeJugadores = open("jsonEntrada.json", "r")
informacionDelJsonDeJugadores = jsonDeJugadores.read()

#transformamos la informacion de ese archivo Json en un objeto manejable por Python 
listaDeJugadores = json.loads(informacionDelJsonDeJugadores)

#usamos la funcion para obtener la cantidad de goles meta por equipo
cantidadDeGolesMetaPorEquipo= funciones.obtenerMetaGolesPorEquipo(listaDeJugadores)

#asi mismo obtenemos la cantidad de goles que apunto el equipo usando la funcion cantidadDeGolesPorEquipo
cantidadDeGolesPorEquipo= funciones.obtenerGolesPorEquipo(listaDeJugadores)

#con los resultados de las 2 funciones anteriores alimentamos una tercera funcion que hara el calculo completo del sueldo final de cada jugador
#ademas de modificar el objeto del Json para agregarle esta infomacion en la seccion #sueldo_completo
listadeJugadores= funciones.asignarSueldoAJugadores(listaDeJugadores,cantidadDeGolesPorEquipo,cantidadDeGolesMetaPorEquipo)
jsonDeJugadores.close()

#por ultimo convertimos el objeto anterior en un json y lo grabamos como un archivo nuevo llamado jsonSalida
jsonFinal = open("jsonSalida.json", "r+")
json.dump(listaDeJugadores, jsonFinal, indent=4)
print (listaDeJugadores)
jsonFinal.close()

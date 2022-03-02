import json
f = open("json.json", "r")
c = f.read()

golesMetaPorNivel = {'A':5,'B':10,'C':15,'Cuauh':20}

f.close()


listaDeJugadores = json.loads(c)

cantidadDeGolesMetaPorEquipo='0'
cantidadDeGolesPorEquipo='0'
for jugador in listaDeJugadores["jugadores"]:
    nivel = jugador["nivel"]
    cantidadDeGolesMetaPorEquipo = int(cantidadDeGolesMetaPorEquipo) + int(golesMetaPorNivel.get(nivel))
    cantidadDeGolesPorEquipo=int(cantidadDeGolesPorEquipo) + int(jugador["goles"])
print (cantidadDeGolesMetaPorEquipo)
print (cantidadDeGolesPorEquipo) 

a_file = open("json.json", "r+")
listaDeJugadores = json.load(a_file)

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
    jugador["sueldo_completo"] = int(jugador["sueldo"]) + bonoTotal
    
a_file.close()

b_file = open("Json entrada.json", "r+")
json.dump(listaDeJugadores, b_file, indent=4)
print (listaDeJugadores)
b_file.close()


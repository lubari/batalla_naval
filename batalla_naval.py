MAX = 24
MIN = 10

def elegir_jugador():
	sandokan = "Sandokan y sus valientes amigos"
	armada =  "Armada Britanica"
	personaje = ""

	print("Usted puede elegir:\n 1 - Sandokan y sus valientes amigos\n 2 - Armada Britanica\n")
	jugador = input("Ingrese el jugador con el que desea jugar: \n")

	while jugador != '1' and jugador != '2':
		jugador = input("Ingrese 1 o 2 para elegir su jugador: \n")

	if jugador == '1':
		personaje = sandokan
	else:
		personaje = armada

	print(f"Usted eligió : {personaje}")
	return jugador

def elegir_tamanio():
	print("El minimo del tablero es de 10 y su maximo 24")
	tamanio = input("Eliga el tamanio deseado del tablero: \n")

	while not tamanio.isdecimal() or int(tamanio) < MIN or int(tamanio) > MAX:
		tamanio = input("Eliga el tamanio deseado del tablero: \n")

	print(f"El tamanio elegido es: {tamanio}")
	return int(tamanio)

def crear_tablero(tamanio):
	tablero = []

	for i in range(tamanio):	
		fila = []

		for i in range(tamanio):
			fila.append(i)
		print(fila)
		tablero.append(fila)
		
	return tablero

def main():
	hilos = [310,1072,1064,170,1010,366,347,387,1009,132,291,1068,100,122,177,941,936,358,361,62,29,55,23,297,85,433,778,268,387,328,288,206,209,683,410,1021,942,362]
	hilos.append(336)
	print(len(hilos))
	print(sorted(hilos))

main()
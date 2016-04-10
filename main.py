import fichero, tablero, settings, util

fichas = fichero.get_fichero_vacio();
fichero.completar_fichas_iniciales(fichas);

turnos = 0
jugador = settings.PRIMER_TURNO
sin_jugadas = 0

while turnos < settings.TURNOS_MAXIMO and sin_jugadas < 2 and fichero.hay_fichas_vacias(fichas):
	tablero.dibujar_tablero(fichas)

	jugadas_disponibles = fichero.obtener_jugadas_disponible(fichas, jugador)

	if len(jugadas_disponibles) > 0:
		coordenada = input(util.mensaje_bienvenida(jugador) + "Ingrese un movimiento válido (" + fichero.obtener_cadena_de_jugadas_disponibles(jugadas_disponibles) + "): ")

		while not fichero.es_movimiento_valido(coordenada, jugadas_disponibles):
			coordenada = input(util.mensaje_bienvenida(jugador) + "Ingrese un movimiento válido (" + fichero.obtener_cadena_de_jugadas_disponibles(jugadas_disponibles) + "): ")

		fichero.colocar_ficha(fichas, fichero.get_coordenada(coordenada), jugador)

		sin_jugadas = 0
		turnos += 1
	else:
		sin_jugadas += 1

		if sin_jugadas == 2:
			break
		
		siguiente_turno = input("El jugador " + jugador + " no tiene movimientos disponibles. Presiona enter para continuar: ")

		while not siguiente_turno == '':
			siguiente_turno = input("El jugador " + jugador + " no tiene movimientos disponibles. Presiona enter para continuar: ")

	jugador = util.get_oponente(jugador)


tablero.dibujar_tablero(fichas)

ganador = fichero.obtener_ganador(fichas)

if ganador == 'empate':
	print("\n" + 'Increíble pero real! Sólo el 5% de las partidas de Reversi terminan en un empate, y este es uno de esos casos.')
else:
	print("\n" + 'Felicidades al jugador ' + ganador + '. Muy bien jugado!')
import settings

def get_letra_by_numero(num):
	'''devuelve la letra correspondiente al numero (ej: 1=>A, 3=>C)'''
	return str(chr(65 + num));

def get_numero_by_letra(letra):
	'''devuelve el numero correspondiente a la letra (ej: A=>1, C=>3)'''
	return ord(letra) - 65;

def get_simbolo_jugador(jugador):
	'''devuelve el simbolo del jugador del parametro'''
	return settings.SIMBOLOS_JUGADORES[0] if jugador == 'blanco' else settings.SIMBOLOS_JUGADORES[1]

def get_jugador_por_simbolo(simbolo):
	'''devuelve el jugador del simbolo del parametro'''
	return 'blanco' if settings.SIMBOLOS_JUGADORES[0] else 'negro'

def get_oponente(jugador):
	'''devuelve el oponenente al jugador del parametro'''
	return 'negro' if jugador == 'blanco' else 'blanco'

def mensaje_bienvenida(jugador):
	'''devuelve el mensaje de bienvenida del jugador del parametro'''
	return 'Es el turno del jugador ' + jugador + '. '
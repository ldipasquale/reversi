from math import floor
import settings, util


def get_fichero_vacio():
	'''devuelve un fichero vacio con la dimension seteada en settings'''
	fichas = []

	for i in range(0, settings.ALTO):
		ficha = []
		for j in range(0, settings.ANCHO):
			ficha.append('')

		fichas.append(ficha)

	return fichas


def completar_fichas_iniciales(fichas):
	'''completa las fichas con los valores iniciales (4 en el medio del tablero)'''
	from_x = floor(settings.ALTO / 2) - 1
	from_y = floor(settings.ANCHO / 2) - 1

	for i in range(from_y, from_y + 2):
		for j in range(from_x, from_x + 2):
			fichas[j][i] = util.get_simbolo_jugador('blanco') if i == j else util.get_simbolo_jugador('negro')

	return fichas


def hay_fichas_vacias(fichas):
	'''certifica que haya fichas vacias'''
	for fichas_x in fichas:
		for ficha in fichas_x:
			if ficha == '':
				return True

	return False


def obtener_ganador(fichas):
	fichas_blanco = 0
	fichas_negro = 0

	for fichas_x in fichas:
		for ficha in fichas_x:
			if ficha == util.get_simbolo_jugador('blanco'):
				fichas_blanco += 1
			elif ficha == util.get_simbolo_jugador('negro'):
				fichas_negro += 1

	if fichas_blanco == fichas_negro:
		return 'empate'

	return 'negro' if fichas_negro > fichas_blanco else 'blanco'


def obtener_jugadas_disponible(fichas, jugador):
	'''obtiene las jugadas disponibles para el jugador del parametro'''
	jugadas_disponibles = []

	for x in range(0, settings.ALTO):
		for y in range(0, settings.ANCHO):
			if validar_movimiento(fichas, (x, y), jugador):
				jugadas_disponibles.append((x, y))

	return jugadas_disponibles


def obtener_cadena_de_jugadas_disponibles(jugadas_disponibles):
	cadena = ""

	for coordenada in jugadas_disponibles:
		cadena += str(coordenada[1] + 1) + util.get_letra_by_numero(coordenada[0]) + ", "

	return cadena[:-2]

def es_movimiento_valido(movimiento, jugadas_disponibles):
	'''certifica que el movimiento del parametro sea valido (que sea una coordenada, y que este dentro de las jugadas disponibles (lista de coordenadas))'''
	if es_coordenada_valida(movimiento):
		coordenada = get_coordenada(movimiento)

		return coordenada in jugadas_disponibles

	return False


def es_coordenada_valida(movimiento):
	'''existe un movimiento valido con el movimiento del parametro?'''
	if es_coordenada(movimiento):
		x, y = get_coordenada(movimiento)

		return existe_coordenada(x, y)

	return False

def existe_coordenada(x, y):
	'''existe coordenada (entre 0 y el ancho/alto seteado)'''
	return x >= 0 and x < settings.ALTO and y >= 0 and y < settings.ANCHO


def es_coordenada(str):
	'''valida que el parametro sea una coordenada (2A, 5D, 3B)'''
	if len(str) == 2:
		return str[0].isdigit() and str[1].isalpha()

	return False


def esta_vacio(fichas, coordenada):
	'''validar que la coordenada del parametro este vacia'''
	x, y = coordenada

	return fichas[x][y] == ''


def validar_movimiento(fichas, coordenada, jugador):
	'''valida que la coordenada este vacia y que alguna de las lineas formadas entre el movimiento y alguna ficha del enemigo termine en una ficha del jugador'''
	return esta_vacio(fichas, coordenada) and len(obtener_lineas_a_pintar(fichas, coordenada, jugador)) > 0


def obtener_lineas_a_pintar(fichas, coordenada, jugador):
	'''obtiene las lineas a pintar segun coordenada y jugador'''
	lineas_analizables = obtener_fichas_alrededor_oponente(fichas, coordenada, jugador)
	lineas_a_pintar = []

	for coordenada_distancia in lineas_analizables:
		if obtener_ficha_final_de_linea(fichas, coordenada, coordenada_distancia, jugador) == util.get_simbolo_jugador(jugador):
			lineas_a_pintar.append(coordenada_distancia)

	return lineas_a_pintar


def obtener_ficha_final_de_linea(fichas, coordenada, coordenada_distancia, jugador):
	'''obtiene la ficha final (que no sea la del oponente) de la linea'''
	x, y = coordenada
	distancia_x, distancia_y = coordenada_distancia

	x += distancia_x
	y += distancia_y

	while fichas[x][y] == util.get_simbolo_jugador(util.get_oponente(jugador)):
		x += distancia_x
		y += distancia_y

		if not existe_coordenada(x, y):
			return ''

	return fichas[x][y]

def obtener_fichas_alrededor_oponente(fichas, coordenada, jugador):
	'''obtener una lista con la distancia (xy) de las fichas enemigas de alrededor'''
	x, y = coordenada
	fichas_oponente_alrededor = []

	for coordenada_x in range(x - 1, x + 2):
		for coordenada_y in range(y - 1, y + 2):
			if (coordenada_x != x or coordenada_y != y) and existe_ficha_de_oponente(fichas, coordenada_x, coordenada_y, jugador):
				fichas_oponente_alrededor.append((coordenada_x - x, coordenada_y - y))

	return fichas_oponente_alrededor


def existe_ficha_de_oponente(fichas, x, y, jugador):
	'''existe una ficha del oponente en la coordenada del parametro?'''
	if existe_coordenada(x, y):
		return fichas[x][y] == util.get_simbolo_jugador(util.get_oponente(jugador))


def get_coordenada(movimiento):
	'''obtiene las partes de la coordenada (x e y) de un movimiento, teniendo en cuenta que este movimiento es una coordenada validada'''
	return (util.get_numero_by_letra(movimiento[1]), int(movimiento[0]) - 1)


def colocar_ficha(fichas, coordenada, jugador):
	'''coloca la ficha del jugador correspondiente en la coordenada correspondiente, colocando las fichas capturadas'''
	x, y = coordenada

	fichas[x][y] = util.get_simbolo_jugador(jugador)
	capturar_fichas(fichas, coordenada, jugador)


def capturar_fichas(fichas, coordenada, jugador):
	for coordenada_distancia in obtener_lineas_a_pintar(fichas, coordenada, jugador):
		pintar_linea(fichas, coordenada, coordenada_distancia, jugador)


def pintar_linea(fichas, coordenada, coordenada_distancia, jugador):
	x, y = coordenada
	distancia_x, distancia_y = coordenada_distancia

	x += distancia_x
	y += distancia_y

	while fichas[x][y] == util.get_simbolo_jugador(util.get_oponente(jugador)):
		fichas[x][y] = util.get_simbolo_jugador(jugador)

		x += distancia_x
		y += distancia_y

		if not existe_coordenada(x, y):
			break
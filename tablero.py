import settings, os, util

def dibujar_tablero(fichas):
	'''dibuja un tablero con las fichas del parametro'''
	limpiar_consola()

	print(get_fila_inicial())

	print(get_fila_separador())

	for i, ficha_x in enumerate(fichas):
		print(util.get_letra_by_numero(i) + ' |', end=' ')
		for ficha_xy in ficha_x:
			print(ficha_xy if ficha_xy != '' else settings.SIMBOLO_VACIO, end=' ')
		print('|')

	print(get_fila_separador())


def get_fila_inicial():
	'''devuelve la fila inicial'''
	fila_inicial = '';
	for j in range(1, settings.ANCHO + 1):
		fila_inicial += str(j) + ' '

	return '    ' + fila_inicial


def get_fila_separador():
	'''devuelve la fila separador'''
	return	'    ' + '- ' * settings.ANCHO;


def limpiar_consola():
	'''limpia la consola'''
	os.system('cls' if os.name=='nt' else 'clear')
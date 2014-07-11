# -*- coding: utf-8 -*-

rango_permitidas = xrange(ord('a'), ord('z')+1)

def contar_letras( palabra = "" ):
	if type(palabra) != str:
		raise Exception("Tipo de entrada no permitido")

	contador = {}
	for letra in palabra.lower():
		if ord(letra) in rango_permitidas:
			contador[letra] = contador.get(letra,0) + 1 
	
	return contador

print contar_letras("Hola hola HOLA")
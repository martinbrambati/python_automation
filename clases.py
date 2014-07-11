class Persona(object):
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido

	def saludar(self, saludo):
		 saludo(self.nombre)
		 


def saludo(nombre):
	print "Hola " + nombre


p = Persona("Tincho","B")
p.saludar( saludo )




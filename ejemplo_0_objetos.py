#


# def saludar(quien, nombre):
# 	print(f"{quien} dice: Hola {nombre}.")

# saludar("Profesor", "MCOC")

#Objeto ---> Personas
#Accion ---> Saludan




class Persona(object):
	"""Ayuda para esta"""
	def __init__(self, nombre):  #constructor
		super(Persona, self).__init__()
		self.nombre = nombre       # atributo (datos)

	def decir_nombre(self):  #metodos de clase
		return self.nombre

	def cambiar_nombre(self, nombre_nuevo):  #metodos de clase
		self.nombre = nombre_nuevo
		
	def saludar(self, otra_persona):
		quien = self.decir_nombre()
		otro = otra_persona.decir_nombre()
		print(f"{quien} dice: Hola {otro}.")

	def intercambiar_nombres(self,otra_persona):
		quien=self.decir_nombre()
		otro=otra_persona.decir_nombre()
		self.cambiar_nombre(otro)
		otra_persona.cambiar_nombre(quien)

profe = Persona("profe")
alumno = Persona("alumno")

profe = Persona("Albus")
alumno  = Persona("Severus")

alumno.saludar(profe)
profe.saludar(alumno)

profe.cambiar_nombre("Albus Percival Wulfric Brian")

alumno.saludar(profe)

profe.intercambiar_nombres(alumno)

print("El profesor es: {}".format(profe.decir_nombre()))
print("El alumno es: {}".format(alumno.decir_nombre()))













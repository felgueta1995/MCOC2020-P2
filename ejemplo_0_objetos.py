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


profe = Persona("profe")
alumno = Persona("alumno")

profe = Persona("Albus")
alumno  = Persona("Severus")


<<<<<<< HEAD
profe.cambiar_nombre("Harry Potter")


=======
>>>>>>> parent of 1a9d32b... Revert "Revert "Updated cambiar nombre and intercambiar nombres""

profe.saludar(alumno)
alumno.saludar(profe)















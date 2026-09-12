# Tipos de variables en python
# Guerrero Aguilar Gullemro
# 24/03/25

''' El tipado de python es dinámico, por lo que no es necesario escribir el tipo de 
    variable antes de su declaración
'''
variable = "Hola Mundo"   
print(variable)
print(type(variable))  # Variable de tipo str -> texto entre comillas dobles o simples

variable = 10             
print(variable)
print(type(variable))  # Variable de tipo entero (int)

variable = 45.6           
print(variable)
print(type(variable))  # Variable de tipo flotante (float)

variable = 1
variable = bool(variable)     #El método bool hace el casting de int a bool
print(variable)
print(type(variable))  # Variable de tipo bool (True - false)

variable = 0
variable = bool(variable)     #El método bool hace el casting de int a bool
print(variable)
print(type(variable))  # Variable de tipo bool (True - false)

variable = True
print(variable)
print(type(variable))  # Variable de tipo bool (True - false)

variable = False
print(variable)
print(type(variable))  # Variable de tipo bool (True - false)

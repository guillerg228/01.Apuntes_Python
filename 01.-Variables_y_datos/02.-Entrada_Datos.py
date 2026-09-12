# Entrada de datos
# Guerrero Aguilar Gullemro
# 24/03/25

variable = input("Ingrese un mensaje: ")
print(variable)
print(type(variable))

''' La funcion input recibe datos por teclado mediante la consola, sin embargo
    los parámetros ingresados en dicha función siempre serán de tipo str, por lo que
    si se requiere ingresar tipos de datos diferentes, es necesario el casting de datos'''

variable = int(input('Ingrese un numero entero: ')) #Converción a int
print(variable)
print(type(variable))

variable = float(input('Ingrese un numero flotante: '))
print(variable)
print(type(variable))
# Metodos que se pueden usar para cadenas
# Guerrero Aguilar Guillermo
# 25/03/25

''' Los métodos son acciones que se pueden realizar a partir de objetos, en este caso se presentan acciones
    para objetos de tipo string'''

cadena = "hola mundo"
cadena = cadena.title()  #Convierte el texto en fomato de título
print(cadena)

cadena = cadena.upper()  #Convierte el texto a mayusculas
print(cadena)

cadena = cadena.lower()  #Convierte el texto a minusculas
print(cadena)

cadena = cadena.capitalize()#El primer caracter de la cadena se hace mayuscula
print(cadena)

cadena = "hola, Hola, hola mundo"
print(cadena.count('hola')) #El método count retorna el número de veces se repite la subcadena

print(cadena.find('Hola')) #Retorna el índice en el que encuentra el caracter o subcadena

print(cadena.find('jfkdsal')) #Si la cadena a buscar no existe, retorna un -1

print(cadena.index('mundo')) #El método index retorna el índice en que que encuentra el caracter o la subcadena

'''print(cadena.index('jkfldas')) #En caso de que le método index no encuentre el parámetro, retorna un error'''

cadena = cadena.replace('hola', 'hello') #Podemos reemplazar una subcadena dentro de la cadena principal con el método replace
print(cadena)

print('hello' in cadena) #Se usa in como operador de pertenecia para verificar si una subcadena está dentro de una cadena

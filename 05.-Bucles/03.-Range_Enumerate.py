# Funciones Range y enumerate
# Guerrero Aguilar Guillemrmo
# 28/03/25

for n in range(5):  # La función range establece un rango de números en los cuales itera
    print(n)

print('\n')
for n in range(5,10):  # En la iteración nunca se incluye 
    print(n)

print('\n')
for n in range(10,21,2):  # La función range nos permite incluir un tercer número para establecer un periodo 
    print(n)

''' La función enumerate itera la lista que se le pasa como parámetro para guardarla en la segunda variable después
    del for, la primera variable guarda el índice que devuelve. El segundo parámetro que se le pasa a la funcion
    es el indice en el que se empézará a enumerar, si este parámetro se queda vacío, se define como cero'''

print('\n')
frutas = ['Manzana', 'Uva', 'Naranja', 'Mandarina', 'Platano', 'Mango']
for index, elemento in enumerate(frutas,45):
    print(index, elemento)
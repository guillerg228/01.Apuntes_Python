# Más métodos de listas
# Guerrero Aguilar Guillermo
# 25/03/25

frutas = ['manzana', 'platano', 'naranja', 'uva']
verduras = ['zanahoria', 'brocoli']
print(frutas)
print(verduras)

frutas.append('tomate')
print(frutas)

frutas.extend(verduras) # El método extend sirve para que a partir de una lista, se le agresgue otra
print(frutas)

frutas.insert(1, 'mandarina') # El método insert, inserta el un elemento en el índice indicado como parámetro
print(frutas)

frutas.remove('brocoli') # Elimina el elemento señalado como parámetro
print(frutas)

frutas.pop()   #El método pop() (sin indicar un parámetro de entrada), elimina el último elemento de una lista
print(frutas)

frutas.pop(1)  #El método pop(i) con parametro de entrada 'i' elimina el elemento de la lista com íncice i 
print(frutas)

print(frutas.index('uva')) # El método index retorna el índice del elemento pasado como parámetro de entrada

frutas.append('manzana')
print(frutas.count('manzana')) # El método count retorna el número de elementos iguales al parámetro de entrada

frutas.reverse()
print(frutas) # El método invierte la cadena 
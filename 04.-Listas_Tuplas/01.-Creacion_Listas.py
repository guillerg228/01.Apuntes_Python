# Aspectos básicos de listas
# Guerrero Aguilar Guillermo
# 25/03/25

''' Las listas son un tipo de datos que contienen diferentes elementos a los cuales se puede acceder mediante
    índices'''

lista1 = ['Rojo', 'Verde', 7, True, 45.2]  #Las listas pueden contener distintos tipos de datos, a demás de ser mutables  
print(lista1)

print(lista1[0])   #Se puede acceder a los elementos mediante indices de igual manera que las cadenas
print(lista1[-1])

print(len(lista1)) #El método len retorna el número de elementos que contiene la lista

lista1.append('Guillermo')  #El método 'append' agrega un elemento al final de la lista
print(lista1)

lista1.remove('Verde')   #El método 'remove' elimina de la lista al elemento pasado como parámetro 
print(lista1)

lista1[0] = 'Amarillo'  #Se puede modificar un elemento de la lista a partir de su índice
print(lista1)

print(7 in lista1)  #Podemos verificar que algún elemento esté o no en la lista usando un operador de pertenecia
print(False in lista1)


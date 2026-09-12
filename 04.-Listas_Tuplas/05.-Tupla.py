# Tuplas
# Guerrero Aguilar Guillermo
# 25/03/25

''' Las tuplas, al igual que las listas, son colecciones de datos , sin embargo, la principal diferencia entre
    una lista y una tupla es que la tupla es inmutable, lo que quiere decir que no se puede modificar '''

tupla1 = (1, 2, 3, 4, 5)  # Las tuplas se declaran entre paréntesis
print(tupla1)
print(type(tupla1))

lista1 = [45, 78, 2, 12, 6, 32, 8]
print(lista1)
print(type(lista1))
lista1 = tuple(lista1)   # Con la fución tuple() podemos convertur una lista en una tupla
print(lista1)
print(type(lista1))

print(lista1.index(12)) # La función index, al igual que en las listas, retorna el índice de un elemeto de la tupla


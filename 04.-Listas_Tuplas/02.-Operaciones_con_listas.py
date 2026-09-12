# Operaciones con listas
# Guerrero Aguilar Guillermo
# 25/03/25

''' Se pueden realizar operaciones con listas tales como sumas o multiplicaciones que pueden resultar
    útiles en un futuro'''

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

listaRes = lista1 + lista2  #La suma de dos listas es igual a otra con las componentes de ambas
print(listaRes)

listaRes = lista1*3  #La multiplicacion de una lista por un núermo es otra que contiene la original tres veces
print(listaRes)

print(listaRes[:4])    #Podemos tomar porciones de la lista al igual que las cadenas
print(listaRes[-4:-1]) #(El último núermo del intervalo nunca se incluye)
print(listaRes[::-1])  #Invierte lista
print(listaRes[2:7:2]) #Retorna los elementos del índice 2 hasta antes del 7 de dos en dos

listaRes = [56, 123, 78, 2, 6, 789]
print(listaRes)
listaRes.sort() #El método sort() ordena en orden ascendente la lista
print(listaRes)

listaRes = [56, 123, 78, 2, 6, 789]
print(listaRes)
listaRes = sorted(listaRes) #De igual manera podemos ordenar la lista con la función sorted
print(listaRes)

listaRes.sort(reverse=True)  # Para ordenarlos descendentemente se usa el método .sort(reverse=True)
print(listaRes)



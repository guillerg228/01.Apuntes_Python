# Pilas y Colas
# Guerrero Aguilar Guillermo
# 25/03/25

''' Las pilas y colas son estructuras de datos que podemos representar como listas. Por una parte, 
        las pilas siguen el principio de LIFO (Last Int, First Out), lo que quiere decir que el último 
        elemento en entrar es el primero en salir.

        Las colas, por su parte, siguen el principio de FIFO (Last Int, First Out), lo que quiere decir
        que el primer elemento en entrar es el primero es salir '''

pila = []
pila.append(1)  #Se agrega un elemento al final de la lista
print(pila)
pila.append(2)
print(pila)
pila.append(3)
print(pila)
pila.append(4)
print(pila)
pila.append(5)
print(pila)

pila.pop()   #Se elimina el último elemento en entrar a la lita
print(pila)
pila.pop()
print(pila)
pila.pop()
print(pila,'\n')


cola = []
cola.append(1)  #Se agrega un elemento al final de la lista
print(cola)
cola.append(2)
print(cola)
cola.append(3)
print(cola)
cola.append(4)
print(cola)
cola.append(5)
print(cola)

cola.pop(0)   #Se elimina el preimer elemento en entrar a la lita
print(cola)
cola.pop(0)
print(cola)
cola.pop(0)
print(cola,'\n')


from collections import deque   #La cola tambien se puede hacer con una librería
cola2 = deque()

cola2.append(1)  #Se agrega un elemento al final de la lista
print(cola2)
cola2.append(2)
print(cola2)
cola2.append(3)
print(cola2)
print(type(cola2))

cola2.popleft() #Se elimina el preimer elemento en entrar a la lita
print(cola2)
cola2.popleft()
print(cola2)

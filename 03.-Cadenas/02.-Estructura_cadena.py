# Estructura de una cadena de texto
# Guerrero Aguilar Gullemro
# 24/03/25

''' Una cadena de texto se puede estructurar en indices, lo que quiere decir que a cada carater de la cadena se
    se puede asignar un número dependiendo de la posición en la que se encuentre a lo largo de la cadena.
    Los índices de las cadenas simpre inician en cero, por ejemplo,
    
    cadena = "Hola mundo"  ----->     H = cadena[0], o = cadena[1], l =  cadena[2], ... , o = cadena[9]
    .                      ----->     H = cadena[-10], o = cadena[-9], l = cadena[-8], ...  ,o = cadena[-1]'''

cadena = "Guillermo"
print(len(cadena))  #La funcion len retorna el número de caracteres que hay en una cadena

caracter = cadena[0]  #La variable que contiene un String, seguido de [n] extrae el indice n de la cadena
print(caracter)

caracter = cadena[5]
print(caracter)

caracter = cadena[-3]
print(caracter)

caracter = cadena[0:4] #Extraemos desde el índice 0 hasta antes del índice 4 (indice 3)
print(caracter)

caracter = cadena[-7: -3] #Extraemos desde el índice -7 hasta antes del índice -3 (índice -4)
print(caracter)

caracter = cadena[::2] # Desde el primer índice hasta el último se toma, pero de dos en dos
print(caracter)

caracter = cadena[1:8:3]# Tomamos desde el 2 hasta el 8 de tres en tres
print(caracter)

'''  cadena[0] = "E"        
        #Las cadenas son inmutables, por lo que no se pueden modificar, y esta línea no es válda'''

cadena = 'E'+cadena[1:]  #Podemos modificar la cadena re definiendola como una concatenación
print(cadena)  #Tomamos el caracter E y lo concatenamos con la cadena desde el indice 1 hasta el fin

cadena += " Antonio";  # En general, podemos re definir las cadenas para modificarlas
print(cadena)
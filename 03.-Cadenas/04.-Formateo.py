# Formateo de cadenas
# Guerrero Aguilar Guillermo 
# 25/03/25
''' A continuacion se veran distintos métodos para el formateo de datos dentro de cadenas'''

nombre = 'Guillermo'
edad = 18
estatura = 1.70

print('* Nombre: ', nombre,'\n Edad: ',edad,'\n Estatura: ',estatura)

cadena = '* Nombre: ', nombre,'\n Edad: ',edad,'\n Estatura: ',estatura
print(cadena) #La cadena se concatena, sin embargo lo hace entre paréntesis y con comas entre elementos

cadena = '* Nombre: '+ nombre +'\n Edad: '+ str(edad) + '\n Estatura: ' + str(estatura)
print(cadena) #La cadena se concatena de manera correcta pero es necesario hacer casting de datos

cadena = '* Nombre: %s \n Edad: %d \n Estatura: %.2f' %(nombre, edad, estatura)
print(cadena) #Se puede formatear con notacion de porcentajes

cadena = '* Nombre: {} \n Edad: {} \n Estatura: {:.2f}'.format(nombre, edad, estatura)
print(cadena) #Uso del método format

cadena = f'* Nombre: {nombre} \n Edad: {edad} \n Estatura: {estatura:.2f}'
print(cadena) #Uso del fprint
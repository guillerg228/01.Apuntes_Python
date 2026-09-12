# Bucle While
# Guerrero Aguilar Guillermo
# 25/03/25

''' El bucle while permite ejecutar un bloque de código repetidas veces, siempre y cuando se cumpla 
    una condición. Ejemplo:

contador = 0

while contador < 10:
    contador +=1;
    print(contador)
'''

#Practica agragar productos

lista_produtos = []
pIngresado = ''

while pIngresado != 'echo':
    pIngresado = input("Ingrese un producto. Digite 'echo' para finalizar la operacion: ")
    if pIngresado != 'echo':
        lista_produtos.append(pIngresado)
    else:
        break

#print(lista_produtos)

indice = 0
contador = 0
print('\n Lista de Productos: ')
while indice <= len(lista_produtos)-1:
    contador += 1
    print(f'  {contador}. {lista_produtos[indice]}')
    indice+=1

# Uso del bucle For
# Guerrero Aguilar Guillemrmo
# 28/03/25

''' El bucle for es usado para iterar, principalmente dentro de cadenas y listas, por ejemplo: 

lista = [1, 2, 3, 4, 5, 6, 7]
for elemento in lista:
    print(elemento)

'''
lista_produtos = []
pIngresado = ''

while pIngresado != 'echo':
    pIngresado = input("Ingrese un producto. Digite 'echo' para finalizar la operacion: ")
    if pIngresado != 'echo':
        lista_produtos.append(pIngresado)
    else:
        break

contador = 1;
print('\n*Lista de productos: ')
for produto in lista_produtos:
    print(f'{contador}. {produto}')
    contador+=1
# Condicionales Anidados
# Guerrero Aguilar Gullemro
# 24/03/25

''' Un condicional anidado consite en codificar condicionales dentro de otra condidión anteriormente 
    establecida '''

numero = int(input('Ingrese un número: '))

if numero > 0:
    if numero%2 == 0:
        print('El número es positivo par')
    else:
        print('El número es positivo impar.')
elif numero < 0:
    if numero%2 == 0:
        print('El número es negativo par')
    else:
        print('El número es negativo impar.')
else:
    print('El número es cero')
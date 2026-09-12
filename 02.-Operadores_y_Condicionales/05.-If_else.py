# If Else
# Guerrero Aguilar Gullemro
# 24/03/25

'''Las sentencias de control if - else sirven como condicionales, emulan lo que en el lenguaje cotidiano sería
    una acción y una consecuencia: si una condición se cumple, entonces pasa algo, sino, pasa otra cosa'''

numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese otro número: '))

if numero1 > numero2:                          # Establece una primera condicion
    print(numero1, ' es mayor que ', numero2)
elif numero1 < numero2:                         # Establece una condicion alterna a la primera
    print(numero1, 'es menor que ',numero2)
else:                                          # Establece lo que pasa cuando ninguna de las condiciones se cumplen
    print('Los números son iguales')
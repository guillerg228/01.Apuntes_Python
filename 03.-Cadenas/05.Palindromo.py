# Verificar si una palabra es un palíndromo
# Guerrero Aguilar Guillermo 
# 25/03/25

palabra = input('Ingrese una palabra para verificar si es paliíndromo:\n')

palabra = palabra.lower()
palabra_revez = palabra[::-1] #Se toma la palabra de inicio a fin de -1 en -1, lo que tiene un efecto de invertir la palabra

if palabra == palabra_revez:
    print(f'La palabra ingresada es un palíndromo: \n    {palabra} = {palabra_revez}')
else:
    print(f'La palabra ingresada NO es un palíndromo: \n    {palabra} != {palabra_revez}')
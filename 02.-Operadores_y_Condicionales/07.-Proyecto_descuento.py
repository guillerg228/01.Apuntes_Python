# Proyecto Descuento
# Guerrero Aguilar Gullemro
# 24/03/25

''' Solicitar al usuario que ingrese el monto de su consumo y a partir del mismo disernir 
el descuento que le corresponde: mayor a 50 y menor o igual a 100 se aplica un descuento de 10%,
mayor a 100 y menor o igual a 200 se aplica un descuento de 20%, mayor a 200 se aplica un desucuento
de 30%. Si el consumo es menor a 50 no se aplica ningún descuento'''

print("***** Calculo de descuentos *****")
consumo = float(input("Ingrese el consumo total: "))
descuento = 0.0
total = 0.0

if consumo<=50 and consumo>0:
    descuento = 0
elif consumo>50 and consumo<=100:
    descuento = consumo*0.10
elif consumo>100 and consumo<=200:
    descuento = consumo*0.20
elif consumo>200:
    descuento = consumo*0.30

total = consumo + descuento
print(f'El descuento aplicado es de: {descuento}')
print(f'El total a pagar es de: {total}')
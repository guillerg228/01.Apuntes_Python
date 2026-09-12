# Operadores Logicos
# Guerrero Aguilar Gullemro
# 24/03/25
''' Los operadores relacionales devuelven un valor booleano dependiendo de las entradas que se tengan. A
    continuacion se muestran la tablas de verdad de dichos operadores

    .    AND                  OR                 NOT
    |---|---|---|        |---|---|---|        |---|---|
    | A | B | Z |        | A | B | Z |        | A | Z |
    |---|---|---|        |---|---|---|        |---|---|
    | 0 | 0 | 0 |        | 0 | 0 | 0 |        | 1 | 0 |
    | 1 | 0 | 0 |        | 1 | 0 | 1 |        | 0 | 1 |
    | 0 | 1 | 0 |        | 0 | 1 | 1 |
    | 1 | 1 | 1 |        | 1 | 1 | 1 |
    '''
op_and = False and False
print('\nFalse and False = ', op_and)
op_and = True and False
print('True and False = ', op_and)
op_and = False and True
print('False and True = ', op_and)
op_and = True and True
print('True and True = ', op_and)

op_or = False or False
print('\nFalse or False = ', op_or)
op_or = True or False
print('True or False = ', op_or)
op_or = False or True
print('False or True = ', op_or)
op_or = True or True
print('True or True = ', op_or)

op_not = not True
print('\nnot True = ', op_not)
op_not = not False
print('not False = ', op_not)
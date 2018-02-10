print ('Calculadora Suma, Resta y Multiplicacion ')
numero_1 = int(input('Introduzca el numero 1 : '))
numero_2 = int(input('Introduzca el numero 2 : '))
operador = input('Quiere [S]umar, [R]estar, [M]ultiplicar o [D]ividir: ')
if operador == 'S':
   valor = numero_1 + numero_2
   simbolo = ' + '
elif operador == 'R':
   valor = numero_1 - numero_2
   simbolo = ' - '
elif operador == 'M':
   valor = numero_1 * numero_2
   simbolo = ' * '
else:
   valor = numero_1 / numero_2
   simbolo = ' / '
print (str(numero_1) + simbolo +  str(numero_2) + ' = ' + str(valor))

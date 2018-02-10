print ('Calculadora Suma y Resta')
numero_1 = int(input('Introduzca el numero 1 : '))
numero_2 = int(input('Introduzca el numero 2 : '))
operador = input('Quiere [S]umar o [R]estar : ')
if operador == 'S':
   valor = numero_1 + numero_2
   simbolo = ' + '
else:
   valor = numero_1 - numero_2
   simbolo = ' - '
print (str(numero_1) + simbolo +  str(numero_2) + ' = ' + str(valor))

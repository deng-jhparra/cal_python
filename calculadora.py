def suma (x,y):
   return x+y

def resta (x,y):
   return x-y

def multiplica (x,y):
   return x*y

def divide (x,y):
   try:
      return x/y
   except ZeroDivisionError:
      return 0


print ('Calculadora Suma, Resta y Multiplicacion ')
Error = False
numero_1 = int(input('Introduzca el numero 1 : '))
numero_2 = int(input('Introduzca el numero 2 : '))
operador = input('Quiere [S]umar, [R]estar, [M]ultiplicar o [D]ividir: ')

if operador == 'S':
   valor = suma (numero_1,numero_2)
   simbolo = ' + '
elif operador == 'R':
   valor = resta (numero_1,numero_2)
   simbolo = ' - '
elif operador == 'M':
   valor = multiplica (numero_1,numero_2)
   simbolo = ' * '
elif operador == 'D':
   valor = divide (numero_1,numero_2)
   Error = (1 - valor) == 1
   simbolo = ' / '
else:
   Error = True

if Error is False:
   print (str(numero_1) + simbolo +  str(numero_2) + ' = ' + str(valor))
else:
   print('Error al seleccinar el operador o hubo una division por cero')

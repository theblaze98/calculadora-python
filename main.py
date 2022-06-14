# Caculadora

operacion = input('Elige la operacion a realizar:\n'
                      + '1. Suma\n'
                      + '2. Resta\n'
                      + '3. Multiplicacion\n'
                      + '4. Division\n'
                      + '--> ')

if operacion == '':
    operacion = 0
else:
    operacion = int(operacion)

valor1 = input('Ingresa el Primer Valor --> ')
valor2 = input('Ingresa el Segundo Valor --> ')

if valor1 == '':
    valor1 = 0
else:
    valor1 = int(valor1)

if valor2 == '':
    valor2 = 0
else:
    valor2 = int(valor2)

# se encarga de la suma
def suma(valor1, valor2):
    print(f'El resultado de tu operracion es --> {valor1 + valor2}')

# se encarga de la resta
def resta(valor1, valor2):
    print(f'El resultado de tu operracion es --> {valor1 - valor2}')

# se encarga de la multiplicacion
def multiplicacion(valor1, valor2):
    print(f'El resultado de tu operracion es --> {valor1 * valor2}')

# se encarga de la division
def division(valor1, valor2):
    print(f'El resultado de tu operracion es --> {valor1 / valor2}')

if operacion==1:
    suma(valor1, valor2)
elif operacion==2:
    resta(valor1, valor2)
elif operacion==3:
    multiplicacion(valor1, valor2)
elif operacion==4:
    division(valor1, valor2)
elif operacion < 1 or operacion > 4:
    print(f'La opcion --> {operacion} no es valida')

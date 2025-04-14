# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = input("Ingrese un numero: ")
contador = 0

for i in range (len(num)):
    contador += 1

print (f'El numero de digitos es: {contador}')


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range(num+1, num2):
    suma += i

print(f'La suma total de los numeros comprendidos entre {num} y {num2} es de {suma}.')

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese un numero entero: "))
acumulador = 0

while num != 0:
    if acumulador != num:
        acumulador += num
    num = int(input("Ingrese un numero entero: "))
print (f'El total acumulado es de: {acumulador}')

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
aleatorio = random.randint(0,9)
flag = True
contador = 0

while flag == True:
    contador += 1 
    num = int(input("Por favor ingrese un numero entero entre 0 y 9: "))
    if 10 < num or num < -1:
        print(f'El numero ingresado {num} no es valido. Por favor ingresa entre 0 y 9')
    if num == aleatorio:
        print(f'Excelente! Acertaste! El numero secreto era {aleatorio}. Intentaste {contador} veces.')
        flag = False

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range (99,0,-1):
    if i%2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero: "))
suma = 0
for i in range (0,num):
    suma += i
print (f'La suma de todos los numeros entre 0 y {num} es de {suma}.')

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador_pares = 0
contador_impares= 0

for i in range(0,100):
    num = int(input("Ingrese un numero: "))
    if num%2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print (f'La cantidad de numeros pares es de: {contador_pares} y la cantidad de numeros impares es de: {contador_impares}.')

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0

for i in range(0,5):
    num = int(input("Ingrese un numero: "))
    contador += 1
    suma += num
media = suma / contador

print(f'La media es de {media}.')

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

n = int(input("Ingrese un numero para invertir: "))
num = 0
while n != 0:
    num = 10*num+n % 10
    n //= 10
print(f'{num}')
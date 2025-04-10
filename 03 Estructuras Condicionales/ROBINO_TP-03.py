# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga 
# “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
     print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo Negativo")
elif media == mediana == moda:
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

palabra = input("Ingrese una palabra o frase: ")
if palabra[-1] in ('a','e','i','o','u'):
    print(f'{palabra}!')
else:
    print(palabra)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 si quiere su nombre en mayusculas, 2 si quiere su nombre en minusculas o  3 si quiere su nombre con la primera letra en mayuscula: "))

if opcion == 1:
    print(f'{nombre.upper()}')
elif opcion == 2:
    print(f'{nombre.lower()}')
elif opcion == 3:
    print(f'{nombre.capitalize()}')
else:
    print("Ingrese un numero valido del 1 al 3!")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
#  Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 0:
    print("Ingrese un numero positivo")
elif magnitud <= 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio =  input("Ingrese su hemisferio con la letra N o S: ").upper()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el dia: "))
mes = mes.capitalize()


if mes in ('Enero', 'Febrero') or (mes == 'Diciembre' and dia >= 21) or (mes == 'Marzo' and dia <= 20):
        if (hemisferio == "N"):
            print("Te encontras en Invierno")
        elif (hemisferio == "S"):
            print("Te encontras en Verano")

elif mes in ('Abril', 'Mayo') or (mes == 'Marzo' and dia >= 21) or (mes == 'Junio' and dia <= 20):
        if (hemisferio == "N"):
            print("Te encontras en Primavera")
        elif (hemisferio == "S"):
            print("Te encontras en Otoño")

elif mes in ('Julio', 'Agosto') or (mes == 'Junio' and dia >= 21) or (mes == 'Septiembre' and dia <= 20):
        if (hemisferio == "N"):
            print("Te encontras en Verano")
        elif (hemisferio == "S"):
            print("Te encontras en Invierno")

elif mes in ('Octubre', 'Noviembre') or (mes == 'Septiembre' and dia >= 21) or (mes == 'Diciembre' and dia <= 20):
        if (hemisferio == "N"):
            print("Te encontras en Otoño")
        elif (hemisferio == "S"):
            print("Te encontras en Primavera")
else:
    print(f'No se encuentra el mes de {mes}')

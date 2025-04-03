# Ejercicio 1:

print("Hola Mundo!")

# Ejercicio 2:

nombre = input("Ingrese su nombre:")
print(f'Hola {nombre}!')

# Ejercicio 3:

nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')

# Ejercicio 4:

radio = int(input("Ingrese el radio del circulo a calcular: "))
area = 3.14 * radio
perimetro = 2 * 3.14 * radio

print(f'El calculo de area es de: {area}, y el calculo del perimetro es de: {perimetro}.')

# Ejercicio 5:

segundos = int(input("Ingrese la cantidad de segundos a calcular: "))
calculo_hora = segundos / 360

print(f'{segundos} son {calculo_hora} horas.')

# Ejercicio 6:

num = int(input("Ingrese un numero: "))
for i in range(1, 9):
    print(f'{num} x {i} = {num * i}')

# Ejercicio 7:

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print (f'La suma de los dos numeros ingresados es = {num1 + num2}, la division es: {num1 / num2}, la multiplicacion es {num1 * num2} y la resta es {num1 - num2}.')

# Ejercicio 8:

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print(f'Su indice de masa corporal es de: {imc}')

# Ejercicio 9:

temp = float(input("Ingrese la temperatura en grados ºC: "))
fahrenheit_temp = (temp * (9/5)) + 32

print(f'La temperatura en grados Fahrenheit es de: {fahrenheit_temp} ºF.')

# Ejercicio 10:

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f'El promedio de los tres numeros ingresados es de: {promedio}')
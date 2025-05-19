def imprimir_hola_Mundo():
    print("Hola Mundo")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

def calcular_area_circulo(radio):
    return 3.14 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1,10):
        print(f'{numero} x {i} = {i*numero}')

def operaciones_basicas(a,b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} x {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')

def calcular_imc(peso, altura):
    return peso / (altura**2)

def celsius_a_fahrenheit(c):
    return (c * (9/5) + 32)

def calcular_promedio(a,b,c):
    return (a+b+c) / 3


def main():
    opcion = int(input("Ingrese el numero de ejercicio: "))
    match opcion:
        case 1:
            imprimir_hola_Mundo()
        case 2:
            saludar_usuario(input("Ingrese su nombre: "))
        case 3:
            informacion_personal(
            input('Ingrese su nombre: '),
            input('Ingrese su apellido: '),
            input("Ingrese su edad: "),
            input("Ingrese su residencia: "))
        case 4:
            radio = float(input('Ingrese el radio del circulo: '))
            print(f'Area: {calcular_area_circulo(radio)}')
            print(f"Perímetro: {calcular_perimetro_circulo(radio)}")
        case 5:
            print(f"Horas: {segundos_a_horas(float(input('Ingrese los segundos: ')))}")
        case 6:
            tabla_multiplicar(int(input("Ingrese un numero entero para imprimir su tabla de multiplicar: ")))
        case 7:
            operaciones_basicas(float(input("Ingrese el primer numero: ")),
                                float(input("Ingrese el segundo numero: ")))
        case 8:
            imc = calcular_imc(float(input("Ingrese su peso en Kg: ")),
                        float(input("Ingrese su altura en Mts: ")))
            print(f'Su indice de masa corporal es de: {round(imc,2)}')
        case 9:
            temp_celcius = float(input("Ingrese la temperatura en grados Cº: "))
            print(f'La temperatura en grados Fahrenheit es de: {celsius_a_fahrenheit(temp_celcius)}ºF.')
        case 10:
            promedio = calcular_promedio(float(input("Ingrese el primer numero: ")),
                                        float(input("Ingrese el segundo numero: ")),
                                        float(input("Ingrese el tercer numero: ")))
            print(f'El promedio para los numeros ingresados es de: {round(promedio,2)}')
        case _:
            print("Opción no válida")



if __name__ == "__main__":
    main()




# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    return print("Hola Mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("¿Cómo te llamas? \n").strip()

if nombre_usuario:
    saludo_personalizado = saludar_usuario(nombre_usuario)
    print(saludo_personalizado)
else:
    print("No has introducido un nombre.")

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("Formulario de Información Personal")
print("---------------------------------")

nombre_usuario = input("Introduce tu nombre: ").strip()
apellido_usuario = input("Introduce tu apellido: ").strip()
edad_usuario = input("Introduce tu edad: ").strip() 
residencia_usuario = input("Introduce tu lugar de residencia (ciudad): ").strip()

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

PI = 3.14159

def calcular_area_circulo(radio):
    return PI * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * PI * radio

while True:
    try:
        radio_usuario = float(input("Introduce el radio del círculo: "))
        
        if radio_usuario < 0:
            print("Error: El radio no puede ser negativo. Inténtalo de nuevo.")
        else:
            break
            
    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número.")

area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

def segundos_a_horas(segundos):
    horas, segundos_restantes = divmod(segundos, 3600)
    minutos, segundos_finales = divmod(segundos_restantes, 60)
    return (horas, minutos, segundos_finales)

while True:
    try:
        segundos_input = int(input("Introduce la cantidad total de segundos: "))
        
        if segundos_input < 0:
            print("Por favor, introduce un número positivo.")
        else:
            break 
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")

h, m, s = segundos_a_horas(segundos_input)

print(f"Equivale a: {h} horas, {m} minutos y {s} segundos.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función

def tabla_multiplicar(numero):
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

while True:
    try:
        numero_usuario = int(input("Introduce un número para ver su tabla: "))
        break 
    except ValueError:
        print(" Entrada no válida. Por favor, introduce un número entero.")

tabla_multiplicar(numero_usuario)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = None
    else:
        division = a / b
    return (suma, resta, multiplicacion, division)

print("Calculadora de Operaciones Básicas")

while True:
    try:
        num1 = float(input("Introduce el primer número (a): "))
        break
    except ValueError:
        print("Entrada no válida. Introduce un número.")

while True:
    try:
        num2 = float(input("Introduce el segundo número (b): "))
        break
    except ValueError:
        print("Entrada no válida. Introduce un número.")

s, r, m, d = operaciones_basicas(num1, num2)

print(f"Suma (a + b): \t\t {s} \n"
    f"Resta (a - b): \t\t {r} \n"
    f"Multiplicación (a * b): \t {m}")

if d is None:
    print("División (a / b): \t Error (División por cero)")
else:
    print(f"División (a / b): \t {d:.2f}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice demasa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

print("Calculadora de Índice de Masa Corporal (IMC)")

while True:
    try:
        peso_usuario = float(input("Introduce tu peso: "))
        if peso_usuario > 0:
            break
        else:
            print("El peso debe ser un número positivo (mayor que cero).")
    except ValueError:
        print("Dato no válida.")

while True:
    try:
        altura_usuario = float(input("Introduce tu altura: "))
        if altura_usuario > 0:
            break 
        else:
            print("La altura debe ser un número positivo")
            
    except ValueError:
        print("Entrada no válida. Introduce un número")

imc_resultado = calcular_imc(peso_usuario, altura_usuario)

print(f"Con un peso de {peso_usuario} kg y una altura de {altura_usuario} m: \n"
    f"Tu Índice de Masa Corporal es: {imc_resultado:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print("Conversor de Celsius a Fahrenheit")

while True:
    try:
        celsius_usuario = float(input("Introduce la temperatura en grados Celsius: "))
        break 
    except ValueError:
        print("Dato no válida")

fahrenheit_resultado = celsius_a_fahrenheit(celsius_usuario)

print(f"{celsius_usuario}°C equivalen a {fahrenheit_resultado:.1f}°F")

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def obtener_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

print("Calculadora de Promedio de 3 Números")

num1 = obtener_numero("Introduce el primer número: ")
num2 = obtener_numero("Introduce el segundo número: ")
num3 = obtener_numero("Introduce el tercer número: ")

promedio_resultado = calcular_promedio(num1, num2, num3)

print(f"Los números ingresados son: {num1}, {num2}, y {num3}"
    f"El promedio es: {promedio_resultado:.2f}")


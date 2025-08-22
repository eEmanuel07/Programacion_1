"""1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”."""

print("Hola Mudo!")

"""2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."""

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

"""3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla."""

nom = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
l_resi = input("Ingrese el lugar en el que reside actualmente: ")

print(f"Soy {nom} {apellido}, tengo {edad} años y vivo en {l_resi}")

"""4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.""" 

radio = float(input("Ingrese el radio del circulo: "))
peri = 2 * 3.14 * radio
area = 3.14 * (radio ** 2)

print(f"El area del circulo es de {area} y su perimetro es {peri}.")

"""5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. """

seg = int(input("Ingrese la cantida de segundos que desea comvertir: "))
min = seg / 60
hora = min / 60

print(f"usted ingreso {int(seg)} segundos, que equivalen a {int(min)} minutos y que son {int(hora)} horas")

"""6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número."""

num = int(input("Ingrese un numero: "))
print("la tabla de multiplicar del numero ingresado es: ")
print(f"{num} x 1 = {num*1}")
print(f"{num} x 2 = {num*2}")
print(f"{num} x 3 = {num*3}")
print(f"{num} x 4 = {num*4}")
print(f"{num} x 5 = {num*5}")
print(f"{num} x 6 = {num*6}")
print(f"{num} x 7 = {num*7}")
print(f"{num} x 8 = {num*8}")
print(f"{num} x 9 = {num*9}")
print(f"{num} x 10 = {num*10}")

"""7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos"""

num1 = int(input("Ingrese un numero distinto a 0: ")) 
num2 = int(input("Ingrese otro numero distinto a 0: ")) 
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
division = num1 / num2

print(f"si sumamos los 2 numeros seria {suma}, si los restamos {resta}, si los multiplicamos {multi} y si los dividimos {division}")

"""8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal."""

altura = float(input("Ingrese su altura en metros (ej: 1.78): "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es de: {int(imc)}")

"""9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit."""

g_c = float(input("Ingrese la temperatura que desea comvertir a grados Fahrenheit: "))
g_f = g_c * 1.8 + 32

print(f"{g_c} grados Celsius equivalen a {g_f} grados Fahrenheit ")

"""10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números."""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3

print(f"El promediod de la suma de los 3 numeros es de {promedio}")
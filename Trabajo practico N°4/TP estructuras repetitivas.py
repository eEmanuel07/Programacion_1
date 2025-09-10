# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(0, 101, 1):
    print(i)
    i += 1

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

numero = int(input("Ingrese un número entero: "))
numero = abs(numero)
contador = 0

while numero > 0:
    numero = numero // 10
    contador += 1

print("Cantidad de dígitos:", contador)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
lista = list(range(num1, num2))
resul = 0

for num in range(num1 +1, num2, 1):
    resul = num + resul

print(resul)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

num1 = int(input("Ingrese un numero:"))
num = num1
num2 = 3

while num2 > 0:
    num2 = int(input("Ingrese un numero:"))
    num = num + num2
    i = num2
    print(f"{num-num2} + {num2} = {num}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

num = random.randint(0, 9)
i = False
contador = 0

while i == False:
    num_1 = int(input("Intente adivinar el numero: "))
    if num_1 != num:
        contador = contador + 1
    else:
        i = True

print(f"Bien hecho, lo encontraste en {contador} intento")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("ingrese un numero: "))
resul = 0

for i in range(0, num + 1, 1):
    resul = resul + i
    print (f"{i} + {resul - i} = {resul} ")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

contador = 2
cero = 0
con_par = 0
con_impar = 0
con_nega = 0
con_posi = 0

for i in range(0, contador, 1):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        con_par = con_par + 1
    else:
        con_impar = con_impar + 1
    
    if num > 0:
        con_posi = con_posi + 1
    elif num < 0:
        con_nega = con_nega + 1
    else:
        cero = cero + 1


print(f"Hay: \n{con_par} par \n{con_impar} inpar \n{con_posi} positivos \n{con_nega} negativos \n{cero} ceros.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

contador = 100
resul = 0

for i in range(0, contador, 1):
    num = int(input("Ingrese un numero: "))
    resul = resul + num
    media = resul / contador

print(f"la suma de los {contador} numeros es de {resul} y su media seria {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un numero: ")
rango = len(num)
cararcter = 0

for i in range(0, rango, 1):
    cararcter = cararcter - 1
    print( num[cararcter], end="" )


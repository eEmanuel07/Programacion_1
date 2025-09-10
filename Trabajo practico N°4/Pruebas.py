# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un numero: ")
rango = len(num)
cararcter = 0

for i in range(0, rango, 1):
    cararcter = cararcter - 1
    print( num[cararcter], end="" )
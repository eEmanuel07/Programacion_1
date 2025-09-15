#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

list_num = []

for i in range(1,101):
    if i % 4 == 0:
        list_num.append(i)

print(list_num)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

list_elem = [1, 2, 3, 4, 5]

print(list_elem[3])
print(list_elem[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
#ejemplo: 
#lista_vacia = []

list_vacia = []

for i in range(0, 3):
    list_vacia.append(input("Ingrese el elemento que desea agregar: "))

print(list_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"] 

animales [1] = "loro"
animales [-1] = "oso"

print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

#numeros = [8, 15, 3, 22, 7]
#numeros.remove(max(numeros))
#print(numeros)

# En la primera linea crea una lista (con los numeros 8, 15, 3, 22, 7), en la segunda linea remueve el numero maximo o mas grade de la lista y el la tercer linea imprime la lista de numeros (pero ahora sin el numero mas grande, que era el 22)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

list_num = []

for i in range(10,35,5):
    list_num.append(i)

print(list_num)

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

for i in range(0, 3):
    if i > 0 and i < 3:
        autos[i] = input("Ingrese el nuevo modelos de auto: ")

print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla. 

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
#a) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
#● Posición lista_anidada[0]: 15 
#● Posición lista_anidada[1]: True 
#● Posición lista_anidada[2][0]: 25.5 
#● Posición lista_anidada[2][1]: 57.9 
#● Posición lista_anidada[2][2]: 30.6 
#● Posición lista_anidada[3]: False 
#Imprimir la lista resultante por pantalla.

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada)









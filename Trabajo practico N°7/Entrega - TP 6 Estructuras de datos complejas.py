# 1. Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Pera = 2300
# ● Manzana = 1500 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Pera'] = 2300
precios_frutas['Manzana'] = 1500

print(precios_frutas)

# 2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

# 4. Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

contactos = {"Juan": "123456", "Ana": "987654"}

for i in range(1):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre que querés consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

# 5. Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# 6. Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7. Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

# 8. Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe
stock = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

producto = input("Ingrese el nombre del producto: ").lower()

if producto in stock:
    print(f"El stock de {producto} es {stock[producto]} unidades.")
    agregar = int(input("¿Cuántas unidades desea agregar? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"El producto '{producto}' no existe en el inventario.")
    opcion = input("¿Desea agregarlo? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("Ingrese la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")

print("\nInventario actualizado:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")

# 9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora}.")

# 10. Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario invertido:")
print(invertido)
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Periodo del año                            Estación en el                    Estación en el
#                                          hemisferio norte                   hemisferio sur

# Desde el 21 de diciembre                     Invierno                           Verano
# hasta el 20 de marzo (incluidos)

# Desde el 21 de marzo                         Primavera                           Otoño
# hasta el 20 de junio (incluidos)

# Desde el 21 de junio                         Verano                             Invierno
# hasta el 20 de septiembre (incluidos)

# Desde el 21 de septiembre                    Otoño                              Primavera
# hasta el 20 de diciembre (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = int(
#     input(
#         "1. hemisferio norte \n2. hemisferio sur \n\nSegun corresponda coloque el numero de hemisferio (1 o 2): "
#     )
# )

# if hemisferio != 1 and hemisferio != 2:
#     print(
#         "\nEl numero ingresado no corresponde a ninguna opción. Reinicie el programa."
#     )
#     exit()
# else:
#     mes = int(
#         input(
#             "1. Enero\n2. Febrero\n3. Marzo\n4. Abril\n5. Mayo\n6. Junio\n7. Julio\n8. Agosto\n9. Septiembre\n10. Octubre\n11. Novienbre\n12. Diciembre\n\nIngrese el numero que le corresponda según el mes: "
#         )
#     )

# if mes <= 0 or mes >= 13:
#     print(
#         "\nEl numero ingresado no corresponde a ninguna opción. Reinicie el programa."
#     )
#     exit()
# else:
#     dia = int(input("\nIngrese el numero correspondiente al dia: "))

# if mes == 2 and (dia < 1 or dia > 28):
#     print("\nEl numero del dia no corresponde al mes. Reinicie el programa.1")
#     exit()
# elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30):
#     print("\nEl numero del dia no corresponde al mes. Reinicie el programa.2")
#     exit()
# elif dia < 1 or dia > 31:
#     print("\nEl numero del dia no corresponde al mes. Reinicie el programa.3")
#     exit()
# else:
#     if (
#         (hemisferio == 1)
#         and (mes == 12 or mes == 1 or mes == 2 or mes == 3)
#         and (mes == 12 and dia >= 21)
#         and (mes == 3 and dia <= 20)
#     ):
#         print("segun la fecha en el hemisferio norte es Invierno")
#     elif (
#         (hemisferio == 1)
#         and (mes == 3 or mes == 4 or mes == 5 or mes == 6)
#         and (mes == 3 and dia >= 21)
#         and (mes == 6 and dia <= 20)
#     ):
#         print("segun la fecha en el hemisferio norte es Primavera")
#     elif (
#         (hemisferio == 1)
#         and (mes == 6 or mes == 7 or mes == 8 or mes == 9)
#         and (mes == 6 and dia >= 21)
#         and (mes == 9 and dia <= 20)
#     ):
#         print("segun la fecha en el hemisferio norte es Verano")
#     elif (
#         (hemisferio == 1)
#         and (mes == 9 or mes == 10 or mes == 11 or mes == 12)
#         and (mes == 9 and dia >= 21)
#         and (mes == 12 and dia <= 20)
#     ):
#         print("segun la fecha en el hemisferio norte es Otoño")
#     else:
#         print("hay un error")




print("\nPrimero necesisamos una fecha para saber en que estacion estamos: ")

anio = int(input("\nIngrese el año de la fecha: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiesto = 1
else:
        bisiesto = 0

mes = int(input("\n1. Enero\n2. Febrero\n3. Marzo\n4. Abril\n5. Mayo\n6. Junio\n7. Julio\n8. Agosto\n9. Septiembre\n10. Octubre\n11. Novienbre\n12. Diciembre\n\nIngrese el numero que le corresponda según el mes: "))

if mes < 0 or mes > 12:
    print("Los años solo tiene 12 meses")
    exit()

dia = int(input("\nIngrese el numero correspondiente al dia: "))

if mes == 2:
    if (bisiesto == 1) and (dia < 0 or dia > 29):
        print("Febrero en los años bisiestos solo tienen 29 dias")
    elif (bisiesto == 0) and (dia < 0 or dia > 28):
        print("Febrero en los años comunes solo tienen 28 dias")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 0 or dia > 30):
    print("El mes ingresado solo tiene 30 dias")
elif dia < 0 or dia > 31:
    print("El mes ingresado solo tiene 31 dias")

hemisferio = int(input("\n1. hemisferio norte \n2. hemisferio sur \n\nSegun corresponda coloque el numero de hemisferio (1 o 2): "))

if not(hemisferio == 1 or hemisferio == 2):
    print("\nEl numero ingresado no pertenece a una opcion. Reinicie el programa.")

if (mes == 12 or mes == 1 or mes == 2 or mes == 3) or (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20):
    if hemisferio == 1:
        estacion = ("Invierno")
    elif hemisferio == 2:
        estacion = ("Verano")
if (mes == 3 or mes == 4 or mes == 5 or mes == 6) or (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20):
    if hemisferio == 1:
        estacion = ("Primavera")
    elif hemisferio == 2:
        estacion = ("Otoño")
if (mes == 6 or mes == 7 or mes == 8 or mes == 9) or (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20):
    if hemisferio == 1:
        estacion = ("Verano")
    elif hemisferio == 2:
        estacion = ("Invierno")
if (mes == 9 or mes == 10 or mes == 11 or mes == 12) or (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20):
    if hemisferio == 1:
        estacion = ("Otoño")
    elif hemisferio == 2:
        estacion = ("Primavera")

print(f" \nSegun la fecha ({dia}/{mes}/{anio}) y el emisferio que eligio estamos en {estacion} \n")



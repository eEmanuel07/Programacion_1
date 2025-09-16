#Caso 1 – Biblioteca escolar – Préstamos de libros
#Enunciado / Descripción
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que utilice listas paralelas (una para títulos[] y otra para ejemplares[]). Cada título debe estar vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario elija salir.

menu = ("\n1.	Ingresar lista de títulos\n\n2.	Ingresar lista de ejemplares disponibles (por título)\n\n3.	Mostrar catálogo con stock\n\n4.	Consultar disponibilidad de un título específico\n\n5.	Listar agotados (0 ejemplares)\n\n6.	Agregar título\n\n7.	Ver títulos agotados\n\n8.	Actualizar ejemplares (préstamo/devolución)\n\n9.	Ver catálogo\n\n10.	Salir")

print(menu)
op = int(input("\nElija alguna opcion: "))

while op != 10:
    if op >= 11 or op <= 0:
        print(f"\nel numero {op} no es uma opcion disponible en el menu")
        print(menu)
        op = int(input("\nElija alguna opcion: "))
    else:
        break



titulo = []
cantidad =[]
blb = [titulo, cantidad]
libros_a = 0

while op != 10:

    if op == 1:
        cant_libros = int(input("\nCual es la cantida de libros que quiere agregar?\n"))
        
        for i in range(cant_libros):
            titulo.append(input("\nIngrese el titulo del libro: ").lower())
            cantidad.append(int(input("\nIngrese la cantidad de ejemplares: ")))
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 2:
        for i in range(len(titulo)):
            print(f"{i+1}.  {titulo[i]}")
        num_l = int(input("Ingrese el numero correspondiente al libro: "))
        if num_l <= len(titulo) and num_l >= 1:
            if cantidad[i] > 1:
                print(f"La biblioteca tiene disponible en este momento {cantidad[i]} ejemplares")
                pass
            else:
                print(f"La biblioteca tiene disponible en este momento {cantidad[i]} ejemplar")
                pass
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 3:
        print("\nLos ejemplares disponibles son: \n")
        for i in range(len(titulo)):
            if cantidad[i] > 1:
                print(f"{i+1}.  {blb[0][i]}, la biblioteca tiene disponible en este momento {blb[1][i]} ejemplares\n")
                pass
            else:
                print(f"{i+1}.  {blb[0][i]}, la biblioteca tiene disponible en este momento {blb[1][i]} ejemplare\n")
                pass
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 4:
        libro_b = input("\nQue libro esta buscando? ").lower()
        for i in range(len(titulo)):
            if libro_b == titulo[i]:
                validacion = True
        if validacion == True:
            print(f"\nEse libro si lo tiene la biblioteca, nos quedan disponibles {cantidad[i]}.")
        elif validacion == False:
            print("\nLo sentimos, todavia no tenemos ese libro.")
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 5:
        for i in range(len(cantidad)):
            if cantidad[i] == 0:
                libros_a += 1
        if libros_a == len(cantidad):
            print(f"\nPor el momento todos los ejemplares tiene por lo menos 1 copia disponible.")
            pass
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 6:
        titulo.append(input("\nIngrese el titulo del libro: ").lower())
        cantidad.append(int(input("\nIngrese la cantidad de ejemplares: ")))
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 7:
        for i in range(len(cantidad)):
            if cantidad[i] == 0:
                libros_a += 1
        if libros_a == len(cantidad):
            print(f"\nPor el momento todos los ejemplares tiene por lo menos 1 copia disponible.")
            pass
        else:
            print("\nLos libros agotados son: \n")
            for i in range(len(cantidad)):
                if cantidad[i] == 0:
                    print(f" {i+1}. {titulo[i]}\n")
        pass
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 8:
        for i in range(len(titulo)):
            print(f"{i+1}.  {titulo[i]}")
        num_l = int(input("\nIngrese el numero correspondiente al libro: \n"))
        if num_l <= len(titulo) and num_l >= 1:
            act_p_o_d = int(input("segun corresponda\n 1. Prestamo\n 2. Devolucion\nElija la actualizacion que desea hacer: \n"))
            if act_p_o_d == 1:
                pres = int(input("Cuantos libros se prestaron? \n"))
                cantidad[num_l-1] -= pres
                if cantidad[num_l - 1] <= 0:
                    print("No contamos con tantas copias.")
            elif act_p_o_d == 2:
                devol = int(input("Cuantos libros se devolvieron? \n"))
                cantidad[num_l-1] += devol
            else:
                print("La opcion ingresada no es valida.")
        print(menu)
        op = int(input("\nElija alguna opcion: "))
        
    elif op == 9:
        print("\nLos ejemplares disponibles son: \n")
        for i in range(len(titulo)):
            if cantidad[i] > 1:
                print(f"{i+1}.  {blb[0][i]} la biblioteca tiene disponible en este momento {blb[1][i]} ejemplares\n")
            else:
                print(f"{i+1}.  {blb[0][i]} la biblioteca tiene disponible en este momento {blb[1][i]} ejemplare\n")
        print(menu)
        op = int(input("\nElija alguna opcion: "))












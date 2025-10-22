def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("Formulario de Información Personal")
print("---------------------------------")

nombre_usuario = input("Introduce tu nombre: ").strip()
apellido_usuario = input("Introduce tu apellido: ").strip()
edad_usuario = input("Introduce tu edad: ").strip() 
residencia_usuario = input("Introduce tu lugar de residencia (ciudad): ").strip()

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
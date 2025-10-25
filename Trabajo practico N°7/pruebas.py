# Agenda inicial
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Gimnasio"
}

# Consultar evento
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay actividades programadas para {dia} a las {hora}.")
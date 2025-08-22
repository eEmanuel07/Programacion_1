"""
Un restaurante quiere ayudar a sus clientes a calcular cuánto dejar de propina según el 
monto de la cuenta. 
El programa debe: 
✓ Pedir al usuario el monto total de la cuenta. 
✓ Calcular la propina sugerida al 10%. 
✓ Calcular la propina sugerida al 15%. 
✓ Calcular el total a pagar en ambos casos (cuenta + propina). 
✓ Mostrar todos los resultados en pantalla.
"""

monto_total = int(input("Ingrese el monto total de la cuenta: "))

propina_10 = monto_total * 0.10
propina_15 = monto_total * 0.15

total_10 = monto_total + propina_10
total_15 = monto_total + propina_15

print(f"El monnto total es de {monto_total}, el 10% de la propina es {propina_10}, y el 15% de la propina es {propina_15}. Los montos sugeridos a pagar son: {total_10} con el 10% de propina y {total_15} con el 15% de propina.")


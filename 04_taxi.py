distancia = float(input("Ingresa la distancia recorrida en km: "))
hora = int(input("Ingresa la hora del viaje (0 - 23): "))


tarifa_base = 1.0


if 6 <= hora <= 19:
    tipo_horario = "diurno"
    costo_km = 0.50
elif (20 <= hora <= 23) or (0 <= hora <= 5):
    tipo_horario = "nocturno"
    costo_km = 0.65
else:
    print("Hora inválida")
    

total = tarifa_base + (distancia * costo_km)

if distancia > 10:
    total += 2

print("\nHorario:", tipo_horario)
print("Distancia:", distancia, "km")
print("Total a pagar: $", round(total, 2))
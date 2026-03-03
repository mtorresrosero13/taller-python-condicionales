n1 = float(input("Ingresa la nota 1: "))
n2 = float(input("Ingresa la nota 2: "))
n3 = float(input("Ingresa la nota 3: "))

if (n1 < 0 or n1 > 100) or (n2 < 0 or n2 > 100) or (n3 < 0 or n3 > 100):
    print("Error: nota inválida")
    exit() #este exit le pedi ayuda a IA porque no me funcionaba.

promedio = (n1 + n2 + n3) / 3

if 90 <= promedio <= 100:
    clasificacion = "Excelente"
elif 80 <= promedio < 90:
    clasificacion = "Muy bueno"
elif 70 <= promedio < 80:
    clasificacion = "Bueno"
elif 60 <= promedio < 70:
    clasificacion = "Supletorio"
else:
    clasificacion = "Reprobado"

print("\nNotas ingresadas:")
print("Nota 1:", n1)
print("Nota 2:", n2)
print("Nota 3:", n3)
print("Promedio:", promedio)
print("Clasificación final:", clasificacion)
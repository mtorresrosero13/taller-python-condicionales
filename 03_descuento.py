subtotal = float(input("Subotal: "))
cliente = input("Que tipo de cliente eres?: ")
descuento = 0
if cliente == "vip":
    descuento = subtotal*0.15
else:
    descuento

total = subtotal - descuento

print("RESUMEN")
print(f"Subtotal:{subtotal} ")
print(f"Descuento aplicado {descuento}")
print(f"total final: {total}")
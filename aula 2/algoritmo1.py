from os import system
from math import pi

system("cls||clear")
r = float(input("Raio: "))
area = f"{pi*r**2:.90g}"
print(f"Área: {area}")
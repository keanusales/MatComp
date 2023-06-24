from os import system

system("cls||clear")
x = float(input("Valor x: "))
com = 0
for i in range(30000):
  com += x
print(f"Resultado: {com:.90g}")
from os import system
from math import inf

def erros(n: int, x: float):
  prox = 10000
  for i in range(n):
    prox -= x
  real = 10000 - x*n
  abst = abs(real - prox)
  try: relt = abst/real
  except ZeroDivisionError:
    relt = -inf
  return abst, relt

system("cls||clear")
n = int(input("Digite o número n: "))
x = float(input("Digite o número x: "))

abst, relt = erros(n, x)

print(f"Erro absoluto: {abst}")
print(f"Erro relativo: {relt}")
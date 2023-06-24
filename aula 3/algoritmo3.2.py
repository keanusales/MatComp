from os import system
from math import inf

def e(x: float):

  def aux(x: float):
    sum, ant, k = 1, 1, 1
    while ant not in [0, inf]:
      ant *= x/k; k += 1
      sum += ant
    print(f"Iterações: {k-1}")
    return sum

  if x == 0: return 1
  if x > 0: return aux(x)
  return 1/aux(-x)

system("cls||clear")
x = float(input("Valor x: "))
print(f"e^{x}: {e(x):.90g}")
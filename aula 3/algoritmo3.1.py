from os import system

def e(x: float, n: int):

  def aux(x: float):
    sum, ant, k = 1, 1, 1
    while k != n:
      ant *= x/k; k += 1
      sum += ant
    print(f"Iterações: {k-1}")
    return sum

  if x == 0: return 1
  if x > 0: return aux(x)
  return 1/aux(-x), aux(x)

system("cls||clear")
n = int(input("Valor n: "))
x = float(input("Valor x: "))
print(f"e^{x}: {e(x, n)}")
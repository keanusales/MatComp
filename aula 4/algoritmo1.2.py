from os import system
from tabulate import tabulate
# from math import log10
# from math import e

def f(x: int): return x**3 - 9*x + 3
# def f(x: int): return x**.5 - 5*e**(-x)
# def f(x: int): return x*log10(x) - 1

def func(a: int, b: int):
  res = [[x, "-" if y < 0 else "+", y] for x, y in [(x, f(x)) for x in range(a, b, 1)]]
  res = [(e1, e2) for e1, e2 in zip(res[:-1], res[1:]) if e1[1] != e2[1]]
  return [e for elem in res for e in elem], [(e1[0], e2[0]) for e1, e2 in res]

def bissec(lista: list, e = 0):
  def aux(a: int, b: int):
    ai, bi = a, b
    while abs(bi - ai) > e:
      pi = (ai + bi)/2
      if f(ai) * f(bi) < 0: bi = pi
      else: ai = pi
    return pi
  res = [aux(a, b) for a, b in lista]
  return [(x, f(x)) for x in res]

def intput(prompt: str, evalue: int):
  print("Valor-padrão: digite algo que não é número")
  try: return int(input(prompt))
  except ValueError: return evalue

system("cls||clear")
a = intput("Digite o 1º número do intervalo: ", -100)
b = intput("Digite o 2º número do intervalo: ", 100)
res1, res2 = func(a, b)
print("\nA lista correspondente é:")
print("\n" + tabulate(res1, ("x", "+/-", "f(x)"), "rst"))
res2 = bissec(res2)
print("\n" + tabulate(res2, ("raíz (x)", "f(x)"), "rst"))
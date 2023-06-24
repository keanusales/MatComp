from os import system
from tabulate import tabulate
# from math import log10
# from math import e

def f(x: int): return x**3 - 9*x + 3

def func(a: int, b: int):
  res = [[x, "-" if y < 0 else "+"] for x, y in [(x, f(x)) for x in range(a, b, 1)]]
  return [e for e1, e2 in zip(res[:-1], res[1:]) if e1[1] != e2[1] for e in (e1, e2)]

def intput(prompt: str, evalue: int):
  print("Valor-padrão: digite algo que não é número")
  try: return int(input(prompt))
  except ValueError: return evalue

system("cls||clear")
a = intput("Digite o 1º número do intervalo: ", -100)
b = intput("Digite o 2º número do intervalo: ", 100)
print("\nA lista correspondente é:")
print(tabulate(func(a, b), ("x", "+/-", "f(x)"), "rst"))
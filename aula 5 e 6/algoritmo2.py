from os import system
from tabulate import tabulate
from math import sin, cos, tanh, log, e

def f(x: float): return 2*log(x)*(x**(log(x)-1)) - (x**3)*cos(x) - 3*(x**2)*sin(x) + 2*x

# def f(x: float):
#   acima = 2*(2*(log(x)**2)*x**log(x) - log(x)*x**log(x) + x**log(x) + x**2)
#   return x*(x**2 - 6)*sin(x) - 6*x**2*cos(x) + (acima/x**2)

def func(a: int, b: int):
  res = [[x, "-" if y < 0 else "+", y] for x, y in [(x, f(x)) for x in range(a, b, 1)]]
  res = [(e1, e2) for e1, e2 in zip(res[:-1], res[1:]) if e1[1] != e2[1]]
  return [e for elem in res for e in elem], [(e1[0], e2[0]) for e1, e2 in res]

def bissec(lista: list):
  def aux(a: int, b: int):
    fa, fb, i = f(a), f(b), 0
    while True:
      x = a + (b - a)/2
      fx = f(x)
      if fx == fa or fx == fb: break
      if fa * fx > 0: a, fa = x, fx
      else: b, fb = x, fx
      i += 1
    print(f"Iterações: {i}")
    return x
  res = [aux(a, b) for a, b in lista]
  return [(x, f(x)) for x in res]

def posfal(lista: list):
  def aux(a: int, b: int):
    fa, fb, i = f(a), f(b), 0
    while True:
      x = (a*fb - b*fa)/(fb - fa)
      fx = f(x)
      if fx == fa or fx == fb: break
      if fa * fx > 0: a, fa = x, fx
      else: b, fb = x, fx
      i += 1
    print(f"Iterações: {i}")
    return x
  res = [aux(a, b) for a, b in lista]
  return [(x, f(x)) for x in res]

def secante(lista: list):
  def aux(a: float, b: float):
    fa, fb, i = f(a), f(b), 0
    while True:
      try: x = b - ((fb*(b-a))/(fb-fa))
      except ZeroDivisionError: break
      a, b, fa, fb = b, x, fb, f(x)
      i += 1
    print(f"Iterações: {i}")
    return b
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
print("A lista correspondente é:")
print(tabulate(res1, ("x", "+/-", "f(x)"), "rst"))

temp = bissec(res2)
print("\nBissecção:")
print(tabulate(temp, ("raíz (x)", "f(x)"), "rst"))

temp = posfal(res2)
print("\nPosição Falsa:")
print(tabulate(temp, ("raíz (x)", "f(x)"), "rst"))

temp = secante(res2)
print("\nSecante:")
print(tabulate(temp, ("raíz (x)", "f(x)"), "rst"))
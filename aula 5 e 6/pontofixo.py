from typing import Callable
from os import system

def fpoint(f: Callable, fi: Callable, x0: float, e1 = 1e-6, e2 = 1e-6):
  if abs(f(x0)) < e1: return x0
  x, k = fi(x0), 0
  while abs(f(x)) > e1 and abs(x - x0) > e2:
    x0 = x; x = fi(x); k += 1
  return x, f(x), k

print(fpoint(lambda x: x**2+x-6, lambda x: (6 - x)**1/2, 1.5))
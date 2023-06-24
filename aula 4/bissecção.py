def bissecção(f: float, a: int, b: int, e = 1e-10):
  i, ai, bi = 0, a, b
  while abs(ai + bi) > e:
    pi = (ai + bi)/2
    if f(ai) * f(bi) < 0: bi = pi
    else: ai = pi
    i += 1
  return (ai + bi)/2
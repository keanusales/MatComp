from numpy.random import randint
from numpy import ndarray, eye, zeros, arange, array
from scipy.linalg import solve
import matplotlib.pyplot as plt
from statistics import mean
from time import time

def gerarSistema(ordem: int):
  A = randint(20, 100, (ordem, ordem)).astype(float)
  b = randint(2000, 10000, (ordem)).astype(float)
  A.flat[::ordem+1] *= randint(10, 20) * ordem
  return A, b, solve(A, b)

def escalonamento(A: ndarray, b: ndarray):
  n = A.shape[0]
  iterações = 0

  for i in arange(n):
    pivo = A[i, i]
    if pivo == 0: return 0
    for j in arange(i+1, n):
      m = A[j, i] / pivo
      A[j] -= m * A[i]
      b[j] -= m * b[i]
      iterações += 1

  x = zeros((n))

  for i in arange(n-1, -1, -1):
    x[i] = (b[i] - sum(A[i] * x)) / A[i, i]
    iterações += 1

  return x, iterações

def fatoraçãoLU(A: ndarray, b: ndarray):
  n = A.shape[0]
  L, U = eye(n), A.copy()
  iterações = 0

  for j in arange(n-1):
    pivo = U[j, j]
    if pivo == 0: return 0
    for i in arange(j+1, n):
      L[i, j] = U[i, j] / pivo
      U[i] -= L[i, j] * U[j]
      iterações += 1

  x, y = zeros(n), zeros(n)

  for i in arange(n):
    y[i] = b[i] - sum(L[i] * y)
    iterações += 1

  for i in arange(n-1, -1, -1):
    x[i] = (y[i] - sum(U[i] * x)) / U[i, i]
    iterações += 1

  return x, iterações

def gauss_jacobi(A: ndarray, b: ndarray, e = 1e-15):
  n = A.shape[0]
  iterações = 0
  
  copy = A.copy()
  copy.flat[::n+1] = 0
  alpha = max(sum(abs(copy) / abs(A.diagonal())))
  if alpha > 1: return 0

  C = zeros((n, n))
  G = zeros((n))
  x = randint(1, 10, (n)).astype(float)

  for i in arange(n):
    C[i] = -A[i] / A[i, i]
    iterações += 1

  for i in arange(n):
    G[i] = b[i] / A[i, i]
    C[i, i] = 0
    iterações += 1

  while True:
    x_ant = x.copy()
    x = C @ x_ant + G
    iterações += n
    if max(abs(x - x_ant)) < e: break

  return x, iterações

def gauss_seidel(A: ndarray, b: ndarray, e = 1e-15):
  n = A.shape[0]
  iterações = 0
  
  copy = A.copy()
  copy.flat[::n+1] = 0
  alpha = max(sum(abs(copy) / abs(A.diagonal())))
  if alpha > 1: return 0

  C = zeros((n, n))
  G = zeros((n))
  x = randint(1, 10, (n)).astype(float)

  for i in arange(n):
    C[i] = -A[i] / A[i, i]
    iterações += 1

  for i in arange(n):
    G[i] = b[i] / A[i, i]
    C[i, i] = 0
    iterações += 1

  while True:
    x_ant = x.copy()
    for i in arange(n):
      x[i] = C[i] @ x + G[i]
      iterações += 1
    if max(abs(x - x_ant)) < e: break

  return x, iterações

métodos = ["Escalonamento", "Fatoração LU", "Gauss-Jacobi", "Gauss-Seidel"]

def plotgfx(tamanho: ndarray, tempos: ndarray, iters: ndarray):
  fig, axes = plt.subplots(ncols = 2, figsize = (12, 6))
  fig.tight_layout(pad = 1)

  for i, elem in enumerate(tempos):
    axes[0].plot(tamanho, elem, label = métodos[i], lw = .5)
  axes[0].set_title("Relação entre Ordem e Tempo")
  axes[0].set_xlabel("Ordem do Sistema Linear")
  axes[0].set_ylabel("Tempo de execução (segundos)")
  axes[0].legend(loc = 2)

  for i, elem in enumerate(iters):
    axes[1].plot(tamanho, elem, label = métodos[i], lw = .5)
  axes[1].set_title("Relação entre Iterações e Tempo")
  axes[1].set_xlabel("Ordem do Sistema Linear")
  axes[1].set_ylabel("Iterações realizadas")
  axes[1].legend(loc = 2)

  return fig

tamanho = arange(1, 46) * 100
tempos, iters = [], []

for i, ordem in enumerate(tamanho):
  A, b, resp = gerarSistema(ordem)
  c1 = time()
  f1, i1 = escalonamento(A, b)
  c2 = time()
  f2, i2 = fatoraçãoLU(A, b)
  c3 = time()
  f3, i3 = gauss_jacobi(A, b)
  c4 = time()
  f4, i4 = gauss_seidel(A, b)
  c5 = time()
  tempos.append((c2-c1, c3-c2, c4-c3, c5-c4))
  iters.append((i1, i2, i3, i4))
  m1 = mean(abs(resp - f1))
  m2 = mean(abs(resp - f2))
  m3 = mean(abs(resp - f3))
  m4 = mean(abs(resp - f4))
  print(f"Iteração {i+1}: {m1}, {m2}, {m3}, {m4}")

tempos = array(tempos).T
iters = array(iters).T
plotgfx(tamanho, tempos, iters).show()
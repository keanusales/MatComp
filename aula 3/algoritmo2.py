from os import system

def pre(a: int, s = 2):
  while s > 1:
    a /= 2
    s = 1 + a
  return 2*a

system("cls||clear")
a = int(input("Valor de a: "))

print(f"Precisão: {pre(a)}")
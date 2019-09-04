import numpy
import matplotlib.pyplot as plt
import random

def gen(p, f):
  def func():
    acumulado = 0
    for i in range(len(f)):
      acumulado += p[i] + f[i]()
    return acumulado
  return func

def main(iterations, p, f):
  f = gen(p, f)
  p = []
  for x in range(iterations):
    p.append(f())
  #plt.plot(p)
  plt.hist(x = p, bins = 50)
  plt.show()

if __name__ == "__main__":
  main(100000, [1], [random.random])
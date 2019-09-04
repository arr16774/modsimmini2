import numpy as np
import matplotlib.pyplot as plt
import random

def gen(p, f):
  def func():
    acumulado = 0
    for i in range(len(f)):
      acumulado += p[i] + f[i]()
    return acumulado
  return func

def normalapply():
  return normal(-600, 50)

def normal(mu, sigma):
    while True:
        y1 = np.log(1 - random.random())/-1
        y2 = np.log(1 - random.random())/-1
        if (y2 - (y1-1) ** 2) /2 > 0:
            y1 = y2 - ((y1-1) ** 2) / 2
            rand = random.random()
            if rand < 0.5:
                return mu + sigma * y1
            else:
                return mu - sigma * y1

def main(iterations, p, f):
  f = gen(p, f)
  p = []
  for x in range(iterations):
    p.append(f())
  #plt.plot(p)
  plt.hist(x = p, bins = 50)
  plt.show()

if __name__ == "__main__":
  main(100000, [0.5, 0.5], [random.random, normalapply])
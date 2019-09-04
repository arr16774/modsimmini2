import random
import matplotlib.pyplot as plt


def escogerclientes():
    rand = random.random()
    if rand <= 0.3:
        periodicos = 9
    elif rand > 0.3 and rand <= 0.7:
        periodicos = 10
    else:
        periodicos= 11
    return periodicos


def simulardia(x, iter):
    total = 0
    for i in range(1, iter):
        clientes = escogerclientes()
        devol = (x - clientes) * 0.5
        ganancia = clientes * 2.5
        perdida = x * 1.5
        total = total + ganancia - perdida + devol
    return total


def main():
    total30 = []
    for i in range(9,12):
        j = 0
        valor = simulardia(i, 30)
        total30.append(valor)
        print("Ganancias de 1 mes:", i, total30[j])
        j += 1
    total364 = []
    for k in range(9, 12):
        j = 0
        valor = simulardia(k, 360)
        total364.append(valor)
        print("Ganancias de 1 anio:",k, total364[j])
        j += 1
    total3640 = []
    for n in range(9, 12):
        j = 0
        print(n)
        valor = simulardia(n, 3640)
        total3640.append(valor)
        print("Ganancias de 1 anio:", n, total3640[j])
        j += 1


if __name__ == '__main__':
    main()
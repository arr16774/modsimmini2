import random
import numpy as np
import matplotlib.pyplot as plt


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


def uniforme(x, y):
    rango = x - y
    choice = random.uniform(0, 1)
    return y + rango*choice


def valorpresenteneto(x, maximo, minimo, vueltas, inicial, porcentaje):
    vpn = 0
    for j in range(1, vueltas):
        total = []
        for i in range(1, len(x)):
            valor = normal(x[i][0], x[i][1])
            total.append(valor)
        valor2 = uniforme(maximo, minimo)
        total.append(valor2)
        vpn += -inicial + sum(flujo/(1+porcentaje) ** (k+1) for k, flujo in enumerate(total))
    return vpn/vueltas

def main():
    comercial = [(-600, 50), (-200, 50), (-600, 100), (250, 150), (350, 150), (400, 150)]
    inicio = 900
    tope1 = 6000
    suelo1 = 1600
    hotel = [(-800, 50), (-800, 100), (-700, 150), (300, 200), (400, 200), (500, 200)]
    inicio2 = 800
    tope2 = 8440
    suelo2 = 200

    valorcomercial = valorpresenteneto(comercial, tope1, suelo1, 100, inicio, 0.1)
    valorcomercial1 = valorpresenteneto(comercial, tope1, suelo1, 100, inicio, 0.1)
    valorcomercial2 = valorpresenteneto(comercial, tope1, suelo1, 100, inicio, 0.1)
    valorhotel = valorpresenteneto(hotel, tope2, suelo2, 100, inicio2, 0.1)
    valorhotel1 = valorpresenteneto(hotel, tope2, suelo2, 1000, inicio2, 0.1)
    valorhotel2 = valorpresenteneto(hotel, tope2, suelo2, 10000, inicio2, 0.1)

    valores = [valorcomercial, valorhotel, valorcomercial1, valorhotel1, valorcomercial2, valorhotel2]

    x = [1, 2, 3, 4, 5, 6]

    plt.bar(x, valores)
    plt.show()

if __name__ == '__main__':
    main()

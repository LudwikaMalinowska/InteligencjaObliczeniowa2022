import math
import random

v1 = [3, 8, 9, 10, 12]
v2 = [8, 7, 7, 5, 6]


def vector_sum(v1, v2):
    v3 = []
    for i in range(v1.length):
        v3.append(v1[i] + v2[i])

    return v3


def vector_multiply(v1, v2):
    v3 = []
    for i in range(v1.length):
        v3.append(v1[i] * v2[i])

    return v3


def vector_iloczyn_skalarny(v1, v2):
    iloczyn = 0
    for i in range(v1.length):
        iloczyn += v1[i] * v2[i]

    return iloczyn


def dlugosc_euklidesowa(v):
    suma_kwadratow = 0
    for i in range(v.length):
        suma_kwadratow += v[i] ** 2

    dlugosc = math.sqrt(suma_kwadratow)
    return dlugosc

def random_50():
    v = []
    random.seed(50)
    for i in range(50):
        v.append(random.randint(1, 100))

    return v


def vector_stats(v):
    v_mean = sum(v) / len(v)
    v_max = max(v)
    v_min = min(v)

    sum1 = 0
    for i in range(len(v)):
        sum1 += (v[i] - v_mean) ** 2

    v_stdev = math.sqrt(sum1 / len(v))

    print("Average = ", v_mean)
    print("Max = ", v_max)
    print("Min = ", v_min)
    print("Odchylenie standardowe = ", v_stdev)


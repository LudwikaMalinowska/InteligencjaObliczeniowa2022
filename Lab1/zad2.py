import math
import random
import statistics


def vector_sum(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i] + v2[i])

    return v3


def vector_multiply(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i] * v2[i])

    return v3


def vector_iloczyn_skalarny(v1, v2):
    iloczyn = 0
    for i in range(len(v1)):
        iloczyn += v1[i] * v2[i]

    return iloczyn


def dlugosc_euklidesowa(v):
    suma_kwadratow = 0
    for i in range(len(v1)):
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


def normalize(v):
    v_max = max(v)
    v_min = min(v)
    normalized = []
    print("Old max: ", v_max)

    for x in v:
        z = (x - v_min) / (v_max - v_min)
        normalized.append(z)

    print("New max: ", max(normalized))
    return normalized


def standarize(v):
    v_mean = sum(v) / len(v)
    v_stdev = statistics.stdev(v)
    standarized = []
    print("Stara średnia: ", v_mean)
    print("Stare odchylenie standardowe: ", v_stdev)

    for x in v:
        z = (x - v_mean) / v_stdev
        standarized.append(z)

    new_mean = sum(standarized) / len(standarized)
    new_stdev = statistics.stdev(standarized)
    print("Nowa średnia: ", new_mean)
    print("Nowa odchylenie standardowe: ", new_stdev)

    return standarized


def przedzial(x):
    if x < 10:
        return "[0, 10)"
    elif x < 20:
        return "[10, 20)"
    elif x < 30:
        return "[20, 30)"
    elif x < 30:
        return "[30, 40)"
    elif x < 50:
        return "[40, 50)"
    elif x < 60:
        return "[50, 60)"
    elif x < 70:
        return "[60, 70)"
    elif x < 80:
        return "[70, 80)"
    elif x < 80:
        return "[80, 90)"
    else:
        return "[90, 100]"


def discredit(v):
    discredited = []
    for x in v:
        discredited.append(przedzial(x))

    print("Nowy wektor po dyskredytacji: ", discredited)
    return discredited


v1 = [3, 8, 9, 10, 12]
v2 = [8, 7, 7, 5, 6]

print("2a:")
print("Suma wektorów: ", vector_sum(v1, v2))
print("Iloczyn (po współrzędnych) wektorów: ", vector_multiply(v1, v2))

print("\n2b:")
print("Iloczyn skalarny: ", vector_iloczyn_skalarny(v1, v2))

print("\n2c:")
print("Długość wektora v1: ", dlugosc_euklidesowa(v1))
print("Długość wektora v2: ", dlugosc_euklidesowa(v2))

print("\n2d")
random_vector = random_50()
print(random_vector)

print("\n2e")
vector_stats(random_vector)

print("\n2f")
normalized = normalize(random_vector);
print(normalized)

print("\n2g")
standarized = standarize(random_vector)
print(standarized)

print("\n2h")
discredited = discredit(random_vector)
print(discredited)


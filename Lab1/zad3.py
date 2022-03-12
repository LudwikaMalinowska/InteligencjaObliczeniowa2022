import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

miasta = pd.read_csv("miasta.csv")
print("3a:")
print(miasta)
print("\n\n")
print(miasta.values)

print("3b:")
nData = {"Rok": 2010, "Gdansk": 460, "Poznan": 555, "Szczecin": 405}
miasta = miasta.append(nData, ignore_index=True)
print(miasta)

print("3c:")
x = miasta.get("Rok")
y = miasta.get("Gdansk")
print(x, y)
plt.plot(x, y, '-or')
plt.xticks(np.arange(min(x), max(x)+1, 10))
plt.xlabel("Lata")
plt.ylabel("Liczba ludności [w tys.]")
plt.title("Ludność w miastach Polski")
plt.show()


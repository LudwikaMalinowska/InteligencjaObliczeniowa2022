import pandas as pd
from matplotlib import pyplot as plt

miasta = pd.read_csv("miasta.csv")
print("3a:")
print(miasta)
print("\n\n")
print(miasta.values)

print("3b:")
miasta.append([2010, 460, 555, 405])
print(miasta)

print("3c:")
x = miasta.get("Rok")
y = miasta.get("Gdansk")
print(x, y)
plt.plot(x,y)
plt.show()


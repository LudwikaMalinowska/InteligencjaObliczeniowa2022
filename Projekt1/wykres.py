
from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv("time_data.csv")
print(table.head())
print(table.columns)


plt.plot(table["size"], table["time_pygad"], label="algorytm genetyczny")


plt.legend(loc="upper left")
# plt.ylim(-0.01, 0.01)
# plt.xlim(0, 1)
# plt.yscale("log")
plt.show()
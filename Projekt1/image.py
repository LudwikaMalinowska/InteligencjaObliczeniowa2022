import matplotlib.pyplot as plt
import numpy as np

def plot(array):
    img = np.array(array, dtype=np.float64)
    img = np.stack([img, img, img], axis=2)
    img = np.abs(img - 1)
    plt.imshow(img)
    plt.show()


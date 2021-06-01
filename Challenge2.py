import numpy as np
import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.hist(nums, bins, color="green")
plt.title("Histogram of nums against bins", fontsize=20)
plt.xlabel("Nums", fontsize=16)
plt.ylabel("Bins", fontsize=16)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

pic = plt.imread("6 Arrays and Images/84.png")

# Trim image to make dimensions divisible by 100
h, w = pic.shape
pic = pic[:(h // 100) * 100, :(w // 100) * 100]

# Reshape into 100x100 blocks
reshaped = pic.reshape(h // 100, 100, w // 100, 100)

# Move the block dimensions to the front and compute mean over inner pixels
means = reshaped.mean(axis=(1, 3))

plt.imshow(means, cmap='gray')
plt.show()
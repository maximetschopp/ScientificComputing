import numpy as np
import matplotlib.pyplot as plt

pic = plt.imread("6 Arrays and Images/holbein.png")
rotated_img = 0 * pic

isize = pic.shape[0]
jsize = pic.shape[1]
print(isize, jsize)


# rotate -45deg then stretch vertically
angle = -1.2 * np.pi /8
cos_value = np.cos(angle)
sin_value = np.sin(angle)
def rotationTransform(x, y):
    return int(x * cos_value - y * sin_value), int(x * sin_value + y * cos_value)

pivot_x = 2 * isize // 3
pivot_y = jsize // 2

for i in range(isize):
    for j in range(jsize):
        p_x = i - pivot_x
        p_y = j - pivot_y
        x, y = rotationTransform(p_x, p_y)
        x = x + pivot_x
        y = y + pivot_y
        if ( 0 < x < isize and 0 < y < jsize):
            rotated_img[x][y] = pic[i][j]


stretch_factor = 8
stretched_img = 0 * rotated_img
isize = len(rotated_img)

for i in range(isize):
    for j in range(jsize):
        y = i // stretch_factor + 800

        stretched_img[i][j] = rotated_img[y][j]


plt.imshow(stretched_img)
plt.show()
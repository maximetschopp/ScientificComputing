import numpy as np
import matplotlib.pyplot as plt

img_path = "/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/10 3d geometry/Equirectangular_projection_SW.jpg"


img = plt.imread(img_path)

# Check if it's already grayscale
if img.ndim == 2:
    gray_img = img  # already grayscale
else:
    # Convert RGB to grayscale using the luminosity method
    gray_img = img[..., :3] @ [0.2989, 0.5870, 0.1140]

def Rx(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), np.sin(theta)],
        [0, -np.sin(theta), np.cos(theta)]
    ])

def Ry(theta):
    return np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])

def Rz(theta):
    return np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def daylight(latitude, longitude, date, time):
    # Constants
    e_x = np.array([1, 0, 0])
    iota = np.radians(23.5)  # Earth's axial tilt
    beta = 2 * np.pi * (date / 365.25)  # one full circle per year
    sigma = np.radians(longitude) + 2 * np.pi * time + beta  # sidereal angle

    # Sun vector
    e_sun = Rz(beta) @ Rx(-iota) @ e_x #@ means matrix multiplication

    # Surface normal
    phi = np.radians(latitude)
    e_perp = Rz(sigma) @ Ry(phi) @ e_x

    return np.dot(e_sun, e_perp)

date = 0
time = 0.4

lats = np.linspace(-90, 90, 180)
lons = np.linspace(-180, 180, 360)
LON, LAT = np.meshgrid(lons, lats)

Z = np.vectorize(daylight)(LAT, LON, date, time)


# Display the grayscale image
plt.figure()
plt.imshow(gray_img, cmap="gray", interpolation='nearest', extent=(-180, 180, -90, 90))
plt.contour(LON, LAT, Z, levels=100, cmap='inferno', alpha=0.4)  # or cmap='gray' etc.
plt.axis('off')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Load and convert image ---
img_path = "/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/10 3d geometry/Equirectangular_projection_SW.jpg"
img = plt.imread(img_path)

if img.ndim == 2:
    gray_img = img
else:
    gray_img = img[..., :3] @ [0.2989, 0.5870, 0.1140]

# --- Rotation matrices ---
def Rx(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), np.sin(theta)],
        [0, -np.sin(theta), np.cos(theta)]
    ])

def Rz(theta):
    return np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# --- Vectorized daylight function ---
def daylight(lat, lon, date, time):
    phi = np.radians(lat)
    sigma = np.radians(lon) + 2 * np.pi * time + 2 * np.pi * (date / 365.25)
    iota = np.radians(23.5)
    beta = 2 * np.pi * (date / 365.25)
    e_sun = Rz(beta) @ Rx(-iota) @ np.array([1, 0, 0])
    x = np.cos(phi) * np.cos(sigma)
    y = np.cos(phi) * np.sin(sigma)
    z = np.sin(phi)
    return e_sun[0]*x + e_sun[1]*y + e_sun[2]*z

# --- Grid setup ---
lats = np.linspace(-90, 90, 180)
lons = np.linspace(-180, 180, 360)
LON, LAT = np.meshgrid(lons, lats)
date = 80

# --- Precompute daylight overlays ---
Z_list = [daylight(LAT, LON, date, hour / 100) for hour in range(100)]

# Normalize to [0, 1] with daylight only (clip night side)
Z_list = [np.clip((Z + 1) / 2, 0, 1) for Z in Z_list]  # convert from [-1,1] to [0,1]

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(gray_img, cmap='gray', extent=[-180, 180, -90, 90], origin='upper')
heat = ax.imshow(Z_list[0], cmap='inferno', alpha=0.5,
                 extent=[-180, 180, -90, 90], origin='upper', vmin=0, vmax=1)
title = ax.set_title("Hour: 0")
ax.axis('off')

# --- Animation function ---
def update(hour):
    heat.set_data(Z_list[hour])
    hr = str(round(hour / 100 * 24, 1)).split(".")[0]
    min = str(round(hour / 100 * 24 % 1 * 0.6, 2)).split(".")[1]
    title.set_text(f"{"0" + hr if len(hr) == 1 else hr}:{"0" + min if len(min) == 1 else min}")
    return [heat, title]

# --- Animate ---
ani = FuncAnimation(fig, update, frames=100, interval=100, blit=False)
plt.show()

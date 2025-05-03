import numpy as np
import matplotlib.pyplot as plt

surface_data_path = "/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/10 3d geometry/surface.xyz"
terrain_data_path = "/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/10 3d geometry/terrain.xyz"

surface_data = np.loadtxt(surface_data_path, skiprows=1).reshape( 2000, 2000, 3)
terrain_data = np.loadtxt(terrain_data_path, skiprows=1).reshape( 2000, 2000, 3)


# Extract x, y, z
surface_x_grid = surface_data[:, :, 0]
surface_y_grid = surface_data[:, :, 1]
surface_z_grid = surface_data[:, :, 2]

terrain_x_grid = terrain_data[:, :, 0]
terrain_y_grid = terrain_data[:, :, 1]
terrain_z_grid = terrain_data[:, :, 2]

# Plot heightmap
plt.figure(figsize=(8, 8))
plt.gca().set_aspect('equal')
plt.pcolormesh(terrain_x_grid, terrain_y_grid, terrain_z_grid, shading='auto', cmap='terrain')
plt.contour(surface_x_grid, surface_y_grid, surface_z_grid, shading='auto', cmap='Reds', levels=200, alpha=0.2)
plt.colorbar(label='Elevation (m)')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Heightmap of Switzerland")
plt.show()
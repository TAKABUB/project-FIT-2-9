import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps


contour_g = np.array([
    [-12.9, -9.5], [-8.5, -8.0], [-5.0, -5.2], [-4.4, 0.0], [-4.9, 4.5], [-3.9, 9.9], 
    [-1.7, 12.6], [2.3, 13.7], [7.8, 13.2], [9.3, 8.4], [9.5, 5.5], 
    [9.5, 2.0], [9.6, -2.0], [8.8, -5.1], [6.7, -7.2], [2.6, -9.5], 
    [-3.1, -11.2], [-8.0, -11.8], [-12.9, -9.5]
])


# Separate x and y coordinates
x_g = contour_g[:, 0]
y_g = contour_g[:, 1]

# Calculate the area using Simpson's rule
area_g_km2 = simps(y_g, x_g)

# Plot the stylized contour and show calculated area
plt.figure(figsize=(8, 8))
plt.plot(x_g, y_g, 'b-', linewidth=2)
plt.fill(x_g, y_g, 'b', alpha=0.3)  # Fill the contour to visualize the area
plt.title(f'Stylized Area of Grenada: {abs(area_g_km2):.2f} km²')
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.grid(True)
plt.show()

print(f"Approximate area of the stylized Grenada: {abs(area_g_km2):.2f} km²")

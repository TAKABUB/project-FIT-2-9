from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Відкриваємо зображення
image_path = r'C:\Users\takab\Desktop\матан\image.png'
image = Image.open(image_path).convert('L')  # Перетворимо у відтінки сірого для зручності
pixels = np.array(image)

# Налаштування масштабу
cm_to_km = 1.36  # 1 см = 1.36 км
cm_to_px = 37.39  # кількість пікселів в 1 см
rect_width_px = 10  # ширина одного прямокутника в пікселях
rect_height_px = 10  # висота одного прямокутника в пікселях
# Площа одного прямокутника в км²
rect_area_km2 = ((cm_to_km / cm_to_px) * rect_width_px) * ((cm_to_km / cm_to_px) * rect_height_px)

# Розміри зображення
image_height, image_width = pixels.shape

# Ініціалізація змінної для загальної площі
total_area_km2 = 0

# Підготовка візуалізації
fig, ax = plt.subplots()
ax.imshow(pixels, cmap='gray')

# Розрахунок площі методом прямокутників і побудова сітки
for y in range(0, image_height, rect_height_px):
    for x in range(0, image_width, rect_width_px):
        # Витягуємо прямокутник
        rect = pixels[y:y + rect_height_px, x:x + rect_width_px]
        total_area_km2 += rect_area_km2
        ax.add_patch(patches.Rectangle((x, y), rect_width_px, rect_height_px, 
                                       linewidth=1, edgecolor='red', facecolor='none'))

# Відображення загальної площі
print(f"Площа Гренади: {total_area_km2:.2f} квадратних кілометрів")

# Показуємо зображення з накладеними прямокутниками
plt.show()

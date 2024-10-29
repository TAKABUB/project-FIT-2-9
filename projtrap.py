from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def calculate_and_visualize_area(image_path, cm_to_km, cm_to_px, n=10):
    # Відкрити зображення
    image = Image.open(image_path)
    width_px, height_px = image.size
    
    # Конвертація розмірів зображення в сантиметри
    width_cm = width_px / cm_to_px
    height_cm = height_px / cm_to_px
    
    # Конвертація розмірів зображення в кілометри
    width_km = width_cm * cm_to_km
    height_km = height_cm * cm_to_km
    
    # Висота кожної трапеції в кілометрах
    trap_height_km = height_km / n
    
    # Ініціалізація загальної площі
    total_area_km2 = 0.0
    
    # Візуалізація
    fig, ax = plt.subplots()
    ax.imshow(image)
    
    # Обчислення та відображення трапецій
    trap_height_px = height_px // n
    
    for i in range(n):
        # Обчислення площі поточної трапеції
        a = width_km  # ширина зверху
        b = width_km  # ширина знизу (однакові для прямокутних трапецій)
        total_area_km2 += (a + b) * trap_height_km / 2
        
        # Візуалізація трапеції
        top_y = i * trap_height_px
        bottom_y = (i + 1) * trap_height_px
        trap = patches.Polygon([[0, top_y], [width_px, top_y], [width_px, bottom_y], [0, bottom_y]], 
                               closed=True, edgecolor='red', facecolor='none', linewidth=1.5)
        ax.add_patch(trap)
    
    # Показ зображення з трапеціями
    ax.set_title(f"Total Area: {total_area_km2:.4f} km²")
    plt.show()
    
    return total_area_km2

# Виклик функції
image_path = r'C:\Users\takab\Desktop\матан\image.png'
cm_to_km = 1.36
cm_to_px = 37.39
area_km2 = calculate_and_visualize_area(image_path, cm_to_km, cm_to_px, n=10)
print("Площа зображення в км²:", area_km2)

from PIL import Image
import random

color_dict = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'pink': (255, 192, 203),
    'orange': (255, 165, 0),
    'purple': (128, 0, 128),
    'brown': (165, 42, 42),
    'gray': (128, 128, 128),
    'lightgray': (211, 211, 211),
    'darkgray': (169, 169, 169),
    'lime': (50, 205, 50),
    'teal': (0, 128, 128),
    'navy': (0, 0, 128),
    'olive': (128, 128, 0),
    'maroon': (128, 0, 0)
}

requested_color = 0

def get_color_input(prompt):
    while True:
        color_name = input(prompt).strip().lower()
        requested_color = color_name
        if color_name in color_dict:
            return color_dict[color_name]
        else:
            print("Error: Invalid color name. Please enter a valid color name.")

def add_noise(base_color, intensity=30):
    r, g, b = base_color
    r = min(max(r + random.randint(-intensity, intensity), 0), 255)
    g = min(max(g + random.randint(-intensity, intensity), 0), 255)
    b = min(max(b + random.randint(-intensity, intensity), 0), 255)
    return (r, g, b)

base_color = get_color_input("Enter the base color (e.g., red, blue): ")

width, height = 1000, 1000
image = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        color_with_noise = add_noise(base_color)
        image.putpixel((x, y), color_with_noise)

image.save(requested_color + ".png")
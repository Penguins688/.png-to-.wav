from PIL import Image

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

def get_color_input(prompt):
    while True:
        color_name = input(prompt).strip().lower()
        if color_name in color_dict:
            return color_dict[color_name]
        else:
            print("Error: Invalid color name. Please enter a valid color name.")

start_color = get_color_input("Enter the start color (e.g., red, blue): ")
end_color = get_color_input("Enter the end color (e.g., red, blue): ")

width, height = 1000, 1000
image = Image.new("RGB", (width, height))

for x in range(width):
    blend = x / (width - 1)
    r = int(start_color[0] * (1 - blend) + end_color[0] * blend)
    g = int(start_color[1] * (1 - blend) + end_color[1] * blend)
    b = int(start_color[2] * (1 - blend) + end_color[2] * blend)
    for y in range(height):
        image.putpixel((x, y), (r, g, b))

image.save("gradient.png")
print("Gradient image saved as 'gradient.png'.")

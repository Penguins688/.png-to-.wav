from PIL import Image
import wave
import numpy

def reduce_image_colors(img, num_colors=256):
    img = img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
    return img

def calculate_image_dimensions(size):
    side_length = int(numpy.ceil(numpy.sqrt(size)))
    return side_length, side_length

file_path = input("Enter .png path: ")
img = Image.open(file_path)

img = reduce_image_colors(img)
width, height = img.size

palette = img.getpalette()
num_colors = len(palette) // 3
colors = [(palette[i], palette[i+1], palette[i+2]) for i in range(0, len(palette), 3)]

color_to_byte = {color: i for i, color in enumerate(colors)}

decoded_data = bytearray()
for y in range(height):
    for x in range(width):
        pixel_color = img.getpixel((x, y))
        if pixel_color < len(colors):
            decoded_data.append(pixel_color % 257)
        else:
            print(f"Unexpected color index found: {pixel_color}")
            break

output_file_path = 'output.wav'
with wave.open(output_file_path, 'wb') as wav_file:
    num_channels = 1
    sample_width = 1
    frame_rate = 44100
    num_frames = len(decoded_data)

    wav_file.setnchannels(num_channels)
    wav_file.setsampwidth(sample_width)
    wav_file.setframerate(frame_rate)
    wav_file.setnframes(num_frames)

    wav_file.writeframes(decoded_data)

print(f"Decoded data saved to {output_file_path}")
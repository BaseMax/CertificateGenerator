from PIL import Image, ImageDraw, ImageFont
import os

# Firstly, let's define some constants and paths
BACKGROUND_IMG = 'certificate-background.png'
FONT_PATH = "arial.ttf"
OUTPUT_DIR = "output"
NAMES = ["Ali Mohammadiyeh", "John Doe", "Jane Smith"]

# Check output directory exists, if not create it
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Load the background image
img = Image.open(BACKGROUND_IMG)

# Get the drawing context
draw = ImageDraw.Draw(img)

# Define the font and its size
font = ImageFont.truetype(FONT_PATH, 50)

for name in NAMES:
    # center the text based on its size and the image size
    text_width, text_height = draw.textsize(name, font)
    x = (img.width - text_width) / 2
    y = 200
    
    # Draw the text on the image
    draw.text((x, y), name, font=font, fill=(0, 0, 0))
    
    # Save the output image in the output directory with a unique filename 
    output_filename = os.path.join(OUTPUT_DIR, f"certificate-{name.replace(' ', '-').lower()}.png")
    img.save(output_filename)

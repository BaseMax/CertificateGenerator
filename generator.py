import os
import re
from PIL import Image, ImageDraw, ImageFont

# Define constants and paths
BACKGROUND_IMG_PATH  = 'certificate-background.png'
FONT_PATH = "arial.ttf"
OUTPUT_DIR_PATH = "output"
TEXT_COLOR = (0, 116, 95)
NAMES_FILE_PATH = "names.txt"
FONT_SIZE = 130

#==================================== read names from file ====================================#
def Read_Names(file_path):
    """
    Read the names from the specified file and return them as a list.
    """
    names = []  # names = ["Ali Mohammadiyeh", "John Doe", "Jane Smith", "Iman Mirazimi", "Matin Mohammadi"]

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            line = line.replace("\t", " ")
            line = re.sub(r"\s+", " ", line)

            if line:
                names.append(line)
    return names
#=========================================   file name ===================================================#
def Certificate_Filename(name):
    """
     make filename for the certificate image related on their names.
    """
    return os.path.join(OUTPUT_DIR_PATH, f"certificate-{name.replace(' ', '-').lower()}.png")

#==================================== Design and make the certificate ====================================#

def Design_Certificate(name):
    """
    Design a certificate image for the each name.
    """
    # Load the background image
    background_img = Image.open(BACKGROUND_IMG_PATH)

    # Get the drawing context
    draw = ImageDraw.Draw(background_img)

    # center the text based on its size and the image size
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    text_width, text_height = draw.textsize(name, font)
    x_position = (background_img.width - text_width) / 2
    y_position = 840
    
    # Draw the text on the image
    draw.text((x_position, y_position), name, font=font, fill=TEXT_COLOR)
    
    # Save the output image in the output directory with a unique filename 
    output_filename = Certificate_Filename(name)
    background_img.save(output_filename)
    print(f"{output_filename} generated")
    
#======================================= create the certificates ==============================================#
def Create_Certificates(names):
    """
    Create a certificate image for each name in the list.
    """
    # Check output directory exists, if not create it
    if not os.path.exists(OUTPUT_DIR_PATH):
        os.makedirs(OUTPUT_DIR_PATH)
    
    for name in names:
        Design_Certificate(name)

if __name__ == "__main__":
    # Read the names from the file
    names = Read_Names(NAMES_FILE_PATH)

    # Create a certificate image for each name
    Create_Certificates(names)

import os
from PIL import Image

# Input and output folder paths
input_folder = "images"
output_folder = "resized"

# Resize dimensions
resize_width = 200
resize_height = 200

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open, resize, and save the image
        with Image.open(input_path) as img:
            resized_img = img.resize((resize_width, resize_height))
            resized_img.save(output_path)

        print(f"Resized and saved: {output_path}")

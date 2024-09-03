import os
from PIL import Image

def find_bounding_box(image):
    """Find the bounding box of the non-white areas in the image."""
    # Convert image to RGBA if it isn't already
    image = image.convert("RGBA")

    # Get data of the image
    data = image.getdata()

    # Variables to track bounds
    left = image.width
    top = image.height
    right = 0
    bottom = 0

    for y in range(image.height):
        for x in range(image.width):
            # Get pixel value
            r, g, b, a = data[y * image.width + x]
            # Check if the pixel is not fully transparent or not white
            if a != 0 and (r, g, b) != (255, 255, 255):
                if x < left:
                    left = x
                if y < top:
                    top = y
                if x > right:
                    right = x
                if y > bottom:
                    bottom = y

    # Return the bounding box coordinates (left, top, right, bottom)
    return (left, top, right, bottom)

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Open the image file
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Find bounding box
            bbox = find_bounding_box(image)

            # Crop the image to the bounding box
            cropped_image = image.crop(bbox)

            # Save the cropped image
            output_path = os.path.join(output_folder, filename)
            cropped_image.save(output_path, "PNG")
            print(f"Processed and saved: {output_path}")

# Example usage:
input_folder = './'
output_folder = './'

process_images(input_folder, output_folder)

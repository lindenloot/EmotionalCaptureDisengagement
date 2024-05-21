import cv2
import numpy as np

# Load the image
image_path = './F01_FE.png'
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Extract the alpha channel
alpha_channel = image[:, :, 3]

# Threshold the alpha channel to get a binary mask
_, binary_mask = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)

# Find contours from the binary mask
contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty image with the same dimensions as the input
filled_image = np.zeros_like(image)

# Define the color to fill (BGR format for OpenCV)
fill_color = (36, 54, 237, 255)  # Green color with full opacity

# Fill the contours on the empty image
for contour in contours:
    cv2.drawContours(filled_image, [contour], -1, fill_color, thickness=cv2.FILLED)

# Save the filled image
output_path = './filled_image.png'
cv2.imwrite(output_path, filled_image)

print(f"Image saved at {output_path}")

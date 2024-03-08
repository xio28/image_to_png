from PIL import Image
from typing import Optional
import os
import pillow_avif

# Define the image formats and the default paths
IMAGE_FORMATS = ['.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.avif']
DEFAULT_SOURCE_FOLDER = os.path.abspath('images')
CONVERTED_IMAGES = os.path.abspath('converted_images')

# Function to check if the source folder exists
def check_source_folder(folder: Optional[str]) -> str:
    # Use the default folder if none is provided
    if folder is None:
        folder = DEFAULT_SOURCE_FOLDER

    # If the folder does not exist, print a message and return an empty string
    if not os.path.exists(folder):
        print(f"The source folder '{folder}' does not exist.")
        return None
    
    return folder

# Function to convert images to PNG format
def convert_to_png(source_folder: Optional[str] = None):
    # Verify and get the source folder
    images_folder = check_source_folder(source_folder)
    if images_folder is None:
        return

    # Create the converted images folder if it doesn't exist
    if not os.path.exists(CONVERTED_IMAGES):
        os.makedirs(CONVERTED_IMAGES)

    # Process the images in the source folder
    for filename in os.listdir(images_folder):
        file_path = os.path.join(images_folder, filename)
        
        if filename.lower().endswith(tuple(IMAGE_FORMATS)):
            try:
                with Image.open(file_path) as img:
                    if img.mode not in ('RGB', 'RGBA'):
                        img = img.convert('RGBA')
                        
                    new_filename = os.path.splitext(filename)[0] + '.png'
                    img.save(os.path.join(CONVERTED_IMAGES, new_filename), 'PNG', optimize=True)
                    print(f"Converted {filename} to {new_filename}")
            except Exception as e:
                print(f"Error converting {filename}: {e}")


# Call the function with the default folder if no path is provided
convert_to_png()

from PIL import Image
import pillow_avif
import os

IMAGE_FORMATS = ['.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.avif']
IMAGES_TO_CONVERT = os.path.abspath('images')
CONVERTED_IMAGES = os.path.abspath('converted_images')


def convert_to_png():
    for filename in os.listdir(IMAGES_TO_CONVERT):
        file_path = os.path.join(IMAGES_TO_CONVERT, filename)
        
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
                

convert_to_png()
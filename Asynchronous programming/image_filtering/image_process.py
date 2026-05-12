import os
import time
from PIL import Image, ImageFilter
import concurrent.futures

image_names = [f"images/{img}" for img in os.listdir("images")]

size = (800, 800)

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(5))
    img.thumbnail(size)

    img.save(f'processed/{os.path.basename(img_name)}')
    print(f'{img_name} was processed...')

os.makedirs("processed", exist_ok=True)
t1 = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, image_names)
t2 = time.perf_counter()
print(f"Processing time: {t2 - t1:.2f} seconds")
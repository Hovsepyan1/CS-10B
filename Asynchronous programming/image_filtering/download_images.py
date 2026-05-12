import requests

images_url = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def download_images(image):
    content = requests.get(image).content
    img_name = image.split("/")
    img_name = f"{img_name[3]}.jpg"
    with open(f"images/{img_name}", "wb") as i:
        i.write(content)

for i in images_url:
    download_images(i)
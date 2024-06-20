import os

IMAGE_DIR = 'temp/images'

def save_image(image):
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    idx = len(os.listdir(IMAGE_DIR))
    image_path = os.path.join(IMAGE_DIR, f'image_{idx}.jpg')
    with open(image_path, 'wb') as img_file:
        img_file.write(image)

def get_saved_images():
    return [os.path.join(IMAGE_DIR, img) for img in os.listdir(IMAGE_DIR)]

def clear_images():
    for img in os.listdir(IMAGE_DIR):
        os.remove(os.path.join(IMAGE_DIR, img))

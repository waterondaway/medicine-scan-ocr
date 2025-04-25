from PIL import Image, ImageEnhance
import numpy as np
import os
import random

def add_light_noise(img, std=10):
    np_img = np.array(img)
    noise = np.random.normal(0, std, np_img.shape).astype(np.int16)
    noisy_img = np.clip(np_img + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy_img)

def rotate_slightly(img, max_angle=3):
    angle = random.uniform(-max_angle, max_angle)
    return img.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor="white")

def adjust_brightness_slightly(img, range_min=0.9, range_max=1.1):
    factor = random.uniform(range_min, range_max)
    return ImageEnhance.Brightness(img).enhance(factor)

def augment_gently_and_save(img_path, output_dir):
    img = Image.open(img_path).convert("RGB")
    filename = os.path.splitext(os.path.basename(img_path))[0]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    rotated = rotate_slightly(img)
    bright = adjust_brightness_slightly(rotated)
    final = add_light_noise(bright, std=10)

    save_path = os.path.join(output_dir, f"{filename}.png")
    final.save(save_path)
    print(f"✅ Saved: {save_path}")

folder = ['ChakraPetch', 'Kanit', 'Krub', 'Sarabun', 'Prompt']
type = ['bold', 'italic', 'regular']

for i in folder:
    for j in type:
        input_folder = f"picture/{i}/{j}"
        output_folder = f"picture/{i}-Augmentation/{j}"
        for file in os.listdir(input_folder):
            if file.endswith(".png"):
                augment_gently_and_save(os.path.join(input_folder, file), output_folder)

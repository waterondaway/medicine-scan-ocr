from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import pandas as pd
import os, csv, random

# Config the specific directory
output_directory = "../assets/output"
font_directory = "../assets/fonts"
file_path = "../lastest.csv"

# Config parameter values
font_size = 40
width, height = 720, 480
background_color = "white"
text_color = "black"

def augment_image(image, filename):
    # Randomly rotate the image
    angle = random.randint(-10, 10)
    image = image.rotate(angle, expand=True)

    enhancer = ImageEnhance.Brightness(image)
    brightness_factor = random.uniform(0.8, 1.5)
    image = enhancer.enhance(brightness_factor)

    noise_level = 20
    noise = Image.effect_noise(image.size, noise_level).convert("RGB")
    image = Image.blend(image, noise, alpha=0.2)

    augmented_filename = f"{filename}.png"
    save_path = os.path.join(output_directory, augmented_filename)
    image.save(save_path)
    print(f"Augmented image saved: {augmented_filename}")

def init_draw(fonts):
    img = Image.new("RGB", (720, 480), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_directory + "/" + fonts, font_size)
    return img, draw, font

def save_image(img, filename):
    save_path = os.path.join(output_directory, f"{filename}.png")
    img.save(save_path)
    augment_image(img, f"{filename}_augmented")

def save_label_text(row, filename):
    label_save_path = os.path.join(output_directory, f"{filename}.txt")
    with open(label_save_path, mode="w", encoding="utf-8") as file:
        file.write(f"ชื่อ {row['PATIENT_NAME']}\n")
        file.write(f"บัตรประจำตัว {row['PATIENT_ID']}\n")
        file.write(f"วันเกิด {row['PATIENT_BIRTHDATE']}\n")
        file.write(f"{row['DRUG_REG_NO']}\n")
        file.write(f"วันผลิต {row['MFG_DATE']}\n")
        file.write(f"วันหมดอายุ {row['EXP_DATE']}\n")
        file.write(f"{(row['DRUG_NAME']).upper()} {row['DOSAGE']} {row['FORM'].upper()}\n")
        file.write(f"{row['USAGE_INSTRUCTIONS']}\n")
        file.write(f"{row['INDICATIONS']}\n")
        file.write(f"{row['WARNINGS']}\n")

def make_medicine_label(fonts, filename):
    count = 1
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            img, draw, font = init_draw(fonts)
            # Draw a text
            draw.text((30, 40), f"ชื่อ {row['PATIENT_NAME']}", fill="black", font=font) # Patient Name
            draw.text((30, 90), f"บัตรประจำตัว {row['PATIENT_ID']}", fill="black", font=font) # Patient ID
            draw.text((30, 140), f"วันเกิด {row['PATIENT_BIRTHDATE']}", fill="black", font=font) # Birthdate
            draw.text((420, 40), f"{row['DRUG_REG_NO']}", fill="black", font=font) # Drug Reg. No.
            draw.text((420, 90), f"วันผลิต {row['MFG_DATE']}", fill="black", font=font) # MFG Date
            draw.text((420, 140), f"วันหมดอายุ {row['EXP_DATE']}", fill="black", font=font) # EXP Date
            draw.text((0, 180), f"-"*300, fill="black", font=font) # Line
            draw.text((30, 220), f"{(row['DRUG_NAME']).upper()}", fill="black", font=font) # Drug Name
            draw.text((280, 220), f"{row['DOSAGE']}", fill="black", font=font) # Dosage
            draw.text((420, 220), f"{row['FORM'].upper()}", fill="black", font=font) # Form
            draw.text((30, 270), f"{row['USAGE_INSTRUCTIONS']}", fill="black", font=font) # Usage Instructions
            draw.text((30, 320), f"{row['INDICATIONS']}", fill="black", font=font) # Indications
            draw.text((30, 370), f"{row['WARNINGS']}", fill="black", font=font) #  Warnings
            
            save_image(img, filename + "_" + str(count))
            print(f"Finish save to assets/output/{filename + "_" + str(count)}")
            save_label_text(row, filename + "_" + str(count))
            count = count + 1
            

for font_file in os.listdir(font_directory):
    if font_file.endswith(".ttf"):
        print(f"Processing font: {font_file}")
        font_name = os.path.splitext(font_file)[0]
        filename = (font_name.lower()).replace(" ", "")
        make_medicine_label(f"{font_file}", filename)




    


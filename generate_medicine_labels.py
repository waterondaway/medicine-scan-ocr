from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os, csv

# Config the specific directory
font_directory = "./font/"
file_path = "./prescription_data.csv"

# Config parameter values
font_size = 26
width, height = 720, 480
background_color = "white"
text_color = "black"

def init_draw(fonts):
    img = Image.new("RGB", (720, 480), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_directory + f'{fonts.split("-")[0]}/' + fonts, font_size)
    return img, draw, font

def save_image(font, img, filename):
    type = filename.split("_")[1]
    save_path = os.path.join(f'picture/{font}/{type}', f"{filename}.png")
    img.save(save_path)

def make_medicine_label(fonts, filename):
    count = 1
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            img, draw, font = init_draw(fonts)
            # Draw a text
            draw.text((30, 40), f"ชื่อ {row['patient_name']}", fill="black", font=font) # Patient Name
            draw.text((30, 90), f"บัตรประจำตัว {row['patient_id']}", fill="black", font=font) # Patient ID
            draw.text((30, 140), f"วันเกิด {row['patient_birthdate']}", fill="black", font=font) # Birthdate
            draw.text((420, 40), f"{row['drug_reg_no']}", fill="black", font=font) # Drug Reg. No.
            draw.text((420, 90), f"วันผลิต {row['mfg_date']}", fill="black", font=font) # MFG Date
            draw.text((420, 140), f"วันหมดอายุ {row['exp_date']}", fill="black", font=font) # EXP Date

            draw.text((30, 220), f"{(row['drug_name']).upper()}", fill="black", font=font) # Drug Name
            draw.text((280, 220), f"{row['dosage']}", fill="black", font=font) # Dosage
            draw.text((420, 220), f"{row['form'].upper()}", fill="black", font=font) # Form
            draw.text((30, 270), f"{row['usage_instructions']}", fill="black", font=font) # Usage Instructions
            draw.text((30, 320), f"{row['indications']}", fill="black", font=font) # Indications
            draw.text((30, 370), f"{row['warnings']}", fill="black", font=font) #  Warnings
            
            save_image(fonts.split("-")[0], img, filename + "_" + str(count))
            print(f"Finish save to picture/{fonts.split('-')[0]}/{filename + '_' + str(count)}")
            count = count + 1


for font_folder in os.listdir(font_directory):
    if font_folder == ".DS_Store":
        continue
    for font_file in os.listdir(font_directory + font_folder):
        if font_file == ".DS_Store":
            continue
        print(f'Processing font: {font_file}')
        font_name = os.path.splitext(font_file)[0]
        filename = (font_name.lower()).replace("-", "_")
        print(font_name.split("-")[0])
        make_medicine_label(font_file, filename)

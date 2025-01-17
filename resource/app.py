from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os, csv

# Config the specific directory
output_directory = "../assets/output"
font_directory = "../assets/fonts"
file_path = "../data/drug_labels.csv"

# Config parameter values
font_size = 40
width, height = 720, 480
background_color = "white"
text_color = "black"

# Data for generate dataset
# NaN

def init_draw(fonts):
    img = Image.new("RGB", (720, 480), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_directory + "/" + fonts, font_size)
    return img, draw, font

def save_image(img, filename):
    save_path = os.path.join(output_directory, f"{filename}.png")
    img.save(save_path)

def save_label_text(row, filename):
    label_save_path = os.path.join(output_directory, f"{filename}.txt")
    with open(label_save_path, mode="w", encoding="utf-8") as file:
        file.write(f"ชื่อ {row['patient_name']}\n")
        file.write(f"บัตรประจำตัว {row['patient_id']}\n")
        file.write(f"วันเกิด {row['patient_birthdate']}\n")
        file.write(f"{row['drug_reg_no']}\n")
        file.write(f"วันผลิต {row['mfg_date']}\n")
        file.write(f"วันหมดอายุ {row['exp_date']}\n")
        file.write(f"{(row['drug_name']).upper()} {row['dosage']} {row['form'].upper()}\n")
        file.write(f"{row['usage_instructions']}\n")
        file.write(f"{row['indications']}\n")
        file.write(f"{row['warnings']}\n")

def make_medicine_label(fonts, filename):
    count = 0
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
            draw.text((0, 180), f"-"*300, fill="black", font=font) # Line
            draw.text((30, 220), f"{(row['drug_name']).upper()}", fill="black", font=font) # Drug Name
            draw.text((280, 220), f"{row['dosage']}", fill="black", font=font) # Dosage
            draw.text((420, 220), f"{row['form'].upper()}", fill="black", font=font) # Form
            draw.text((30, 270), f"{row['usage_instructions']}", fill="black", font=font) # Usage Instructions
            draw.text((30, 320), f"{row['indications']}", fill="black", font=font) # Indications
            draw.text((30, 370), f"{row['warnings']}", fill="black", font=font) #  Warnings
            
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




    


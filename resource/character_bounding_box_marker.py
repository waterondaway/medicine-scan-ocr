from PIL import Image, ImageDraw, ImageFont
import os, unicodedata, csv

# Config parameter values
font_size = 40
width, height = 100, 100
background_color = "white"
text_color = "black"

# Config the specific directory
font_directory = "../assets/fonts/"
output_directory = "../assets/template/"
file_path = "../data/drug_labels.csv"

def init_draw(fonts):
    img = Image.new("RGB", (720, 480), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_directory + "/" + fonts, font_size) 
    return img, draw, font

def save_image(img, filename):
    save_path = os.path.join(output_directory, f"template_image_bounding_box_marker.png") # Specific filename
    img.save(save_path)

def draw_text_with_red_dots(draw, text, position, font):
    x, y = position
    for char in text:
        bbox = draw.textbbox((x, y), char, font=font) # (left, top, right, bottom)
        left, top, right, bottom = bbox[0], bbox[1], bbox[2], bbox[3]
        print(left, top, right, bottom)
        char_width = right - left
        char_height = bottom - top
        center_x = left + char_width / 2
        center_y = top + char_height / 2
        
        if char != " " and char != "-":
            draw.text((x, y), char, fill=text_color, font=font)
        if char != " " and char != "-":
            draw.rectangle([left, top, right, bottom], fill=None, outline="red", width=1) # [initial x-axis, initial y-axis, ending x-axis, ending y-axis]
        if unicodedata.category(char) not in ['Mn', 'Mc']:
            x += char_width


def make_medicine_label(fonts, filename):
    count = 0
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            img, draw, font = init_draw(fonts)
            # Draw a text
            draw_text_with_red_dots(draw, f"ชื่อ {row['patient_name']}", (30, 40), font)  # Patient Name
            draw_text_with_red_dots(draw, f"บัตรประจำตัว {row['patient_id']}", (30, 90), font)  # Patient ID
            draw_text_with_red_dots(draw, f"วันเกิด {row['patient_birthdate']}", (30, 140), font)  # Birthdate
            draw_text_with_red_dots(draw, f"{row['drug_reg_no']}", (420, 40), font)  # Drug Reg. No.
            draw_text_with_red_dots(draw, f"วันผลิต {row['mfg_date']}", (420, 90), font)  # MFG Date
            draw_text_with_red_dots(draw, f"วันหมดอายุ {row['exp_date']}", (420, 140), font)  # EXP Date
            draw_text_with_red_dots(draw, f"{'-'*300}", (0, 180), font)  # Line (for separation)
            draw_text_with_red_dots(draw, f"{(row['drug_name']).upper()}", (30, 220), font)  # Drug Name
            draw_text_with_red_dots(draw, f"{row['dosage']}", (250, 220), font)  # Dosage
            draw_text_with_red_dots(draw, f"{row['form'].upper()}", (400, 220), font)  # Form
            draw_text_with_red_dots(draw, f"{row['usage_instructions']}", (30, 270), font)  # Usage Instructions
            draw_text_with_red_dots(draw, f"{row['indications']}", (30, 320), font)  # Indications
            draw_text_with_red_dots(draw, f"{row['warnings']}", (30, 370), font)  # Warnings
            save_image(img, filename)
            print(f"Finish save to assets/template/template_image_bounding_box_marker.png")
            count = count + 1


make_medicine_label("ANGSA.ttf", None)
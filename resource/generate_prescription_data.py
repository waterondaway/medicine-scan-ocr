import random
import pandas as pd
from faker import Faker
from datetime import datetime

fake = Faker("th_TH")

drugs = [
    {"name": "Paracetamol", "dosage": "500mg", "form": "tablet", "reg_no": "REG001"},
    {"name": "Ibuprofen", "dosage": "400mg", "form": "capsule", "reg_no": "REG002"},
    {"name": "Amoxicillin", "dosage": "250mg", "form": "syrup", "reg_no": "REG003"},
    {"name": "Ciprofloxacin", "dosage": "500mg", "form": "tablet", "reg_no": "REG004"},
    {"name": "Loratadine", "dosage": "10mg", "form": "tablet", "reg_no": "REG005"},
    {"name": "Diclofenac", "dosage": "50mg", "form": "tablet", "reg_no": "REG006"},
    {"name": "Omeprazole", "dosage": "20mg", "form": "capsule", "reg_no": "REG007"},
    {"name": "Metformin", "dosage": "500mg", "form": "tablet", "reg_no": "REG008"},
    {"name": "Cetirizine", "dosage": "10mg", "form": "tablet", "reg_no": "REG009"},
    {"name": "Azithromycin", "dosage": "250mg", "form": "tablet", "reg_no": "REG010"},
    {"name": "Prednisolone", "dosage": "5mg", "form": "tablet", "reg_no": "REG011"},
    {"name": "Doxycycline", "dosage": "100mg", "form": "capsule", "reg_no": "REG012"},
    {"name": "Fluconazole", "dosage": "150mg", "form": "tablet", "reg_no": "REG013"},
    {"name": "Clarithromycin", "dosage": "250mg", "form": "tablet", "reg_no": "REG014"},
    {"name": "Losartan", "dosage": "50mg", "form": "tablet", "reg_no": "REG015"},
]

warnings = [
    "ห้ามเกินขนาดที่แนะนำ",
    "อาจทำให้ง่วงซึม ควรหลีกเลี่ยงการขับขี่ยานพาหนะ",
    "ควรรับประทานพร้อมอาหารเพื่อหลีกเลี่ยงอาการคลื่นไส้",
    "ห้ามใช้ในผู้ที่แพ้ส่วนประกอบของยา",
    "ควรปรึกษาแพทย์ก่อนใช้ในผู้ป่วยที่มีโรคประจำตัว",
    "ห้ามใช้ยาเกิน 7 วันโดยไม่ปรึกษาแพทย์",
    "หลีกเลี่ยงการใช้ร่วมกับแอลกอฮอล์",
    "ควรหยุดยาและปรึกษาแพทย์หากมีอาการแพ้",
    "อาจเพิ่มความเสี่ยงต่ออาการหัวใจเต้นผิดจังหวะ",
    "ควรเก็บยาให้พ้นมือเด็ก"
]

indications = [
    "บรรเทาอาการปวดจากระดับเบาถึงปานกลาง",
    "บรรเทาอาการอักเสบและปวดตามข้อ",
    "รักษาการติดเชื้อระบบทางเดินหายใจ",
    "บรรเทาอาการแพ้และอาการคัน",
    "รักษาการติดเชื้อระบบทางเดินปัสสาวะ",
    "ลดไข้ในผู้ป่วยที่มีไข้สูง",
    "รักษาอาการคัดจมูกและภูมิแพ้",
    "ช่วยลดอาการปวดศีรษะและไมเกรน",
    "รักษาอาการกรดไหลย้อนและแผลในกระเพาะอาหาร",
    "บรรเทาอาการไอและเจ็บคอ"
]

usage_instructions = [
    "รับประทานวันละ 1 เม็ดทุก 6 ชั่วโมงเมื่อจำเป็น",
    "รับประทานวันละ 1 แคปซูลทุก 8 ชั่วโมงพร้อมน้ำ",
    "เขย่าขวดก่อนใช้ รับประทาน 5 มล. ทุก 12 ชั่วโมง",
    "รับประทานวันละ 1 เม็ดหลังอาหาร",
    "รับประทานวันละ 2 เม็ดก่อนนอน",
    "รับประทานวันละ 1 แคปซูลหลังมื้ออาหารเช้า",
    "ใช้เฉพาะเมื่อมีอาการเท่านั้น ไม่เกิน 4 ครั้งต่อวัน",
    "หยด 2-3 หยดในตาข้างที่มีอาการ วันละ 2 ครั้ง",
    "รับประทานยาก่อนอาหาร 30 นาที วันละ 1 ครั้ง",
    "ทาวันละ 2 ครั้ง เช้า-เย็น"
]


def format_thai_date(date):
    thai_months = [
        "มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", 
        "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", 
        "พฤศจิกายน", "ธันวาคม"
    ]
    day = date.day
    month = thai_months[date.month - 1]
    year = date.year + 543
    return f"{day} {month} {year}"


records = []
for _ in range(100): 
    patient_name = fake.name()
    patient_id = fake.random_int(min=1000000000000, max=9999999999999)
    patient_birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
    thai_birthdate = format_thai_date(patient_birthdate) 
    drug = random.choice(drugs)
    mfg_date = fake.date_between(start_date="-1y", end_date="today")
    exp_date = fake.date_between(start_date="+1y", end_date="+3y")
    record = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "patient_birthdate": thai_birthdate, 
        "drug_name": drug["name"],
        "dosage": drug["dosage"],
        "form": drug["form"], 
        "drug_reg_no": drug["reg_no"],
        "mfg_date": mfg_date,
        "exp_date": exp_date,
        "warnings": random.choice(warnings),
        "indications": random.choice(indications),
        "usage_instructions": random.choice(usage_instructions)
    }
    records.append(record)


df = pd.DataFrame(records)
df.to_csv("drug_labels.csv", index=False, encoding="utf-8-sig")

print("finish work : drug_labels.csv")

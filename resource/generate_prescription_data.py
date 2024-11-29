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
    {"name": "Aspirin", "dosage": "300mg", "form": "tablet", "reg_no": "REG016"},
    {"name": "Lorazepam", "dosage": "2mg", "form": "tablet", "reg_no": "REG017"},
    {"name": "Tamsulosin", "dosage": "0.4mg", "form": "capsule", "reg_no": "REG018"},
    {"name": "Atorvastatin", "dosage": "20mg", "form": "tablet", "reg_no": "REG019"},
    {"name": "Simvastatin", "dosage": "40mg", "form": "tablet", "reg_no": "REG020"},
    {"name": "Furosemide", "dosage": "40mg", "form": "tablet", "reg_no": "REG021"},
    {"name": "Clopidogrel", "dosage": "75mg", "form": "tablet", "reg_no": "REG022"},
    {"name": "Erythromycin", "dosage": "500mg", "form": "tablet", "reg_no": "REG023"},
    {"name": "Diazepam", "dosage": "10mg", "form": "tablet", "reg_no": "REG024"},
    {"name": "Warfarin", "dosage": "5mg", "form": "tablet", "reg_no": "REG025"},
    {"name": "Lisinopril", "dosage": "20mg", "form": "tablet", "reg_no": "REG026"},
    {"name": "Amlodipine", "dosage": "5mg", "form": "tablet", "reg_no": "REG027"},
    {"name": "Prednisone", "dosage": "10mg", "form": "tablet", "reg_no": "REG028"},
    {"name": "Hydrochlorothiazide", "dosage": "25mg", "form": "tablet", "reg_no": "REG029"},
    {"name": "Benzonatate", "dosage": "100mg", "form": "capsule", "reg_no": "REG030"}
]

warnings = [
    "ห้ามเกินขนาดที่แนะนำ",
    "อาจทำให้ง่วงซึม",
    "ควรรับประทานพร้อมอาหาร",
    "ห้ามใช้ในผู้ที่แพ้ยา",
    "ปรึกษาแพทย์หากมีโรคประจำตัว",
    "หลีกเลี่ยงการใช้ร่วมกับแอลกอฮอล์",
    "ควรหยุดยาและปรึกษาแพทย์หากมีอาการแพ้",
    "ห้ามใช้ในผู้มีโรคหัวใจ",
    "ควรเก็บยาให้พ้นมือเด็ก",
    "ห้ามใช้เกิน 7 วัน",
    "ไม่ควรใช้ในผู้ที่มีโรคตับ",
    "ห้ามใช้ในหญิงตั้งครรภ์",
    "ควรหลีกเลี่ยงการดื่มแอลกอฮอล์",
    "หากมีอาการเวียนศีรษะ ควรหยุดยา",
    "ห้ามใช้ในผู้ที่มีประวัติการแพ้ยา",
    "การใช้ยาเกินขนาดอาจทำให้เกิดภาวะพิษ",
    "ไม่ควรใช้ในผู้สูงอายุที่มีโรคประจำตัว",
    "หากมีอาการท้องเสีย ควรหยุดยา",
    "ห้ามใช้ในเด็กอายุต่ำกว่า 2 ปี",
    "ควรใช้ตามคำแนะนำของแพทย์",
    "หากมีอาการหายใจลำบาก ควรหยุดยา",
    "ควรหลีกเลี่ยงการทำงานที่ต้องการความตื่นตัว",
    "ควรหยุดยาและพบแพทย์หากมีผื่น",
    "ห้ามใช้ในผู้ที่มีปัญหากับระบบทางเดินอาหาร",
    "การใช้ยาเกินขนาดอาจทำให้เกิดอาการแทรกซ้อน",
    "หากยาไม่ได้ผลภายใน 3 วัน ควรปรึกษาแพทย์",
    "หลีกเลี่ยงการใช้ร่วมกับยาตัวอื่นๆ",
    "ควรใช้ยาในปริมาณที่ถูกต้อง",
    "หากมีอาการมึนงง ควรหยุดยาและปรึกษาแพทย์"
]

indications = [
    "บรรเทาอาการปวดเบา",
    "บรรเทาอาการอักเสบ",
    "รักษาการติดเชื้อหายใจ",
    "บรรเทาอาการแพ้",
    "รักษาการติดเชื้อปัสสาวะ",
    "ลดไข้ในผู้ป่วยไข้สูง",
    "รักษาคัดจมูก",
    "ช่วยลดปวดหัวไมเกรน",
    "รักษาอาการกรดไหลย้อน",
    "บรรเทาอาการไอเจ็บคอ",
    "บรรเทาอาการปวดหลัง",
    "ช่วยรักษาผื่นภูมิแพ้",
    "รักษาการติดเชื้อผิวหนัง",
    "รักษาท้องร่วงจากแบคทีเรีย",
    "รักษาผลกระทบจากการผ่าตัด",
    "บรรเทาอาการข้ออักเสบ",
    "ลดอาการบวมจากการบาดเจ็บ",
    "บรรเทาอาการหืดหอบ",
    "ลดน้ำตาลในเลือด",
    "รักษาภาวะกรดไหลย้อน",
    "รักษาผลข้างเคียงจากการแพ้สารเคมี",
    "รักษาภาวะติดเชื้อผิวหนัง",
    "ลดอาการเจ็บปวดหลังผ่าตัด",
    "บรรเทาอาการเมาค้าง",
    "บรรเทาอาการจากการติดเชื้อทางเดินอาหาร",
    "ช่วยฟื้นฟูหลังการรักษามะเร็ง",
    "รักษาอาการแพ้ฝุ่นและสารก่อภูมิแพ้",
    "ลดความเสี่ยงจากภาวะหลอดเลือดตีบ",
    "ช่วยฟื้นฟูหลังการออกกำลังกาย",
    "ลดอาการจุกเสียดจากแผลในกระเพาะ"
]

usage_instructions = [
    "รับประทานวันละ 1 เม็ดทุก 6 ชั่วโมง",
    "รับประทานวันละ 1 แคปซูลทุก 8 ชั่วโมง",
    "เขย่าขวดก่อนใช้ รับประทาน 5 มล. ทุก 12 ชั่วโมง",
    "รับประทานวันละ 1 เม็ดหลังอาหาร",
    "รับประทาน 2 เม็ดก่อนนอน",
    "รับประทาน 1 แคปซูลหลังอาหารเช้า",
    "ใช้เฉพาะเมื่อมีอาการ",
    "หยด 2-3 หยดในตา วันละ 2 ครั้ง",
    "รับประทานก่อนอาหาร 30 นาที",
    "ทาวันละ 2 ครั้ง เช้า-เย็น",
    "รับประทานวันละ 1 เม็ดหลังมื้อกลางวัน",
    "รับประทาน 1 แคปซูลทุก 6 ชั่วโมง",
    "เขย่าขวดให้เข้ากันก่อนทุกครั้ง",
    "ใช้เจลทาบริเวณที่มีอาการ วันละ 3 ครั้ง",
    "หยด 1-2 หยดในจมูกวันละ 3 ครั้ง",
    "รับประทานยาท้องว่างก่อนอาหาร 30 นาที",
    "รับประทานวันละ 1 เม็ดก่อนนอน",
    "รับประทานยาพร้อมน้ำมาก ๆ",
    "หยด 1 หยดใต้ลิ้นวันละ 2 ครั้ง",
    "รับประทานวันละ 2 เม็ดเช้า-เย็น",
    "รับประทาน 1 แคปซูลก่อนนอน",
    "ใช้ยาทาเพียงบางๆ นวดเบาๆ วันละ 1-2 ครั้ง",
    "รับประทานยานี้หลังทานอาหารทันที",
    "ใช้เฉพาะเมื่ออาการไม่หายควรปรึกษาแพทย์",
    "ทาบริเวณที่มีอาการวันละ 2 ครั้ง",
    "หยดยาลงในน้ำดื่มวันละ 3 ครั้ง",
    "ทาบริเวณที่มีอาการแล้วล้างมือหลังใช้",
    "รับประทานเมื่อมีอาการปวด ไม่เกิน 3 วัน",
    "รับประทานวันละ 3 ครั้งหลังมื้ออาหารใหญ่",
    "ใช้ทาในเวลากลางคืนก่อนนอน"
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
    mfg_date = fake.date_between(start_date="-1y", end_date="today")
    exp_date = fake.date_between(start_date="+1y", end_date="+3y")
    record = {
        "patient_name": patient_name,
        "patient_id": patient_id,
        "patient_birthdate": thai_birthdate, 
        "drug_name": random.choice(drugs)["name"],
        "dosage": random.choice(drugs)["dosage"],
        "form": random.choice(drugs)["form"], 
        "drug_reg_no": random.choice(drugs)["reg_no"],
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

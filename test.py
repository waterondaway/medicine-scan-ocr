import openai

# ใส่ API Key ของคุณที่นี่
openai.api_key = ''

try:
    # ใช้ Chat API สำหรับโมเดลแบบสนทนา (เช่น gpt-3.5-turbo, gpt-4)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # หรือ gpt-4 หรือโมเดลอื่นๆ
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "สวัสดีครับ, คุณช่วยตอบคำถามได้ไหม?"}
        ]
    )

    # แสดงข้อความที่โมเดลตอบกลับ
    print("ข้อความจาก ChatGPT:", response['choices'][0]['message']['content'])

except openai.OpenAIError as e:
    print(f"เกิดข้อผิดพลาดในการเชื่อมต่อกับ OpenAI API: {e}")
except Exception as e:
    print(f"เกิดข้อผิดพลาดอื่นๆ: {e}")

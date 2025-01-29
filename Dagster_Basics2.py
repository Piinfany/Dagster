# Install Dagster and Dagit on your machine and verify the installation.
# การติดตั้ง Dagster และ Dagit บนเครื่อง

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Dagster_Basics2.py
# touch Dagster_Basics2.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

from dagster import op,job

@op
def hello_basics2():
    return "Dagster!"

@op
def goodbye_basics2(name: str):
    print(f"Goodbye, {name}!")

@job
def hello_dagster2():
    goodbye_basics2(hello_basics2())

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Dagster_Basics2.py

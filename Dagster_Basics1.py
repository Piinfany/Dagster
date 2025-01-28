# Install Dagster and Dagit on your machine and verify the installation.
# การติดตั้ง Dagster และ Dagit บนเครื่อง

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Dagster_Basics1.py
# touch Dagster_Basics1.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Dagster_Basics1.py
# สร้าง Pipeline
# โค้ดนี้เป็นการสร้าง Pipeline ที่มี 2 Solids คือ hello_basics Solid และ goodbye_basics Solid

from dagster import job, op

# สร้าง Solids โดยใช้ Decorator @op 
@op
def hello_basics(): # สร้าง Solid ชื่อ hello_basics ที่ไม่มี Input
    return "Dagster!" # ส่งค่ากลับเป็น Dagster!


@op 
def goodbye_basics(name: str): # สร้าง Solid ชื่อ goodbye_basics ที่มี Input ชื่อ name โดยมี Type เป็น str
    print(f"Goodbye, {name}!") # แสดงข้อความ Goodbye, ตามด้วยค่าของ name ที่รับมา


@job
def hello_dagster(): # สร้าง Job ชื่อ hello_dagster
    goodbye_basics(hello_basics()) # เรียกใช้งาน Solid goodbye_basics โดยส่งค่าจาก Solid hello_basics ไปเป็น Input ของ Solid goodbye_basics


# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Dagster_Basics1.py

# หลังจากเปิด Dagit ให้เปิด Browser และเข้าไปที่ URL ดังนี้
# http://127.0.0.1:52569






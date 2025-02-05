# Write a pipeline that processes a list of numbers and calculates their sum.

# Install Dagster and Dagit on your machine and verify the installation.
# การติดตั้ง Dagster และ Dagit บนเครื่อง

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Ops_and_Jobs3.py
# touch Ops_and_Jobs3.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Ops_and_Jobs3.py
# สร้าง Pipeline
from dagster import op, job, Field

@op(config_schema={"numbers": Field(list, default_value=[1, 2, 3, 4, 5])})
def sum_number(context):
    # เข้าถึงค่า config จาก context.op_config
    numbers = context.op_config["numbers"]
    total = sum(numbers)
    print(f"Sum of the numbers is: {total}")
    return total # คืนค่า total

@job
def sum_total():
    sum_number()

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Ops_and_Jobs3.py
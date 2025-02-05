# Add input validation to the doubling op to handle non-numeric inputs.

# Install Dagster and Dagit on your machine and verify the installation.
# การติดตั้ง Dagster และ Dagit บนเครื่อง

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Ops_and_Jobs2.py
# touch Ops_and_Jobs2.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Ops_and_Jobs1.py
# สร้าง Pipeline
from dagster import op, job, Field
import random  

@op(config_schema={"min": Field(int, default_value=1), "max": Field(int, default_value=100)})
def random_num(context):
    # เข้าถึงค่า config จาก context.op_config
    min_num = context.op_config["min"]
    max_num = context.op_config["max"]
    rand_num = random.randint(min_num, max_num) 
    print(f"Random Number : {rand_num}")
    # แสดงข้อความใน log
    context.log.info(f"Random Number : {rand_num}")
    return rand_num

@op
def double_num(context,number:int):
    if not isinstance(number, (int, float)): # ก่อนจะ arg จะตรวจสอบว่าถ้า number ไม่ใช่จำนวนเต็มหรือทศนิยม
        context.log.error(f"Invalid input: {number} is not a valid number.") # บันทึก log error
        raise ValueError(f"Expected a numeric value, but got {type(number).__name__}.") # และยกข้อความนี้มา
    
    try: # ตรวจสอบข้อผิดพลาดระหว่างการคูณ
        double_number = number * 2
        print(f"Double Number : {double_number}") 
        context.log.info(f"Double Number : {double_number}")
        return double_number
    except Exception as e:
        context.log.error(f"Error in doubling the number: {str(e)}")
        raise
        

@job
def result_number():
    double_num(random_num())

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Ops_and_Jobs2.py
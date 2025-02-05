# Create an op that reads a configuration value and prints it.

# Install Dagster and Dagit on your machine and verify the installation.
# การติดตั้ง Dagster และ Dagit บนเครื่อง

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Configuring_Ops_and_Jobs1.py
# touch Configuring_Ops_and_Jobs1.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Configuring_Ops_and_Jobs1.py
# สร้าง Pipeline
from dagster import op, job, Field, String

@op(config_schema={"str": Field(String, default_value="Hello, Dagster!")})
def get_name(context):
     # เข้าถึงค่า config จาก context.op_config
     str_value = context.op_config["str"]
     # แสดงข้อความใน log
     context.log.info(f"Message from config: {str_value}")
     print(f"Message from config: {str_value}")
     return str_value

@job
def geeting():
     get_name()

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs1.py
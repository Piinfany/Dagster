# Build a pipeline that accepts user input via configuration for a greeting message.

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Configuring_Ops_and_Jobs3.py
# touch Configuring_Ops_and_Jobs3.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Configuring_Ops_and_Jobs3.py
# สร้าง Pipeline
import json
import sys
from dagster import op, job, resource


# Resource สำหรับดึงการตั้งค่าจากไฟล์ JSON หรือจาก Argument
@resource
def config_resource(context):
    # ตรวจสอบว่าได้รับค่าผ่าน command-line argument หรือไม่
    if len(sys.argv) > 1:
        # ใช้ค่าที่ผู้ใช้ป้อนจาก command line
        message = sys.argv[1]
        context.log.info(f"รับข้อความจาก argument: {message}")
        return {"message": message}
    
    # ถ้าไม่มี argument ให้ดึงค่าจากไฟล์ config.json
    context.log.info("กำลังอ่านการตั้งค่าจาก 'config.json'")
    with open('config.json', 'r') as file:
        config = json.load(file)
    context.log.info("อ่านการตั้งค่าเรียบร้อยแล้ว")
    return config

# Operation ที่ใช้สำหรับแสดงข้อความจากการตั้งค่า
@op(required_resource_keys={'config'})
def print_config(context):
    context.log.info("กำลังเริ่มต้นการทำงานของ print_config...")

    # ดึงข้อมูลการตั้งค่าจาก resource ชื่อว่า config
    config = context.resources.config

    # ดึงค่าของ message ถ้าไม่พบให้แสดงข้อความว่า "ไม่พบข้อความ"
    message = config.get("message", "ไม่พบข้อความ")

    context.log.info(f"ข้อความจากการตั้งค่า: {message}")
    print(message)

    context.log.info("การทำงานของ print_config เสร็จสิ้น.")

# Job ที่เชื่อมต่อ resource และ operation เข้าด้วยกัน
@job(resource_defs={'config': config_resource})
def config_job():
    print_config()

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs3.py



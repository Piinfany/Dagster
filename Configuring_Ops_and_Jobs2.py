# Write a job that uses a configuration file to decide which op to run.
# สร้าง Dagster Job ที่ใช้ไฟล์คอนฟิกูเรชันเพื่อกำหนดว่าให้รัน Operation (หรือ op) ตัวไหน โดยใช้ภาษา Python ในการพัฒนา

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Configuring_Ops_and_Jobs2.py
# touch Configuring_Ops_and_Jobs2.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Configuring_Ops_and_Jobs2.py
# สร้าง Pipeline
from dagster import op, job, resource
import json

# Resource ใช้ในการดึงข้อมูลการตั้งค่าจากแหล่งต่าง ๆ
@resource
def config_resource(context):
    context.log.info("Reading configuration from 'config2.json'")
    with open('config2.json', 'r') as file:
        config = json.load(file)
    context.log.info("Configuration read successfully")
    return config

# Op 1: พิมพ์ข้อความจากการตั้งค่า
@op(required_resource_keys={'config'}) 
def print_config(context):
    context.log.info("Starting the print_config operation...")
    config = context.resources.config
    message = config.get("message", "No message found.")
    context.log.info(f"Configuration message: {message}")
    print(message)
    context.log.info("print_config operation completed.")

# Op 2: แสดงข้อความอีกตัวหนึ่ง
@op(required_resource_keys={'config'})
def other_op(context):
    context.log.info("Starting the other_op operation...")
    config = context.resources.config
    another_message = config.get("another_message", "No other message found.")
    context.log.info(f"Other configuration message: {another_message}")
    print(another_message)
    context.log.info("other_op operation completed.")

# สร้าง job ที่จะอ่าน operations จากไฟล์ config.json และรันการดำเนินการที่กำหนด
@job(resource_defs={'config': config_resource})
def config_job(context):
    config = context.resources.config  # ดึงข้อมูลการตั้งค่าจาก resource
    operations_to_run = config.get('operations', [])  # อ่านรายชื่อ operations ที่ต้องรันจาก config.json

    # ใช้ for loop ถ้ามีหลาย operation
    for operation in operations_to_run:
        if operation == 'print_config':
            print_config(context)
        elif operation == 'other_op':
            other_op(context)
        # คุณสามารถเพิ่ม op อื่น ๆ ที่จะรันได้ในลักษณะเดียวกัน

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs2.py
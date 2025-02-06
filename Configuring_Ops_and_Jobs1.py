# Create an op that reads a configuration value and prints it.

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
from dagster import op, job, resource
import json

# resource >> ใช้ในการดึงข้อมูลการตั้งค่าจากแหล่งต่าง ๆ
@resource
def config_resource(context):
    context.log.info("Reading configuration from 'config.json'")  # ใช้บันทึกข้อความที่เป็นข้อมูลทั่วไป
    with open('config.json', 'r') as file: # เปิด file
        config = json.load(file) # โหลดข้อมูลที่เป็น JSON เข้าในตัวแปร config แล้วส่งกลับมาเป็นผลลัพธ์
    context.log.info("Configuration read successfully")  # ใช้บันทึกข้อความที่เป็นข้อมูลทั่วไป
    return config

# Op นี้ต้องการ resource ที่ชื่อว่า config
@op(required_resource_keys={'config'}) 
def print_config(context):
    # ใช้บันทึกข้อความที่เป็นข้อมูลทั่วไป
    context.log.info("Starting the print_config operation...")
    
    # ดึงข้อมูลจาก resource ที่ชื่อว่า config
    config = context.resources.config

    # ดึงค่าของ message ถ้าไม่มีให้แสดงข้อความว่า "No message found."
    message = config.get("message", "No message found.")
    
    # ใช้บันทึกข้อความที่เป็นข้อมูลทั่วไป
    context.log.info(f"Configuration message: {message}")
    
    # แสดงค่าของ message ที่ได้
    print(message)
    
    # ใช้บันทึกข้อความที่เป็นข้อมูลทั่วไป
    context.log.info("print_config operation completed.")

# สร้าง job ซึ่งจะใช้ resource ที่ชื่อว่า config_resource ในการดึงข้อมูลการตั้งค่า
@job(resource_defs={'config': config_resource})
def config_job():
    print_config()

# Run the job
if __name__ == "__main__":
    config_job.execute_in_process()

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs1.py
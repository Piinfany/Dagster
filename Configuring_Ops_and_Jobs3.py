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
from dagster import op, job, resource, Field

# resource >> ใช้ในการดึงข้อมูลการตั้งค่าจากแหล่งต่าง ๆ
@resource(config_schema={"message": Field(str, default_value="Hello Dagster!!")})
def config_resource(context):
    # ดึง configuration จาก run_config ที่กำหนดใน UI
    config = context.resource_config
    context.log.info(f"Configuration received: {config}")  # บันทึกข้อความใน logs ของ UI
    return config

# Op นี้ต้องการ resource ที่ชื่อว่า config
@op(required_resource_keys={'config'})
def print_config(context):
    context.log.info("Starting the print_config operation...")
    
    # ดึงข้อมูลจาก resource ที่ชื่อว่า config
    config = context.resources.config

    # ดึงค่าของ message ถ้าไม่มีให้แสดงข้อความว่า "No message found."
    message = config.get("message", "No message found.")
    
    context.log.info(f"Configuration message: {message}")
    
    print(message)
    
    context.log.info("print_config operation completed.")

# สร้าง job ซึ่งจะใช้ resource ที่ชื่อว่า config_resource ในการดึงข้อมูลการตั้งค่า
@job(resource_defs={'config': config_resource})
def config_job():
    print_config()

# python3 Configuring_Ops_and_Jobs3.py

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs3.py



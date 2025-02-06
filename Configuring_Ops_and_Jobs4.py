# Modify the pipeline to validate and handle missing configuration parameters.

# สร้าง Virtual Environment(สิ่งแวดล้อมเสมือน) ชื่อ dagster-env เพื่อป้องกันการแยกการทำงานของโปรแกรมที่ต่างกัน
# python3 -m venv dagster-env

# เปิด Virtual Environment >> เห็นว่ามีชื่อ dagster-env ข้างหน้า $ แสดงว่าเปิด Virtual Environment อยู่
# source dagster-env/bin/activate

# สร้างไฟล์ Python ชื่อ Configuring_Ops_and_Jobs4.py
# touch Configuring_Ops_and_Jobs4.py

# ติดตั้ง Dagster
# pip install dagster

# ติดตั้ง Dagit
# pip install dagit

# ติดตั้ง Dagster และ Dagit ใน Virtual Environment ชื่อ dagster-env
# dagster-daemon run
# dagster-daemon start

# ทดสอบการติดตั้ง Dagster และ Dagit
# dagit

# นำโค้ดด้านล่างไปใส่ในไฟล์ Configuring_Ops_and_Jobs4.py
# สร้าง Pipeline

from dagster import op, job, resource
import json

# resource >> ใช้ในการดึงข้อมูลการตั้งค่าจากแหล่งต่าง ๆ
@resource
def config_resource(context):
    context.log.info("กำลังอ่านการตั้งค่าจาก 'config.json'")
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
        
        # ตรวจสอบว่า keys ที่จำเป็นมีครบหรือไม่
        required_keys = ["message"]
        for key in required_keys:
            if key not in config:
                context.log.warning(f"การตั้งค่า '{key}' หายไปในไฟล์ config.json")
        
        context.log.info("การอ่านการตั้งค่าสำเร็จ")
        return config
    
    except FileNotFoundError:
        context.log.error("ไม่พบไฟล์ 'config.json'")
    except json.JSONDecodeError:
        context.log.error("เกิดข้อผิดพลาดในการอ่านไฟล์ config.json")
    except Exception as e:
        context.log.error(f"เกิดข้อผิดพลาด: {e}")

# Op นี้ต้องการ resource ที่ชื่อว่า config
@op(required_resource_keys={'config'}) 
def print_config(context):
    context.log.info("เริ่มการทำงานของ op print_config...")
    
    # ดึงข้อมูลจาก resource ที่ชื่อว่า config
    config = context.resources.config

    # ดึงค่าของ message ถ้าไม่มีให้แสดงข้อความว่า "ไม่พบข้อความ"
    message = config.get("message", "ไม่พบข้อความ")
    
    context.log.info(f"ข้อความจากการตั้งค่า: {message}")
    
    # แสดงค่าของ message ที่ได้
    print(message)
    
    context.log.info("การทำงานของ print_config เสร็จสมบูรณ์")

# สร้าง job ซึ่งจะใช้ resource ที่ชื่อว่า config_resource ในการดึงข้อมูลการตั้งค่า
@job(resource_defs={'config': config_resource})
def config_job():
    print_config()

# python3 Configuring_Ops_and_Jobs4.py

# ทดสอบการสร้าง Pipeline โดยใช้ Dagit
# ใช้คำสั่งใน Terminal ดังนี้
# dagit -f Configuring_Ops_and_Jobs4.py
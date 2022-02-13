from faulthandler import enable
from kafka import KafkaConsumer
import mysql.connector
import json

def populate_student_data(record):
    insert_stmt = ("INSERT INTO students "
               "(name, address, email, created_at) "
               "VALUES (%s, %s, %s, %s)")
    student_data = tuple(json.loads(msg.value).values())
    cursor.execute(insert_stmt, student_data)
    conn.commit()

if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="password",
            database="kafka_feed"
        )
    except mysql.connector.Error as e:
        print("Oh something went wrong {}".format(e))   

    print(conn.is_connected())
    cursor = conn.cursor()

    consumer =  KafkaConsumer('student_data', group_id = 'student_group_1', 
        bootstrap_servers=['localhost:9092'], auto_offset_reset ='earliest',
        enable_auto_commit = False)
    print('Consumer Starting....')
    for msg in consumer:
        populate_student_data(json.loads(msg.value))



import json
from kafka import KafkaProducer
from fake import get_students_data
import time 

def json_serialize(data):
    return json.dumps(data).encode("utf-8")

def get_partitions(key, all, available):
    return 0

# partition = get_partitions will 
# ensure all message will go to partion 0, 
# it is optional and can be removed if message need to distributes to all partitions randomly

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'], 
    value_serializer = json_serialize)

if __name__ == "__main__":
    counter = 0
    while counter < 20:
        student = get_students_data()
        print(student)
        producer.send(topic="student_data", value=student)
        time.sleep(5)
        counter += 1



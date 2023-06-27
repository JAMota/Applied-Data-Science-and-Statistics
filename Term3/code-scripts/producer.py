from time import sleep
from confluent_kafka import Producer
import time

def send_line_to_topic(line, topic, producer):
    # Create message headers
    headers = [
        ('producer_timestamp', str(time.time()).encode('utf-8')),  # Store producer timestamp
        ('topic_entry_timestamp', str(time.time()).encode('utf-8')),  # Store topic entry timestamp
        ('consumer_timestamp', str(time.time()).encode('utf-8')),  # Store consumer timestamp
        # Add additional headers as needed
    ]

    producer.produce(topic, line.encode('utf-8'), headers=headers)
    producer.flush()


def read_file_and_send_to_kafka(file_path, topic, bootstrap_servers):
    conf = {'bootstrap.servers': bootstrap_servers}
    producer = Producer(conf)

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            send_line_to_topic(line, topic, producer)
            sleep(1)  # Wait for 1 second before sending the next line

    producer.flush()
    producer.close()


# Usage example
file_path =  "b1.txt" #'path/to/your/file.txt'
topic = 'heart-data'  # 'your-kafka-topic'
bootstrap_servers = '10.0.0.4:9092'

read_file_and_send_to_kafka(file_path, topic, bootstrap_servers)


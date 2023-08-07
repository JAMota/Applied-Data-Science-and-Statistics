from time import sleep, time
from confluent_kafka import Producer

def send_line_to_topic(line, topic, producer, producer_entry_timestamp):
    # Create message headers
    headers = [
        ('producer_entry_timestamp', producer_entry_timestamp),
        # Add additional headers as needed
    ]

    # Capture message_sent_timestamp just before sending the message
    producer_sent_timestamp = str(time()).encode('utf-8')
    headers.append(('producer_sent_timestamp', producer_sent_timestamp))

    producer.produce(topic, line.encode('utf-8'), headers=headers)
    producer.flush()

def read_file_and_send_to_kafka(file_path, topic, bootstrap_servers):
    conf = {'bootstrap.servers': bootstrap_servers}
    producer = Producer(conf)

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            producer_entry_timestamp = str(time()).encode('utf-8')  # Store producer entry timestamp
            send_line_to_topic(line, topic, producer, producer_entry_timestamp)
            sleep(1)  # Wait for 1 second before sending the next line

    producer.flush()
    producer.close()

# Usage example
file_path = "heartData.txt"
topic = 'heart-data'
bootstrap_servers = '10.0.0.4:9092'

read_file_and_send_to_kafka(file_path, topic, bootstrap_servers)


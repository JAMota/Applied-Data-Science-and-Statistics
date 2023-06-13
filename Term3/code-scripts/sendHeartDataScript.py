# -*- coding: utf-8 -*-
"""
@author: AndreMota
"""

from time import sleep
from confluent_kafka import Producer


def send_line_to_topic(line, topic, producer):
    producer.produce(topic, line.encode('utf-8'))
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


# Usage example
file_path = "C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term3/heartData/b1.txt" 
##'path/to/your/file.txt'
topic = 'heart-data'  # 'your-kafka-topic'
bootstrap_servers = 'localhost:9092' 
#'localhost:9092'  # Update with your Kafka broker addresses

read_file_and_send_to_kafka(file_path, topic, bootstrap_servers)
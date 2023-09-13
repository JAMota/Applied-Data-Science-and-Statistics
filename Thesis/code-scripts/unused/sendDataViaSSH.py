# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 01:36:26 2023

@author: AndreMota
"""
import logging
from time import sleep
from sshtunnel import SSHTunnelForwarder
from confluent_kafka import Producer

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_line_to_topic(line, topic, producer):
    try:
        logging.debug("Sending line to Kafka: %s", line)
        producer.produce(topic, line.encode('utf-8'))
        producer.flush()
        logging.debug("Line sent to Kafka: %s", line)
    except Exception as e:
        logging.error("Error while sending line to Kafka: %s", str(e))

def read_file_and_send_to_kafka(file_path, topic, ssh_host, ssh_port, ssh_username, ssh_private_key, kafka_bootstrap_servers):
    try:
        with SSHTunnelForwarder(
                (ssh_host, ssh_port),
                ssh_username=ssh_username,
                ssh_pkey=ssh_private_key,
                remote_bind_address=('localhost', 9092)
        ) as _:
            conf = {'bootstrap.servers': kafka_bootstrap_servers}
            producer = Producer(conf)

            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    send_line_to_topic(line, topic, producer)
                    sleep(1)  # Wait for 1 second before sending the next line

            producer.flush()

    except Exception as e:
        logging.error("Error while reading file and sending data to Kafka: %s", str(e))

# SSH tunnel configuration
ssh_host = '20.90.165.83'
ssh_port = 22  # Default SSH port
ssh_username = 'azureuser'
ssh_private_key = "C:/Users/AndreMota/Downloads/UbuntuApacheKofta_key.pem"

# Kafka configuration
kafka_bootstrap_servers = 'localhost:9092'
topic = 'heart-data'
file_path = "C:/AppliedDataScienceAndStatistics/Applied-Data-Science-and-Statistics/Term3/heartData/b1.txt"

read_file_and_send_to_kafka(file_path, topic, ssh_host, ssh_port, ssh_username, ssh_private_key, kafka_bootstrap_servers)

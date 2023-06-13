# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 01:36:26 2023

@author: AndreMota
"""

from time import sleep
from confluent_kafka import Producer
from sshtunnel import SSHTunnelForwarder

def send_line_to_topic(line, topic, producer):
    producer.produce(topic, line.encode('utf-8'))
    producer.flush()

def read_file_and_send_to_kafka(file_path, topic, ssh_host, ssh_port, ssh_username, ssh_private_key, kafka_bootstrap_servers):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_username,
            ssh_pkey=ssh_private_key,
            remote_bind_address=('localhost', 9092)
    ) as tunnel:
        conf = {'bootstrap.servers': kafka_bootstrap_servers}
        producer = Producer(conf)

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                send_line_to_topic(line, topic, producer)
                sleep(1)  # Wait for 1 second before sending the next line

        producer.flush()

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

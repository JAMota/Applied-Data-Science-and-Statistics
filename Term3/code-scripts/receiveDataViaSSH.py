# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 01:33:14 2023

@author: AndreMota
"""
import logging
import time
from sshtunnel import SSHTunnelForwarder
from confluent_kafka import Consumer

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def consume_from_kafka(topic, ssh_host, ssh_port, ssh_username, ssh_private_key, kafka_bootstrap_servers):
    try:
        with SSHTunnelForwarder(
                (ssh_host, ssh_port),
                ssh_username=ssh_username,
                ssh_pkey=ssh_private_key,
                remote_bind_address=('10.0.0.4', 9092),
                local_bind_address=('localhost', 9092)
        ) as tunnel:
            logging.info("SSH tunnel created. Listening on localhost:9092")

            conf = {
                'bootstrap.servers': kafka_bootstrap_servers,
                'group.id': 'my-consumer-group',
                'auto.offset.reset': 'earliest'
            }
            consumer = Consumer(conf)
            consumer.subscribe([topic])

            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    logging.error("Error while consuming message: %s", msg.error())
                    continue

                logging.debug("Received message: %s", msg.value().decode('utf-8'))

    except Exception as e:
        logging.error("Error while consuming messages from Kafka: %s", str(e))

# SSH tunnel configuration
ssh_host = '20.90.165.83'
ssh_port = 22  # Default SSH port
ssh_username = 'azureuser'
ssh_private_key = "C:/Users/AndreMota/Downloads/UbuntuApacheKofta_key.pem"

# Kafka configuration
kafka_bootstrap_servers = 'localhost:9092'
topic = 'heart-data'

consume_from_kafka(topic, ssh_host, ssh_port, ssh_username, ssh_private_key, kafka_bootstrap_servers)

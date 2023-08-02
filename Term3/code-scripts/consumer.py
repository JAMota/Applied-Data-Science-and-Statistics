import sqlite3
from confluent_kafka import Consumer, KafkaException
import time

conf = {
    'bootstrap.servers': '10.0.0.4:9092', # Update with your Kafka broker's address
    'group.id': 'my-consumer-group-heart-data',  # Specify a unique consumer group ID
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
}

consumer = Consumer(conf)

def consume_messages():
    try:
        consumer.subscribe(['heart-data']) #insert your topic name here
        conn = sqlite3.connect('/opt/sqlite3/heart.db') #insert your database path here
        cursor = conn.cursor()
        timestamp_file = open('timestamps.log', 'a')

        while True:
            msg = consumer.poll(1.0)  
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            
            kafka_entry_timestamp = msg.timestamp()[1]           # kafka_entry_timestamp
            consumer_received_timestamp = str(time.time())    # consumer_received_timestamp

            headers = msg.headers()
            producer_entry_timestamp = None
            producer_sent_timestamp = None

            if headers is not None:
                for header in headers:
                    header_key = header[0]
                    header_value = header[1]
                    
                    if header_key == 'producer_entry_timestamp':
                        producer_entry_timestamp = header_value.decode('utf-8')
                    
                    if header_key == 'producer_sent_timestamp':
                        producer_sent_timestamp = header_value.decode('utf-8')

            if producer_entry_timestamp and producer_sent_timestamp:
                print(f"Producer entry timestamp: {producer_entry_timestamp}")
                print(f"Producer sent timestamp: {producer_sent_timestamp}")

            values = msg.value().decode('utf-8').split()
            values.append(producer_entry_timestamp)
            values.append(producer_sent_timestamp)
            
            database_entry_timestamp = time.time()  # Time before start of DB operation
            
            query = """
            INSERT INTO heart_messages (
                heart_rate, 
                chest_volume, 
                blood_oxygen_concentration, 
                producer_entry_timestamp, 
                producer_sent_timestamp, 
                kafka_entry_timestamp, 
                consumer_received_timestamp, 
                database_entry_timestamp
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (*values, kafka_entry_timestamp, consumer_received_timestamp, database_entry_timestamp))
            conn.commit()
            
            database_finished_timestamp = time.time()  # Time after end of DB operation
            consumer_sent_timestamp = str(time.time())     # consumer_sent_timestamp

            timestamp_file.write(
                f"{producer_entry_timestamp} {producer_sent_timestamp} " \
                f"{kafka_entry_timestamp} {consumer_received_timestamp} " \
                f"{database_entry_timestamp} {database_finished_timestamp} {consumer_sent_timestamp}\n"
            )
            timestamp_file.flush()

            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        conn.close()
        timestamp_file.close()

consume_messages()

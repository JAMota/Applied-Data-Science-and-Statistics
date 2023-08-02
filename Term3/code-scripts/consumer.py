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

        while True:
       

            # Insert the message values and timestamps into the database
            values = msg.value().decode('utf-8').split()
            values.append(producer_entry_timestamp)
            values.append(producer_sent_timestamp)
            values.append(kafka_entry_timestamp)
            values.append(consumer_received_timestamp)
            
            database_entry_timestamp = time.time()  # Time before start of DB operation
            
            query = """
            INSERT INTO messages (
                heart_rate, 
                chest_volume, 
                blood_oxygen_concentration, 
                producer_entry_timestamp, 
                producer_sent_timestamp, 
                kafka_entry_timestamp,
                consumer_received_timestamp,
                database_entry_timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (*values, kafka_entry_timestamp, consumer_received_timestamp, database_entry_timestamp))
            conn.commit()

            database_finished_timestamp = time.time()  # Time after end of DB operation
            consumer_sent_timestamp = time.ctime(time.time())  # New timestamp for consumer_sent_timestamp

            timestamp_file.write(f"{producer_entry_timestamp} {producer_sent_timestamp} {kafka_entry_timestamp} {consumer_received_timestamp} {database_entry_timestamp} {database_finished_timestamp} {consumer_sent_timestamp}\n")
            timestamp_file.flush()

            print(f"Received message: {msg.value().decode('utf-8')}")


    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        conn.close()
        timestamp_file.close()


consume_messages()

import sqlite3
from confluent_kafka import Consumer, KafkaException
import time

conf = {
    'bootstrap.servers': '10.0.0.4:9092',  # Update with your Kafka broker's address
    'group.id': 'my-consumer-group-heart-data',  # Specify a unique consumer group ID
    'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
}

consumer = Consumer(conf)


def consume_messages():
    try:
        consumer.subscribe(['heart-data'])  # Replace 'your-topic' with the topic you want to consume from
        
        # Establish a connection to the SQLite database
        conn = sqlite3.connect('/opt/sqlite3/heart.db')
        cursor = conn.cursor()

        # Open the timestamps.log file in append mode
        timestamp_file = open('timestamps.log', 'a')

        while True:
            msg = consumer.poll(1.0)  # Poll for new messages with a timeout of 1 second
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            # Retrieve headers
            headers = msg.headers()

            # Extract and print custom headers
            producer_timestamp = None
            topic_entry_timestamp = str(time.time())

            if headers is not None:
                for header in headers:
                    header_key = header[0]
                    header_value = header[1]
                    
                    if header_key == 'producer_timestamp':
                        producer_timestamp = header_value.decode('utf-8')

            if producer_timestamp:
                print(f"Producer timestamp: {producer_timestamp}")
                print(f"Topic entry timestamp: {topic_entry_timestamp}")

            # Insert the message values and timestamps into the database
            values = msg.value().decode('utf-8').split()
            values.append(producer_timestamp)
            values.append(topic_entry_timestamp)
            
            query = """
            INSERT INTO messages (heart_rate, chest_volume, blood_oxygen_concentration, producer_timestamp,
                                  topic_entry_timestamp)
            VALUES (?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, values)
            conn.commit()

            # Write the timestamps to the timestamps.log file
            timestamp_file.write(f"{topic_entry_timestamp} {producer_timestamp}\n")
            timestamp_file.flush()

            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        conn.close()
        timestamp_file.close()


consume_messages()

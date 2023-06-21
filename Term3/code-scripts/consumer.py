import sqlite3
from confluent_kafka import Consumer, KafkaException

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
            topic_entry_timestamp = None
            topic_exit_timestamp = None
            consumer_timestamp = None

            for header in headers:
                header_key = header[0]
                header_value = header[1]
                
                if header_key == 'producer_timestamp':
                    producer_timestamp = header_value.decode('utf-8')
                
                if header_key == 'topic_entry_timestamp':
                    topic_entry_timestamp = header_value.decode('utf-8')

                if header_key == 'topic_exit_timestamp':
                    topic_exit_timestamp = header_value.decode('utf-8')

                if header_key == 'consumer_timestamp':
                    consumer_timestamp = header_value.decode('utf-8')

            if producer_timestamp:
                print(f"Producer timestamp: {producer_timestamp}")

            if topic_entry_timestamp:
                print(f"Topic entry timestamp: {topic_entry_timestamp}")

            if topic_exit_timestamp:
                print(f"Topic exit timestamp: {topic_exit_timestamp}")

            if consumer_timestamp:
                print(f"Consumer timestamp: {consumer_timestamp}")

            # Insert the message value and timestamps into the database
            query = "INSERT INTO heart_data (heart_rate, chest_volume, blood_oxygen) VALUES (?, ?, ?)"
            values = msg.value().decode('utf-8').split()
            values.append(producer_timestamp)
            values.append(topic_entry_timestamp)
            values.append(topic_exit_timestamp)
            values.append(consumer_timestamp)
            cursor.execute(query, values)
            conn.commit()

            print(f"Received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        conn.close()


consume_messages()

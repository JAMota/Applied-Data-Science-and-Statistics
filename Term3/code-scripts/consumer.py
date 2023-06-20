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
        while True:
            msg = consumer.poll(1.0)  # Poll for new messages with a timeout of 1 second
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


consume_messages()
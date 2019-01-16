from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import time

KAFKA_TOPIC = 'url'

def create_kafka_consumer():
    print('Connecting to kafka broker...')
    while True:
        try:
            consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers='kafka:9092')
            break
        except NoBrokersAvailable:
            print('Failed to create consumer, kafka broker is not yet available. Retrying in 10 seconds...')
            time.sleep(10)
    print('  ...connected!')
    return consumer

def consume_url(consumer):
    for url in consumer:
        print(f'Consumer received "{url}"...')

if __name__ == "__main__":
    consumer = create_kafka_consumer()
    consume_url(consumer)


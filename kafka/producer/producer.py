import time
import json
import random
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

PRODUCE_DELAY_SECONDS = 5
KAFKA_TOPIC = 'url'

def create_kafka_producer():
    print('Connecting to kafka broker...')
    while True:
        try:
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            break
        except NoBrokersAvailable:
            print('Failed to create producer, kafka broker is not yet available. Retrying in 10 seconds...')
            time.sleep(10)
    print('  ...connected!')
    return producer

def send_random_urls(producer):
    with open('urls.json', 'r') as handle:
        urls = json.loads(handle.read())

    while True:
        url = random.choice(urls)
        print(f'Producer sending "{url}"...')
        producer.send(KAFKA_TOPIC, url.encode('utf-8'))
        time.sleep(PRODUCE_DELAY_SECONDS)

if __name__ == "__main__":
    producer = create_kafka_producer()
    send_random_urls(producer)

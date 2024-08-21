from kafka import KafkaConsumer, KafkaProducer

class KafkaClient:
    def __init__(self):
        self.consumer = None
        self.producer = None

    def start(self):
        self.consumer = KafkaConsumer('financial_data_topic', bootstrap_servers=['localhost:9092'])
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    def stop(self):
        if self.consumer:
            self.consumer.close()
        if self.producer:
            self.producer.close()

    def send_message(self, topic, message):
        self.producer.send(topic, message.encode('utf-8'))

    def receive_messages(self):
        for message in self.consumer:
            yield message.value.decode('utf-8')
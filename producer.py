
from time import sleep
from json import dumps
from kafka import KafkaProducer
import os

from dotenv import load_dotenv
load_dotenv()

port = "9092"
adress = os.getenv("SERVER_IP") + ":" + port

producer = KafkaProducer(bootstrap_servers=[adress],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

print("Conectado")
for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)


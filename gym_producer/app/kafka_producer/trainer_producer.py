from dotenv import load_dotenv
from kafka_gym.kafka_directory.producer import produce
import os

load_dotenv(verbose=True)
new_trainer_topic = os.environ['NEW_TRAINER_TOPIC']

def produce_new_trainer(trainer_info):
    produce(
        topic=new_trainer_topic,
        key=trainer_info['id'],
        value=trainer_info)
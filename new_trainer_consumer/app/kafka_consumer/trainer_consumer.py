from dotenv import load_dotenv
from kafka_gym.kafka_settings.consumer import consume
import new_trainer_consumer.app.service.trainer_service as member_service
import os

load_dotenv(verbose=True)
new_trainer_topic = os.environ['NEW_TRAINER_TOPIC']

def consume_trainers():
    consume(
        topic=new_trainer_topic,
        function=member_service.insert_member
    )

from dotenv import load_dotenv
from kafka_gym.kafka_directory.producer import produce
import os

load_dotenv(verbose=True)
new_member_topic = os.environ['NEW_MEMBER_TOPIC']

def produce_new_member(member_info):
    produce(
        topic=new_member_topic,
        key=member_info['id'],
        value=member_info)
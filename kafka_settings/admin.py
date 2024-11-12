import os
from ensurepip import bootstrap
from dotenv import load_dotenv
from kafka_settings import KafkaAdminClient
from kafka_settings.admin import NewTopic
from kafka_settings.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)

def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    new_member_topic = NewTopic(
        name=os.environ['NEW_MEMBER_TOPIC'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    try:
        client.create_topics([new_member_topic])
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()

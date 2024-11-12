import gym_producer.app.kafka_producer.trainer_producer as trainer_producer


def produce_trainer(trainer_info):
    trainer_producer.produce_new_trainer(trainer_info)
import gym_producer.app.kafka_producer.member_producer as member_proudcer


def produce_member(member_info):
    member_proudcer.produce_new_member(member_info)
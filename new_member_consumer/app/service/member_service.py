import new_trainer_consumer.app.repository.trainer_repository as member_repos


def insert_member(kafka_member):
    member_repos.insert_member(kafka_member.value)
    print("consumed member")
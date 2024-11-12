import new_trainer_consumer.app.repository.trainer_repository as trainer_repos


def insert_member(kafka_trainer):
    trainer_repos.insert_trainer(kafka_trainer.value)
    print("consumed trainer")
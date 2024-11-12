from db.database import get_trainers_collection

trainers_collection = get_trainers_collection()

def insert_trainer(trainer_to_add):
    trainer = trainers_collection.insert_one(trainer_to_add)
    return trainer.inserted_id

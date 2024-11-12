from db.database import get_members_collection

members_collection = get_members_collection()

def insert_member(member_to_add):
    member = members_collection.insert_one(member_to_add)
    return member.inserted_id

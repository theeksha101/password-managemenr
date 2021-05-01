import pymongo

client = pymongo.MongoClient("localhost", 27017)

db = client.IT
login_collec = db.login
store_collec = db.store


def checkLogin(username, password):
    entry = login_collec.find_one({"username": username, "password": password})
    if (entry is None):
        return None
    return entry["_id"]


def signupInsert(username, password, email):
    if login_collec.find_one({"$or": [{"username": username}, {"email": email}]}):
        return None
    else:
        return login_collec.insert_one({"username": username, "password": password, "email": email}).inserted_id


def getEntries(owner_id):
    return store_collec.find()

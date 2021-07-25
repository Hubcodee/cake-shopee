from pymongo import MongoClient
client = MongoClient(
    r"mongodb://127.0.0.1:27017")


def db(name, email, company, contact, message):
    db = "test"
    col = "test"
    user = {"name": name, "email": email, "company": company,
            "contact": contact, "message": message}
    client[db][col].insert(user)
    res = client[db][col].find()
    return res, True


def fetch_db():
    db = "test"
    col = "test"
    res = client[db][col].find()
    return res, True


def mod_db(name=None, email=None, company=None, contact=None, message=None):
    db = "test"
    col = "test"
    if name != None:
        query = {"name": name}
    elif company != None:
        query = {"company": company}
    elif contact != None:
        query = {"contact": contact}
    elif message != None:
        query = {"message": message}
    user = {"email": email}
    client[db][col].update(user, {"$set": query})
    res = client[db][col].find()
    return res, True


def del_user(name=None, email=None):
    db = "test"
    col = "test"
    user = {"name": name, "email": email}
    client[db][col].delete_one(user)
    res = client[db][col].find()
    return res, True


def del_all():
    db = "test"
    col = "test"
    client[db][col].remove({})
    return True

    # for i in res:
    #     print(i)

    # update = client[db][col].update_one(
    #     {"name": "eric"}, {"$set": {"address": "Canyon 123"}})

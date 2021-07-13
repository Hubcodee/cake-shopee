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


def mod_db(name, email, company, contact, message):
    db = "test"
    col = "test"
    user = {"name": name, "email": email, "company": company,
            "contact": contact, "message": message}
    client[db][col].update_one()
    res = client[db][col].find()
    return res, True


def del_user(name=None, email=None, company=None, contact=None, message=None):
    db = "test"
    col = "test"
    user = {"name": name, "email": email, "company": company,
            "contact": contact, "message": message}

    client[db][col].delete_one(user)
    res = client[db][col].find()
    return res, True

    # for i in res:
    #     print(i)

    # update = client[db][col].update_one(
    #     {"name": "eric"}, {"$set": {"address": "Canyon 123"}})

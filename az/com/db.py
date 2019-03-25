import pymongo
from pymongo import InsertOne
import csv


def save(uri):
    client = pymongo.MongoClient(uri)
    db = client.get_database("thesis")
    colection = db.get_collection("twt")
    with open("ucl.csv", "r", encoding="utf8") as f:
        reader = csv.DictReader(f)
        list_ = []
        for row in reader:
            list_.append(
                InsertOne(
                    {
                        'user': row["from_user"],
                        'created_at': row["created_at"],
                        'time': row["time"],
                        "user_lang": row["user_lang"]
                    }
                )
            )
        colection.bulk_write(list_)

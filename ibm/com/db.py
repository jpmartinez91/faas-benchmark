from cloudant import CouchDB
import uuid
import csv

client = None


def save(username, passw, url):
    client = CouchDB(username, passw, url=url)
    client.connect()
    database = client["thesis"]
    with open("ucl.csv", "r", encoding="utf8") as f:
        reader = csv.DictReader(f)
        list_ = []
        for row in reader:
            data = {
                'id_': str(uuid.uuid4()),
                'user': row["from_user"],
                'created_at': row["created_at"],
                'time': row["time"],
                "user_lang": row["user_lang"]
            }
            list_.append(data)
        database.bulk_docs(list_)

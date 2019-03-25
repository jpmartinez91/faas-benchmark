from google.cloud import datastore
import json
import uuid
import csv
client = datastore.Client()


def save():
    with open("ucl.csv", "r") as f:
        reader = csv.DictReader(f)
        entities = []
        init = 0
        for row in reader:
            id_ = str(uuid.uuid4())
            key = client.key("TWT", id_)
            entity = datastore.Entity(key=key)
            entity['user'] = row["from_user"]
            entity['created_at'] = row["created_at"]
            entity['time'] = row["time"]
            entity["user_lang"] = row["user_lang"]
            init = init + 1
            if init <= 500:
                entities.append(entity)
                if init == 500:
                    client.put_multi(entities)
                    init = 0
                    entities = []



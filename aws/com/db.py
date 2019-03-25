import boto3
import csv
import os

dynamoDb = boto3.resource("dynamodb")
dynamo_name = os.environ["DYNAMODB_TABLE"]


def save():
    table = dynamoDb.Table(dynamo_name)
    with open("ucl.csv", "r") as f:
        reader = csv.DictReader(f)
        with table.batch_writer() as batch:
            for row in reader:
                batch.put_item(
                    Item={
                        'id_tw': str(uuid.uuid4()),
                        'user': row["from_user"],
                        'created_at': row["created_at"],
                        'time': row["time"],
                        "user_lang": row["user_lang"]
                    }
                )



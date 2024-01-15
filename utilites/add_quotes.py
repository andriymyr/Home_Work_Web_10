import json
from pymongo import MongoClient
from bson import ObjectId
import configparser
import pathlib


file_config = pathlib.Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
db = config.get("DB", "db")
domain = config.get("DB", "domain")
authors = config.get("json", "authors")
qoutes = config.get("json", "qoutes")
count_user = config.get("messege", "count_user")

uri = f"mongodb+srv://{username}:{password}@{db_name}.{domain}/?retryWrites=true&w=majority"


def get_mongodb():
    client = MongoClient(uri, ssl=True)
    return client[db]

db = get_mongodb()
with open("qoutes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for qoute in quotes:
    author = db.authors.find_one({"fullname": qoute["author"]})
    if author:
        db.quotes.insert_one(
            {
                "quote": qoute["quote"],
                "tags": qoute["tags"],
                "author": ObjectId(author["_id"]),
            }
        )

import json
from pymongo import MongoClient
from bson import ObjectId
from quotes.utilite import get_mongodb

db = get_mongodb()
with open("quotes.json", "r", encoding="utf-8") as fd:
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

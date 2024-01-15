import bson
from bson.objectid import ObjectId
from django import template
from ..utilite import get_mongodb

register = template.Library()


def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({"_id": ObjectId(id_)})
    return author["fullname"]


def change_name(name):
    return name.replace(" ", "-")


register.filter("author", get_author)
register.filter("change_name", change_name)

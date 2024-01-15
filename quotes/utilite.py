from pymongo import MongoClient

# from pymongo.server_api import ServerApi
import configparser
import pathlib
from pymongo.server_api import ServerApi


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
    client = MongoClient(uri, server_api=ServerApi("1"))
    return client[db]

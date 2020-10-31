import pymongo
import pprint

username = input("Enter db username: ")
pw = input("Enter db password: ")
user_genre = input("What kind of genre are you looking for? (ie: Comedy, Drama, Western) ")

db_name = "sample_mflix"
collection_name = "movies"

mdbClient = pymongo.MongoClient("mongodb+srv://" + username + ":" + pw + "@sandbox.qx9qh.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = mdbClient[db_name]
collection = db[collection_name]

reccomended_movie = collection.find_one({"genres": user_genre})

pprint.pprint(reccomended_movie['title'])

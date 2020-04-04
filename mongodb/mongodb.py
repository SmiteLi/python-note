# python -m pip install pymongo
import requests, pymongo, datetime, pprint, urllib
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    return client.db.collection.find_one({'_id': ObjectId(post_id)})

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
# password = urllib.parse.quote_plus('pass/word')
password = urllib.parse.quote_plus('ADMIN@123.com')
print('user:', username, 'password:', password)

# client = MongoClient('mongodb://localhost:27017/')
# MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')

db = client['www_pcwap_cn']
# db = client['test-database']
# collection = db.test_collection
posts = db.posts

# Collections and databases are created when the first document is inserted into them.
post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
post_id = posts.insert_one(post).inserted_id
print(post_id)
db.list_collection_names()

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

pprint.pprint(posts.find_one({"author": "Eliot"}))

pprint.pprint(posts.find_one({"_id": post_id}))

pprint.pprint(get('5e88884a54795f3870a4a998'))

new_posts = [{"author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14)},
            {"author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print(posts.count_documents({}))
print('{"author": "Mike"}', posts.count_documents({"author": "Mike"}))

for post in posts.find():
    pprint.pprint(post)

for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)

d = datetime.datetime(2009, 11, 12, 12)

for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)

# create index for collection profiles
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}
]

# result = db.profiles.insert_many(user_profiles)

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# result = db.profiles.insert_one(new_profile)  # This is fine.
try:
    result = db.profiles.insert_one(duplicate_profile)
except DuplicateKeyError as err:
    print(err)


# if __name__ == "__main__":


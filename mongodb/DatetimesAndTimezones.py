# https://api.mongodb.com/python/current/examples/datetimes.html
import requests, pymongo, datetime, pprint, urllib, pytz
from pymongo import MongoClient, WriteConcern
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne, DeleteOne
from pymongo.errors import BulkWriteError
from bson.codec_options import CodecOptions

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('ADMIN@123.com')

client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')
db = client.test
# db = client['aggregation_example']

# result = db.test.bulk_write([
# DeleteMany({})  # Remove all documents from the previous example.
# ])

result = db.test.insert_one({"last_modified": datetime.datetime.utcnow()})

result = db.test.insert_one({"last_modified": datetime.datetime.now()})

# pprint.pprint([doc['last_modified'] for doc in db.test.find()])

result = db.test.insert_one({'date': datetime.datetime(2020, 10, 27, 6, 0, 0)})

pacific = pytz.timezone('US/Pacific')
aware_datetime = pacific.localize(datetime.datetime(2020,10,11,18,0,0))
result = db.times.insert_one({"date": aware_datetime})
print(db.times.find_one()['date'])


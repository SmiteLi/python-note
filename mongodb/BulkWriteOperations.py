# https://api.mongodb.com/python/current/examples/custom_type.html
import requests, pymongo, datetime, pprint, urllib
from pymongo import MongoClient, WriteConcern
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne, DeleteOne
from pymongo.errors import BulkWriteError

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('ADMIN@123.com')

client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')
db = client.bulk_example
# db = client['aggregation_example']
db.test.insert_many([{'i': i} for i in range(10000)]).inserted_ids
print(db.test.count_documents({}))

result = db.test.bulk_write([
# DeleteMany({}),  # Remove all documents from the previous example.
InsertOne({'_id': 1}),
InsertOne({'_id': 2}),
InsertOne({'_id': 3}),
UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}}),
UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True),
ReplaceOne({'j': 1}, {'j': 2})])

pprint.pprint(result.bulk_api_result)

requests = [
    ReplaceOne({'j': 2}, {'i': 5}),
    InsertOne({'_id': 4}),  # Violates the unique key constraint on _id.
    DeleteOne({'i': 5})]
try:
    db.test.bulk_write(requests)
except BulkWriteError as bwe:
    pprint.pprint(bwe.details)

requests = [
InsertOne({'_id': 1}),
DeleteOne({'_id': 2}),
InsertOne({'_id': 3}),
ReplaceOne({'_id': 4}, {'i': 1})]
try:
    db.test.bulk_write(requests, ordered=False)
except BulkWriteError as bwe:
    pprint.pprint(bwe.details)

coll = db.get_collection('test', write_concern=WriteConcern(w=1, wtimeout=1))
try:
    coll.bulk_write([InsertOne({"a": i}) for i in range(4)])
except BulkWriteError as bwe:
    pprint.pprint(bwe.details)
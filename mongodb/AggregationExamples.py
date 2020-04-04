# https://api.mongodb.com/python/current/examples/aggregation.html
import requests, pymongo, datetime, pprint, urllib
from pymongo import MongoClient
from bson.son import SON
from bson.code import Code

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('ADMIN@123.com')

client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')

db = client['aggregation_example']
result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
{"x": 2, "tags": ["cat"]},
{"x": 2, "tags": ["mouse", "cat", "dog"]},
{"x": 3, "tags": []}])

print(result.inserted_ids)

pipeline = [
{"$unwind": "$tags"},
{"$group": {"_id": "$tags", "count": {"$sum": 1}}},
{"$sort": SON([("count", -1), ("_id", -1)])}
]

pprint.pprint(list(db.things.aggregate(pipeline)))

# To run an explain plan for this aggregation use the command() method:
db.command('aggregate', 'things', pipeline=pipeline, explain=True)

mapper = Code("""
function () {
  this.tags.forEach(function(z) {
    emit(z, 1);
  });
}
""")

reducer = Code("""
function (key, values) {
  var total = 0;
  for (var i = 0; i < values.length; i++) {
    total += values[i];
  }
  return total;
}
""")

result = db.things.map_reduce(mapper, reducer, "myresults")
for doc in result.find():
    pprint.pprint(doc)

pprint.pprint(db.things.map_reduce(mapper, reducer, "myresults", full_response=True))

results = db.things.map_reduce(mapper, reducer, "myresults", query={"x": {"$lt": 2}})
for doc in results.find():
    pprint.pprint(doc)

pprint.pprint(
db.things.map_reduce(
mapper,
reducer,
out=SON([("replace", "results"), ("db", "outdb")]),
full_response=True))
# python -m pip install pymongo
import requests, pymongo, datetime, pprint, urllib, logging
from pymongo import MongoClient
from logging.handlers import RotatingFileHandler
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
#定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大50M : 50 * 1024 * 1024
rHandler = RotatingFileHandler("main.log",maxBytes = 50*1024*1024,backupCount = 10)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

 
logger.addHandler(rHandler)
logger.addHandler(console)

logger.info("Start print log, info level.")
logger.debug("debug level log.")
logger.warning("warning level log.")
logger.info("info level log.")

# url = 'https://www.pcwap.cn/show/602038.html'

# r = requests.get(url)

# print(r.status_code)
# print(r.text)

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
# password = urllib.parse.quote_plus('pass/word')
password = urllib.parse.quote_plus('ADMIN@123.com')
print('user:', username, 'password:', password)

# client = MongoClient('mongodb://localhost:27017/')
# MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
client = MongoClient('55.qiweioa.cn', 8089)
client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')

db = client['www_pcwap_cn']
# db = client['test-database']
collection = db.test_collection

# Collections and databases are created when the first document is inserted into them.
post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
posts = db.posts
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








# if __name__ == "__main__":

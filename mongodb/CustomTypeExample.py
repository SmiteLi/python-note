# https://api.mongodb.com/python/current/examples/custom_type.html
import requests, pymongo, datetime, pprint, urllib
from pymongo import MongoClient
from bson.son import SON
from bson.code import Code
from decimal import Decimal
from bson.decimal128 import Decimal128
from bson.codec_options import TypeCodec, TypeRegistry, CodecOptions

class DecimalCodec(TypeCodec):
    python_type = Decimal
    bson_type = Decimal128
    def transform_python(self, value):
        return Decimal128(value)
    def transform_bson(self, value):
        return value.to_decimal()

# https://api.mongodb.com/python/current/examples/authentication.html
username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('ADMIN@123.com')

client = MongoClient('55.qiweioa.cn', 8089, username='admin',password='ADMIN123.com',authSource='admin',authMechanism='SCRAM-SHA-256')
client.drop_database('custom_type_example')
# db = client['aggregation_example']
db = client.custom_type_example

num = Decimal("45.321")
# db.test.insert_one({'num': num})

decimal_codec = DecimalCodec()
type_registry = TypeRegistry([decimal_codec])
codec_options = CodecOptions(type_registry=type_registry)
collection = db.get_collection('test', codec_options=codec_options)
collection.insert_one({'num': Decimal("45.321")})
mydoc = collection.find_one()
pprint.pprint(mydoc)

vanilla_collection = db.get_collection('test')
pprint.pprint(vanilla_collection.find_one())
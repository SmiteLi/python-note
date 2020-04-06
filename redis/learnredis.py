# -*- coding: UTF-8 -*-

import redis
import random

r = redis.Redis(host='192.168.153.136', port=6379, password='123456', db=0)
r.set('foo','bar')
print(r.get('foo'))

for i in range(10):
    r.set('key' + str(i), i)

for i in range(10):
    print(r.get('key'+ str(i)))

for i in range(10):
    r.hset('hash01', i, random.randrange(1,100))

for i in range(10):
    print(r.hget('hash01', i))

print(r.hgetall('hash01'))

for i in range(10):
    r.lpush('list01', i)

for i in range(10):
    r.rpush('list01', i)

print(r.lrange('list01', 0, 100))

for ch in list(map(chr, range(ord('a'), ord('z') + 1))):
    r.sadd('set01', ch)

print(r.smembers('set01'))

keys = r.keys()
print(type(keys))
print(keys)
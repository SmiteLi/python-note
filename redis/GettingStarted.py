# https://pypi.org/project/redis/
import redis, time

r = redis.Redis(host='55.qiweioa.cn', port=8088, db=0, password='Admin123.com')
r.set('foo', 'bar')
r.get('foo')

# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

r.set('bing', 'baz')
r.set('visits:100', 999)
r.incr('visit:100')
r.get('visit:100')

pipe = r.pipeline()
pipe.set('foo', 'bar')
pipe.get('bing')
pipe.execute()
pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
# pipe = r.pipeline(transaction=False)
current_value = 10

# WATCH 命令提供了在开始事务前监视一个或多个键
# 这些键中的任何一个在执行事务前发生改变，整个事务就会被取消并抛出 WatchError 异常
# 事务由命令MULTI命令启动，然后需要传递一个应该在事务中执行的命令列表，然后整个事务由EXEC命令执行
sellerid = 101
itemid = 101
price = 50
print(time.time())
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

def list_item(r, itemid, sellerid, price):
    inventory = "inventory:%s" %sellerid
    item = "%s:%s" % (itemid, sellerid)
    end = time.time() + 5
    pipe = r.pipeline()
    while time.time() < end:
        try:
            pipe.watch(inventory)
            if not pipe.sismember(inventory, itemid):
                pipe.unwatch()
                return None
            pipe.multi()
            pipe.zadd("market:", item, price)
            pipe.srem(inventory, itemid)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
        return False

list_item(r, itemid, sellerid, price)

def client_side_incr(pipe):
    current_value = pipe.get('OUR-SEQUENCE-KEY')
    next_value = int(current_value) + 1
    pipe.multi()
    pipe.set('OUR-SEQUENCE-KEY', next_value)

r.transaction(client_side_incr, 'OUR-SEQUENCE-KEY')
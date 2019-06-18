import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib import request, parse
from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener, ProxyHandler
from urllib.error import URLError
import http.cookiejar

# user-account
username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

# proxy
proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'http://127.0.0.1:9743'
})

opener = build_opener(proxy_handler)
try:
    response2 = opener.open('https://baidu.com')
    print(response2.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response3 = opener.open('http://baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

response = urllib.request.urlopen('http://www.python.org')
#print(response.read().decode('utf-8'))

print(type(response))


print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

request1 = urllib.request.Request('https://python.org')
response1 = urllib.request.urlopen(request1)
print(response1.read().decode('utf-8'))
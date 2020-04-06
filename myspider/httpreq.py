
# http://2.python-requests.org/zh_CN/latest/user/quickstart.html

import requests, json

# r = requests.get('https://api.github.com/events')
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})
# r = requests.put('http://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
print(r.text)
print(r.content)
print(r.encoding)
print(r.status_code)
print(r.raise_for_status())


# r = requests.get('https://api.github.com/events')
# print(r.encoding)
# print(r.json())
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)

# 你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

payload = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# 很多时候你想要发送的数据并非编码为表单形式的。如果你传递一个 string 而不是一个 dict，那么数据会被直接发布出去。
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# #  2.4.2 版的新加功能：
# r = requests.post(url, json=payload)

# POST一个多部分编码(Multipart-Encoded)的文件
url = 'http://httpbin.org/post'
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
files = {'file': open('H:\\python-note\\spider\\cookies.txt', 'rb')}
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print(r.text)
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers.get('content-type'))

# if r.status_code == requests.codes.ok :
#     print('200 OK')


# bad_r = requests.get('http://httpbin.org/status/404')
# print(bad_r.status_code)
# bad_r.raise_for_status()

# ## cookies 的使用
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# r.text
# Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。你还可以把 Cookie Jar 传到 Requests 中：

# >>> jar = requests.cookies.RequestsCookieJar()
# >>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# >>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# >>> url = 'http://httpbin.org/cookies'
# >>> r = requests.get(url, cookies=jar)
# >>> r.text
# '{"cookies": {"tasty_cookie": "yum"}}'
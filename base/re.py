import re

data = 'Hello in Python 2.7.5;Hello in python 3.7.5'

re.findall('Python [0-9]\.[0-9]\.[0-9]', data)

re_obj = re.compile('Python [0-9]\.[0-9]\.[0-9]', flags=re.IGNORECASE)
re_obj.findall(data)

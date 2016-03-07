import urllib
import urllib2
url = 'http://localhost:3000/api/todos'
values = {'arg1': 'value1', 'arg2': 'value2'}
headers = {'User-Agent': 'python urllib2'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
result = response.read()
print result

from urllib import request, parse

url = 'http://www.httpbin.org/get'


parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

queryString = parse.urlencode(parms)

u = request.urlopen(url+'?'+queryString)

resp = u.read()
print(resp)




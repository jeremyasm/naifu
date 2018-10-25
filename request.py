# -*- coding: utf-8 -*- 
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
status_code = response.status_code
print('status code:', status_code)
response_body = response.text
if response_body.find('<') == -1:
	print('it is error')
	print('response body:', response_body)
else:
	if (response_body.find('北京东单') > 0) and (response_body.find('2018-10-20') > 0):
	   # print(response_body)
	   print('it is xml')
	   id = url[(len(url) - 12):len(url)]
	   filename = id+'.txt'
	   # print(filename)
	   with open(filename, 'w') as f:
	      f.write(response_body)
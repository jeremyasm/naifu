import requests
import sys
def gen_permutation(str, num):
        if(num == 1):
            for x in str:
                yield x
        else:
            for x in str:
                for y in gen_permutation(str, num-1):
                    yield x+y
 
strKey="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for x in gen_permutation(strKey,12):
    print(x)
    url = 'https://x.y.com/i/'+x
    print(url)
    response = requests.get(url)
    status_code = response.status_code
    print('status:', status_code)
    response_body = response.text
    print(response_body)
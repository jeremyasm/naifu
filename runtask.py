# -*- coding: utf-8 -*- 
import requests
import sys
import time

def getRequest(url, id):
    response = requests.get(url)
    status_code = response.status_code
    print('status code:', status_code)
    response_body = response.text
    if response_body.find('<') == -1:
	       print('it is error')
	       print('response body:', response_body)
    else:
        print('it is xml')
        # if (response_body.find('北京东单') > 0) and (response_body.find('2018-10-20') > 0):
        if 1 > 0:
	              # print(response_body)
	              # id = url[(len(url) - 12):len(url)]
	              filename = id+'.txt'
	              # print(filename)
	              with open(filename, 'w') as f:
	                     f.write(response_body)


def gen_permutation(charset, bits):
        if(bits == 1):
            for x in charset:
                yield x
        else:
            for x in charset:
                for y in gen_permutation(charset, bits-1):
                    yield x+y
                         
if __name__ == "__main__":
    start = time.time()
    count = 0
    print('This is main function.')
    ##################################
    # strKey="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    # first_part="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # second_part="1234567890ABCDEF"
    first_part="apxBK"
    second_part="135AF"
    # https://y.x.com/i/KxpBaF5AA31
    # for fp in gen_permutation(first_part,5):
    list = ["KxpBa"]
    for fp in list:
        for sp in gen_permutation(second_part,7):
            id = fp + sp
            print('============================')
            print('try id:', id)
            url = 'https://x.y.com/i/' + id
            getRequest(url, id)
            current = time.time()
            print('time elapsed:', current - start)
            count += 1
            print('requests count:', count)
    ############################################
    end = time.time()
    print('time elapsed:', end - start)


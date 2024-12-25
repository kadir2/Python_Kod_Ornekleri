import json

    

if __name__ == '__main__':
    with open('test.json', 'r') as f:
        data = json.load(f)
    abc = data['api_key']
    xyz = data['timeout']
    v= data['endpoints'][0]
    a=v['url']
    b=v['method']
    c=v['headers']['Content-Type']

    print(abc)
    print(xyz)
    print(a)
    print(b)
    print(c)
    #bunun gibi onlarca kod daha

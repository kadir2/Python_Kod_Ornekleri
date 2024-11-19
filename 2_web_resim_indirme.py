import urllib.request

url1 = 'https://avatars.mds.yandex.net/get-mpic/1985106/img_id2047960825122601198.jpeg/orig'
url2 = 'https://i.pinimg.com/originals/24/97/12/2497128c6cf4e7b7a686c94a5cf09e31.jpg'
url3 = 'https://wallpapers.com/images/hd/outdoor-background-lqbdhgwpyctsjcmf.jpg'

urls = [url1, url2, url3]

i=1
for url in urls:
   urllib.request.urlretrieve(url,"resim"+str(i)+".jpeg")
   i+=1

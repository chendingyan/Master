# -*- coding:utf-8 -*
# import re
# import requests
import os
import urllib.request
# from bs4 import BeautifulSoup
def xxx():
    url = 'https://www.thiswaifudoesnotexist.net'
    html = requests.get(url).text  # 获取网页内容
    print(html)
    # 这里由于有些图片可能存在网址打不开的情况，加个5秒超时控制。
    # data-objurl="http://pic38.nipic.com/20140218/17995031_091821599000_2.jpg"获取这种类型链接
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    # ^abc.*?qwe$
    pic_url = soup.find_all('img', src=re.compile(r'^https://www.thiswaifudoesnotexist.net/.*?jpg$'))
    # pic_url = pic_node.get_text()
    # pic_url = re.findall('"https://cdn.pixabay.com/photo/""(.*?)",',html,re.S)
    print(pic_url)
    i = 0
    # 判断image文件夹是否存在，不存在则创建
    if not os.path.exists('webcrawled-image'):
        os.makedirs('webcrawled-image')
    for url in pic_url:
        img = url['src']
        try:
            pic = requests.get(img, timeout=5)  # 超时异常判断 5秒超时
        except requests.exceptions.ConnectionError:
            print('当前图片无法下载')
            continue
        file_name = "webcrawled-image/" + str(i) + ".jpg"  # 拼接图片名
        print(file_name)
        # 将图片存入本地
        fp = open(file_name, 'wb')
        fp.write(pic.content)  # 写入图片
        fp.close()
        i += 1

def one_photo(num):

    # 图片url地址
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    # req = urllib.request.Request(url=chaper_url, headers=headers)
    # urllib.request.urlopen(req).read()

    url = 'https://www.thiswaifudoesnotexist.net/example-'+ str(num) + '.jpg'
    # 方法一
    # 获取图片数据
    req = urllib.request.Request(url=url, headers=headers)
    image = urllib.request.urlopen(req).read()
    path = "./webcrawled-image/"
    with open(path + '%s.jpg' % num, 'wb') as fp:
        fp.write(image)
        print("正在下载第%s张图片" % num)




if __name__ == '__main__':
    for i in range(200000):
        one_photo(i)
# -*- coding:utf-8*-
from http import cookiejar
from urllib import request
from lxml import etree


def get_ip_list(item, num=0):
    cj = cookiejar.CookieJar()  # 创建CookieJar对象
    handler = request.HTTPCookieProcessor(cj)   # 创建cookie处理器
    opener = request.build_opener(handler)  # 创建打开器
    url = 'http://qq.ip138.com/idsearch/index.asp?action=idcard&userid='+ item
    # 封装请求头参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Referer': 'http://qq.ip138.com/idsearch/index.asp?action=idcard',
        'Host': 'qq.ip138.com'
    }
    req = request.Request(url, headers=headers)
    response = opener.open(req)     # 发送请求，返回响应
    response = response.read().decode()
    node = etree.HTML(response)
    node1 = node.xpath('//div[@class="bd"]//table/tbody/tr/td[2]//text()')
    print(num)
    return node1


# print(u'总共耗时：'+str(time2-time1)+'s')
if __name__ == '__main__':
    num = 0
    with open('shen.txt', 'r') as f:
        idcards = f.read()
        idcards = idcards.split('\n')
    with open('身份信息.txt', 'a')as f:
        for idcard in idcards:
            num += 1
            text = get_ip_list(idcard, num)
            print(text)
            f.write(str(text)+'\n')
    print('爬虫完毕')

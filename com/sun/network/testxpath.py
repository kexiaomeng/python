from lxml import etree
from urllib import request
import os
import time

def get_html(url):

    page = request.urlopen(url)
    html = page.read()
    return html


def getArticleLinks(urls):
    url_list = []
    for url in urls:

        url_list.append('https://tieba.baidu.com' + url)

    return url_list


def get_photo_per_url(url, j):

    root_path  = os.getcwd()
    rootpath = 'downloads'

    data = etree.HTML(get_html(url))
    selects = data.xpath('//*[@id="j_p_postlist"]/div//img[@class="BDE_Image"]/@src')

    imgdir = rootpath+'/'+j

    if not os.path.exists(imgdir):
        os.mkdir(imgdir)

    os.chdir(imgdir)
    print(os.getcwd())

    i = 0
    for select in selects:

        request.urlretrieve(select, os.getcwd() + "/%s.jpg" % i)
        i = i+1

    os.chdir(root_path)
    print(os.getcwd())

    time.sleep(3)



if __name__ == '__main__':

    data = etree.HTML(get_html('https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A3%81%E7%BA%B8').decode("utf-8"))

    result = etree.tostring(data, encoding="utf-8")
    # print(result.decode('utf-8'))

    # select = data.xpath('//*[@id="head"]/div/div[1]/div/a[1]/text()')


    select = data.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')

    active_utls = getArticleLinks(select)

    print(active_utls)
    j = 0;
    for url in active_utls:
        print(url)
        get_photo_per_url(url, "imgs%s" % j)
        j += 1






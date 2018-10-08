from lxml import etree
from urllib import request


def get_html(url):

    page = request.urlopen(url)
    html = page.read()
    return html


def getArticleLinks(urls):
    url_list = []
    for url in urls:

        url_list.append('https://tieba.baidu.com' + url)

    return url_list


data = etree.HTML(get_html('https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A3%81%E7%BA%B8').decode("utf-8"))

result = etree.tostring(data, encoding="utf-8")
# print(result.decode('utf-8'))

# select = data.xpath('//*[@id="head"]/div/div[1]/div/a[1]/text()')


select = data.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href')


print(getArticleLinks(select))



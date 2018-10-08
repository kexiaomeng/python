from urllib import request, parse
import re

print("-----网页图片抓取------")
print("请输入url:")
url = input()

if url:
    pass
else:
    url = 'https://tieba.baidu.com/p/5897430180'


print(url)
#
# page = request.urlopen(str)
#
# html = page.read(1024)


def get_html(url):

    page = request.urlopen(url)
    html = page.read()
    return html


# html = get_html(str)
#
# with open('thieba.html','wb') as f:
#
#     f.write(html)
reg = 'src="(.+?\.jpg)" size'

reg_img = re.compile(reg)

html = get_html(url)

imglist = reg_img.findall(html.decode("utf-8"))

i = 0
for img in imglist:
    i += 1
    if(img.startswith("//",0,2)):

        img = img.split("//",1)[1]
    print(img)
    request.urlretrieve(img, "img/%s.jpg" % i)

print("下载成功")









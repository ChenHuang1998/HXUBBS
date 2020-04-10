import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HXUBBS.settings")# project_name 项目名称
django.setup()
import requests
from lxml import etree
from new_spider.models import *

def get_new(url):
    response = requests.get(url)
    html = etree.HTML(response.content.decode('utf-8'))
    new_list = html.xpath('//div[@id="newslist"]/ul/li')
    for new in new_list:
        new_title = new.xpath('./a/@title')[0]
        new_url = new.xpath('./a/@href')[0].replace('../', 'http://www10.hxu.edu.cn/',1)
        new_time = new.xpath('./span/text()')[0]
        News.objects.create(title=new_title,url=new_url,time=new_time)


if __name__ == '__main__':
    News.objects.all().delete()
    url = 'http://www10.hxu.edu.cn/xwzx/xykx.htm'
    get_new(url)



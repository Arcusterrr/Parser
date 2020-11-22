import requests
import lxml.html
from lxml import etree

def habr_themes():
    url = 'https://habr.com/ru/'
    html_text = requests.get(url).text

    tree = lxml.html.document_fromstring(html_text)
    finDict = dict()

    staff_title = tree.xpath('//*[@class="post__title_link"]/text()')
    staff_object = tree.xpath('//*[@class="post__title_link"]')
    hreflist = []

    for i in staff_object:
        hreflist.append(i.attrib['href']) 

    finDict['title'] = staff_title
    finDict['href'] = hreflist
    formatedList = []

    for i in range(len(finDict['title'])):
        formatedList.append([finDict['title'][i], finDict['href'][i]])
    return formatedList
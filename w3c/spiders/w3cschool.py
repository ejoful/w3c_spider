# -*- coding: utf-8 -*-
import scrapy
import sys
from w3c.items import W3CItem

class W3cschoolSpider(scrapy.Spider):
    name = "w3cschool"
    allowed_domains = ["w3cschool.cn"]
    start_urls = (
        'http://www.w3cschool.cn/html/',
    )
    # 编码设置为utf8,避免中文显示为unicode编码
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def parse(self, response):
        w3c_item = W3CItem()

        url_str = start_urls[0][:-1]
        url_arr = url_str.split('/')

        w3c_item['tutorial_slug'] = url_arr[-1]
        w3c_item['tutorial_name'] = response.xpath('//div[@class="coverinfo"]/h1/text()')[0].extract()
        w3c_item['tutorial_description'] = response.xpath('//div[@class="coverinfo-desc"]/p/text()')[0].extract()
        img_path_str = response.xpath('//img[@class="pimgcover"]/@src')[0].extract()
        img_path_arr = img_path_str.split('?')
        w3c_item['tutorial_img_path'] = img_path_arr[0]
        content_str = response.xpath('//div[@class="project-desc-content"]')[0].extract()
        w3c_item['tutorial_content'] = content_str[35:-6]
        w3c_item['tutorial_position'] = 1

        w3c_item['tutorial_doc'] = []

        doc_list = response.xpath('//div[@id="nestable_handbook"]/ol')
        li_list = doc_list[0].xpath('li')

        #组装文章链接
        doc_link_arr = []
        index = 0
        for li_str in li_list[0:]:
            slug = li_str.xpath('@data-id')
            link = 'http://www.w3cschool.cn/' + w3c_item['tutorial_slug'] + '/' + slug + '.html'
            ismenu = li_str.xpath('@ismenu')
            index = index + 1

            if not ismenu:
                title = li_str.xpath('div/h2[@class="dd-content "]/a/@title')[0].extract()
                doc_link_arr.append({'tutorial_id': 1,
                                     'ismenu': 0,
                                     'slug': slug,
                                     'name': title,
                                     'description': '',
                                     'link': link,
                                     'content': '',
                                     'tag': '',
                                     'position': index})
            else:
                title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
                doc_link_arr.append({'tutorial_id': 1,
                                     'ismenu': 1,
                                     'slug': slug,
                                     'name': title,
                                     'description': title + '_来自' + w3c_item['tutorial_name'] + ',w3cxyz',
                                     'link': link,
                                     'content': '',
                                     'tag': '',
                                     'position': index})
                #组装菜单下面的链接
                menu_doc_li = li_str.xpath('ol[@class="dd-list"]/li')
                for doc_li in menu_doc_li[0:]:
                    index = index + 1
                    doc_slug = doc_li.xpath('@data-id')
                    doc_name = doc_li.xpath('div[@class="dd-content "]/a/@title')[0].extract()
                    doc_link = ['http://www.w3cschool.cn' + doc_li.xpath('div[@class="dd-content "]/a/@href')[0].extract()]
                    doc_link_arr.append({'tutorial_id': 1,
                                         'ismenu': 0,
                                         'slug': doc_slug,
                                         'name': doc_name,
                                         'description': '',
                                         'link': doc_link,
                                         'content': '',
                                         'tag': '',
                                         'position': index})
        return self.recursive_parse_video(doc_link_arr, w3c_item)


        #         w3c_item['tutorial_doc'].append({'tutorial_id': 1,
        #                                          'ismenu': ismenu,
        #                                          'slug': slug,
        #                                          'name': title,
        #                                          'description': title + '_来自' + w3c_item['tutorial_name'] + ',w3cxyz',
        #                                          'content': '',
        #                                          'tag': '',
        #                                          'position': index})
        #         menu_doc_li = li_str.xpath('ol[@class="dd-list"]/li')
        #
        # index = 0
        # for li_str in li_list[0:]:
        #     slug = li_str.xpath('@data-id')
        #     ismenu = li_str.xpath('@ismenu')
        #
        #     if not ismenu:
        #         title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
        #     else:
        #         title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
        #         index = index+1
        #         w3c_item['tutorial_doc'].append({'tutorial_id':1,
        #                                          'ismenu':ismenu,
        #                                          'slug':slug,
        #                                          'name':title,
        #                                          'description':title+'_来自'+w3c_item['tutorial_name']+',w3cxyz',
        #                                          'content':'',
        #                                          'tag':'',
        #                                          'position':index})
        #         menu_doc_li = li_str.xpath('ol[@class="dd-list"]/li')
        #
        #         for doc_li in menu_doc_li[0:]:
        #             doc_slug = doc_li.xpath('@data-id')
        #             doc_name = doc_li.xpath('div[@class="dd-content "]/a/@title')[0].extract()
        #             doc_link = ['http://www.w3cschool.cn'+doc_li.xpath('div[@class="dd-content "]/a/@href')[0].extract()]
        #             yield scrapy.Request(url=doc_link[0], meta={'w3c_item': w3c_item,'doc_slug':doc_slug,'doc_name':doc_name,'index':index,'tag':title}, callback=self.parse_doc,
        #                                  dont_filter=True)

    def recursive_parse_doc(self, tbd, w3c_item):
        if not tbd:
            yield w3c_item
        else:
            les = tbd.pop()
            title = les.xpath('a/span/text()')[0].extract()
            link = ["http://www.maiziedu.com" + les.xpath('a/@href')[0].extract()][0]

            yield scrapy.Request(url=link,
                                 meta={'tbd': tbd, 'w3c_item': w3c_item, 'title': title, 'link': link},
                                 callback=self.parse_doc,
                                 dont_filter=True)

    def parse_doc(self, response):
        w3c_item = response.meta['w3c_item']
        doc_slug = response.meta['doc_slug']
        doc_name = response.meta['doc_name']
        index = response.meta['index']
        tag = response.meta['tag']

        doc_description = response.xpath('/html/head/meta[@name="description"]/@content')[0].extract()
        doc_content = response.xpath('/html/head/meta[@name="description"]/@content')[0].extract()
        doc_content_str = response.xpath('//div[@class="content-intro view-box"]')[0].extract()
        doc_content = doc_content_str[36:-6]

        w3c_item['tutorial_doc'].append({'tutorial_id': 1,
                                         'ismenu': 0,
                                         'slug': doc_slug,
                                         'name': doc_name,
                                         'description': doc_description,
                                         'content': doc_content,
                                         'tag': tag,
                                         'position': index})
        course_item['lessons'].append(
            {'video_id': video_id, 'title': title, 'link': link, 'video_link': video_link})
        tbd = response.meta['tbd']
        return self.recursive_parse_video(tbd, course_item)


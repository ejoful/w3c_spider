# -*- coding: utf-8 -*-
import scrapy
import sys
from w3c.items import W3CItem

'''
 jquery获取url
http://www.w3cschool.cn/tutorial

var url = "";
var index = 0;
$(".pro-item a").each(function(){
var cur_url=$(this).attr('href');
    url += "\"http://"+cur_url.substr(2)+"\",";
    index += 1;
});
console.log(url);
//url就是遍历出来的单个a标签网址，txt就是a之间的文本。

'''


class W3cschoolSpider(scrapy.Spider):
    name = "w3cschool"
    allowed_domains = ["w3cschool.cn"]
    start_urls = [
        # "http://www.w3cschool.cn/html/", "http://www.w3cschool.cn/html5/", "http://www.w3cschool.cn/css/",
        # "http://www.w3cschool.cn/css3/", "http://www.w3cschool.cn/bootstrap/", "http://www.w3cschool.cn/foundation/",
        # "http://www.w3cschool.cn/javascript/", "http://www.w3cschool.cn/htmldom/", "http://www.w3cschool.cn/jquery/",
        # "http://www.w3cschool.cn/angularjs/", "http://www.w3cschool.cn/react/",
        # "http://www.w3cschool.cn/jqueryui/",
        # "http://www.w3cschool.cn/jqueryeasyui/",
        # "http://www.w3cschool.cn/nodejs/",
        #  "http://www.w3cschool.cn/ajax/",
        # "http://www.w3cschool.cn/json/",
        # "http://www.w3cschool.cn/highcharts/",
        #  "http://www.w3cschool.cn/googleditu/",
        # "http://www.w3cschool.cn/php/",
        # "http://www.w3cschool.cn/python/",
        # "http://www.w3cschool.cn/python3/",
        # "http://www.w3cschool.cn/django/",
        # "http://www.w3cschool.cn/linux/",
        # "http://www.w3cschool.cn/docker/",
        # "http://www.w3cschool.cn/ruby/",
        # "http://www.w3cschool.cn/java/",
        #  "http://www.w3cschool.cn/c/",
        # "http://www.w3cschool.cn/cpp/",
        #  "http://www.w3cschool.cn/perl/",
        #  "http://www.w3cschool.cn/servlet/",
        # "http://www.w3cschool.cn/jsp/",
        #  "http://www.w3cschool.cn/lua/",
        #  "http://www.w3cschool.cn/scala/",
        # "http://www.w3cschool.cn/go/",
        #  "http://www.w3cschool.cn/shejimoshi/",
        # "http://www.w3cschool.cn/zhengzebiaodashi/",
        #  "http://www.w3cschool.cn/asp/",
        #  "http://www.w3cschool.cn/appml/",
        # "http://www.w3cschool.cn/vbscript/",
        #  "http://www.w3cschool.cn/wkspring/",
        #  "http://www.w3cschool.cn/sql/",
        # "http://www.w3cschool.cn/mysql/",
        #  "http://www.w3cschool.cn/sqlite/",
        #  "http://www.w3cschool.cn/mongodb/",
        # "http://www.w3cschool.cn/redis/",
        #  "http://www.w3cschool.cn/memcached/",
        #  "http://www.w3cschool.cn/android/",
        # "http://www.w3cschool.cn/swift/",
        #  "http://www.w3cschool.cn/jquerymobile/",
        #  "http://www.w3cschool.cn/ionic/",
        # "http://www.w3cschool.cn/ios/",
        #  "http://www.w3cschool.cn/xml/",
        #  "http://www.w3cschool.cn/dtd/",
        # "http://www.w3cschool.cn/xmldom/",
        # "http://www.w3cschool.cn/xslt/",
        # "http://www.w3cschool.cn/xlink/",**********************************************
        # "http://www.w3cschool.cn/xslfo/",
         # "http://www.w3cschool.cn/xpath/",
        # "http://www.w3cschool.cn/xquery/",
         # "http://www.w3cschool.cn/xpointer/",
        # "http://www.w3cschool.cn/xmlschema/",
         # "http://www.w3cschool.cn/svg/",
        # "http://www.w3cschool.cn/aspnet/",
        #  "http://www.w3cschool.cn/csharp/",
        #  "http://www.w3cschool.cn/webservices/",
        # "http://www.w3cschool.cn/wsdl/",
         # "http://www.w3cschool.cn/soap/",
         # "http://www.w3cschool.cn/rss/",
        # "http://www.w3cschool.cn/rdf/",
         # "http://www.w3cschool.cn/eclipse/",
         # "http://www.w3cschool.cn/git/",
        # "http://www.w3cschool.cn/firebug/",
         # "http://www.w3cschool.cn/http/",
         # "http://www.w3cschool.cn/tcpip/",
        # "http://www.w3cschool.cn/wzjszn/",
         # "http://www.w3cschool.cn/llq/",
         # "http://www.w3cschool.cn/wzzjjc/",
        # "http://www.w3cschool.cn/xuexiw3c/",
        #  "http://www.w3cschool.cn/wzpz/",





        #
        # "http://www.w3cschool.cn/htmltags/", "http://www.w3cschool.cn/cssref/", "http://www.w3cschool.cn/jsref/",
        # "http://www.w3cschool.cn/xmldom/",  "http://www.w3cschool.cn/ssdb/",
        # "http://www.w3cschool.cn/phpkfbmgf/",**********************************************

        # "http://www.w3cschool.cn/jeesite/", "http://www.w3cschool.cn/uncode/", "http://www.w3cschool.cn/osmp/",
        # "http://www.w3cschool.cn/jfinal/", "http://www.w3cschool.cn/aniauto/",
        #
        # "http://www.w3cschool.cn/nutz/","http://www.w3cschool.cn/yii2manual/",

        # "http://www.w3cschool.cn/mip/",
        # "http://www.w3cschool.cn/jslite/",
        # "http://www.w3cschool.cn/ymp/",

        # "http://www.w3cschool.cn/omi/",
         # "http://www.w3cschool.cn/fag2f6/",

        # "http://www.w3cschool.cn/phalcon7/",
        # "http://www.w3cschool.cn/finch/",


        # "http://www.w3cschool.cn/thinkphp/",

        # "http://www.w3cschool.cn/zqf/",

        # "http://www.w3cschool.cn/php300/",
        # "http://www.w3cschool.cn/cobub/",

        # "http://www.w3cschool.cn/dedecms/",
        # "http://www.w3cschool.cn/jpaspec/",
        # "http://www.w3cschool.cn/liblog/",
        # "http://www.w3cschool.cn/lme/",
        # "http://www.w3cschool.cn/weflow/",
        # "http://www.w3cschool.cn/memory/",
        # "http://www.w3cschool.cn/lsc/",
        # "http://www.w3cschool.cn/openwaf/",
        # "http://www.w3cschool.cn/qmui_web/",
        # "http://www.w3cschool.cn/whc_autolayout/",

        # "http://www.w3cschool.cn/openauthdotnet/",
        # "http://www.w3cschool.cn/dfs/",
        # "http://www.w3cschool.cn/zys/",
        # "http://www.w3cschool.cn/webside/",
        # "http://www.w3cschool.cn/fastquery/",
        # "http://www.w3cschool.cn/easyokhttp/",
        # "http://www.w3cschool.cn/wxtools/",
        # "http://www.w3cschool.cn/dwz_jui/",
        # "http://www.w3cschool.cn/xingo/",
        # "http://www.w3cschool.cn/liblog/",
        # "http://www.w3cschool.cn/typesdk/",
        # "http://www.w3cschool.cn/cron/",
        # "http://www.w3cschool.cn/xujunzhou/",
        # "http://www.w3cschool.cn/lvxin/",

        # "http://localhost/test/opensnscourse/opensnscourse.html",
        # "http://www.w3cschool.cn/opensnscourse/",
        # "http://www.w3cschool.cn/seafile/",
        # "http://localhost/test/seafile/seafile.html",
        # "http://www.w3cschool.cn/thinkphp323",
        # "http://localhost/test/thinkphp323/thinkphp323.html",
        # "http://www.w3cschool.cn/hprose_php/",
        # "http://localhost/test/hprose_php/hprose_php.html",
        # "http://www.w3cschool.cn/idea_framework/",
        # "http://localhost/test/idea_framework/idea_framework.html",
        # "http://www.w3cschool.cn/phalapi/",
        # "http://localhost/test/phalapi/phalapi.html",


        # "http://www.w3cschool.cn/ohsce/",



        # "http://www.w3cschool.cn/tinyform/tinyform-home.html",

        # "http://www.w3cschool.cn/wex5/",
        # "http://tp://www.bootcss.com",
    ]
    # start_urls.reverse()
    # 编码设置为utf8,避免中文显示为unicode编码
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def parse(self, response):
        w3c_item = W3CItem()

        url_str = response.url
        url_arr = url_str.split('/')

        w3c_item['category'] = 'opensource'

        w3c_item['slug'] = url_arr[-2]

        w3c_item['name'] = response.xpath('//div[@class="coverinfo"]/h1/text()')[0].extract()
        w3c_item['description'] = response.xpath('//div[@class="coverinfo-desc"]/p/text()')[0].extract()
        img_path_str = response.xpath('//img[@class="pimgcover"]/@src')[0].extract()
        img_path_arr = img_path_str.split('?')
        img_arr = img_path_arr[0].split('/')
        w3c_item['img'] = img_arr[-1]

        w3c_item['img_path'] = img_path_arr[0]
        if response.xpath('//div[@class="project-desc-content"]'):
            content_str = response.xpath('//div[@class="project-desc-content"]')[0].extract()
        else:
            content_str = ''
        w3c_item['content'] = content_str[35:-6]
        w3c_item['position'] = 1

        w3c_item['tutorial_doc'] = []

        doc_list = response.xpath('//div[@id="nestable_handbook"]/ol')
        li_list = doc_list[0].xpath('li')

        #组装文章链接
        doc_link_arr = []
        index = 0
        for li_str in li_list[0:]:
            slug = str(li_str.xpath('@data-id')[0].extract())
            # python基础教程 教程中 Python 拓展阅读 跳出
            if (slug == 'css-rwd-videos') or (slug == 'w8bg1tbj') or (slug == 'ah4g12cb') or (slug == 'xslfo-reference'):
                break
            # slug = slug_arr[0]
            link = 'http://www.w3cschool.cn/' + str(w3c_item['slug']) + '/' + slug + '.html'
            if li_str.xpath('@ismenu'):
                 is_menu = li_str.xpath('@ismenu')[0].extract()
            else:
                is_menu = 0
            index = index + 1

            if not is_menu:
                # title = li_str.xpath('div/h2[@class="dd-content "]/a/@title')[0].extract()
                title = li_str.xpath('div[@class="dd-content "]/a/@title')[0].extract()
                doc_link_arr.append({'tutorial': w3c_item['slug'],
                                     'is_menu': 0,
                                     'slug': slug,
                                     'name': title,
                                     'description': '',
                                     'link': link,
                                     'content': '',
                                     'tag': '',
                                     'position': index})
            else:
                # print(li_str)
                # exit()
                if li_str.xpath('div/h2[@class="menu-title"]/span/@title'):
                    title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
                else:
                    title = li_str.xpath('div/h2[@class="menu-title"]/a/@title')[0].extract()
                doc_link_arr.append({'tutorial': w3c_item['slug'],
                                     'is_menu': 1,
                                     'slug': slug,
                                     'name': title,
                                     'description': title + '_来自' + w3c_item['name'] + ',w3cxyz',
                                     'link': link,
                                     'content': '',
                                     'tag': '',
                                     'position': index})
                # print(doc_link_arr)
                #组装菜单下面的链接
                menu_doc_li = li_str.xpath('ol[@class="dd-list"]/li')
                for doc_li in menu_doc_li[0:]:
                    index = index + 1
                    doc_slug = doc_li.xpath('@data-id')[0].extract()
                    print(doc_slug)
                    if doc_slug == '1k8t1tbq':
                        break
                    doc_name = doc_li.xpath('div[@class="dd-content "]/a/@title')[0].extract()
                    # doc_link = ''
                    # if index == 42:
                    #     doc_link = str(doc_li.xpath('div[@class="dd-content "]/a/@href')[0].extract())
                    # else:
                    #     doc_link = 'http://www.w3cschool.cn' + str(doc_li.xpath('div[@class="dd-content "]/a/@href')[0].extract())
                    doc_link = str(doc_li.xpath('div[@class="dd-content "]/a/@href')[0].extract())
                    if doc_link.find('www.w3cschool.cn') == -1:
                        doc_link = 'http://www.w3cschool.cn' + doc_link
                    elif doc_link.find('www.w3cschool.cn') == 0:
                        doc_link = 'http://'+doc_link
                    doc_link_arr.append({'tutorial': w3c_item['slug'],
                                         'is_menu': 0,
                                         'slug': doc_slug,
                                         'name': doc_name,
                                         'description': '',
                                         'link': doc_link,
                                         'content': '',
                                         'tag': title,
                                         'position': index})
                    # print(doc_link_arr)
                    # exit()

        return self.recursive_parse_doc(doc_link_arr, w3c_item)


        #         w3c_item['tutorial_doc'].append({'tutorial_id': 1,
        #                                          'is_menu': is_menu,
        #                                          'slug': slug,
        #                                          'name': title,
        #                                          'description': title + '_来自' + w3c_item['name'] + ',w3cxyz',
        #                                          'content': '',
        #                                          'tag': '',
        #                                          'position': index})
        #         menu_doc_li = li_str.xpath('ol[@class="dd-list"]/li')
        #
        # index = 0
        # for li_str in li_list[0:]:
        #     slug = li_str.xpath('@data-id')
        #     is_menu = li_str.xpath('@ismenu')
        #
        #     if not is_menu:
        #         title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
        #     else:
        #         title = li_str.xpath('div/h2[@class="menu-title"]/span/@title')[0].extract()
        #         index = index+1
        #         w3c_item['tutorial_doc'].append({'tutorial_id':1,
        #                                          'is_menu':is_menu,
        #                                          'slug':slug,
        #                                          'name':title,
        #                                          'description':title+'_来自'+w3c_item['name']+',w3cxyz',
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
            les = tbd.pop(0)
            link = les['link']
            # print(les)
            # exit()
            yield scrapy.Request(url=link,
                                 meta={'tbd': tbd, 'w3c_item': w3c_item, 'les': les},
                                 callback=self.parse_doc,
                                 dont_filter=True)

    def parse_doc(self, response):
        w3c_item = response.meta['w3c_item']
        les = response.meta['les']
        tbd = response.meta['tbd']

        if les['is_menu'] == 1:
            w3c_item['tutorial_doc'].append(les)
        else:
            les['description'] = response.xpath('/html/head/meta[@name="description"]/@content')[0].extract()
            content_str = response.xpath('//div[@class="content-intro view-box"]')[0].extract()
            les['content'] = content_str[36:-6]
            w3c_item['tutorial_doc'].append(les)


        return self.recursive_parse_doc(tbd, w3c_item)


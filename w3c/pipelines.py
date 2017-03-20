# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class W3CPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):

    def __init__(self):

        self.dbpool = adbapi.ConnectionPool(
            'MySQLdb',
            db='w3c',
            host='127.0.0.1',
            user='root',
            passwd='',
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=True)



    def process_item(self, item, spider):
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item

    def _conditional_insert(self, tx, item):
        # create recode if doesn't exist.
        # all this block run on it's own thread

        # tx.execute("select * from `tbl_course` where id = %s", (item['id']))
        # result = tx.fetchone()
        # if result:
        #     log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
        # else:
            sql = """INSERT INTO `w3c_tutorial` (`tutorial_category_id`, `slug`, `name`, `description`, `img`, `img_path`, `content`, `position`)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            lis = (1,item['slug'], item['name'], item['description'], item['img'], item['img_path'], item['content'], item['position'])
            # print(lis)
            result = tx.execute(sql,lis)
            # if result:
            #     log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
            # else:

            print(item['tutorial_doc'])
            print('/n/n/n')
            for le in item['tutorial_doc']:
                sql = """INSERT INTO `w3c_tutorial_doc` (`tutorial`, `is_menu`, `slug`, `name`, `description`,  `content`, `tag`, `position`)
                                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                print(le)
                print('/n/n/n')
                params = ( le['tutorial'], le['is_menu'], le['slug'], le['name'], le['description'], le['content'], le['tag'], le['position'])
                tx.execute(sql, params)




    def handle_error(self, e):
        print ('handle_error')
        log.err(e)
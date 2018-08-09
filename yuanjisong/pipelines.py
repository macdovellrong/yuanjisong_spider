# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='ronglei12',
        charset='utf8',
        use_unicode=False
    )
    return conn

class YuanjisongPipeline(object):
    def process_item(self, item, spider):
        print('1')
        dbObject = dbHandle()
        print('2')
        cursor = dbObject.cursor()
        print('3')
        sql = 'insert into yuanjisong.job(url,title,cooperation,day_rate,total_rate,task_time,area1,area2,area3,requirement,status,participants) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            cursor.execute(sql, (item['url'], item['title'], item['cooperation'], item['day_rate'], item['total_rate'], \
                                 item['task_time'], item['area1'], item['area2'], item['area3'], item['requirement'], item['status'], item['participants']))
            print("aaaaaa")
            dbObject.commit()
            print("bbbbbb")
        except Exception as e:
            print("cccccc")
            print(e)
            dbObject.rollback()


        return item

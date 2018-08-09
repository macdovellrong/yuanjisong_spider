# -*- coding: utf-8 -*-
import scrapy


class MyclawerSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['bbs.fengniao.com']
    start_urls = ['http://bbs.fengniao.com/']

    def start_requests(self):
        # 全局变量
        pageDict = {'page': 99}
        pageGlobal = 99

        # 关注 pageIdx    循环内的变量
        for pageIdx in range(1,10):

            # 关注 pageDict   循环外的变量，相对于循环来说，是全局变量(可变)
            pageDict['page'] = pageIdx

            # 关注 pageGlobal   循环外的变量，相对于循环来说，是全局变量(不可变)
            pageGlobal = pageIdx

            # 关注 pageTemp   循环外的变量，相对于循环来说，是局部变量，每轮都会创建一个单独的变量
            pageTemp = pageIdx
            print("1========")
            yield scrapy.Request(
                url=f'http://bbs.fengniao.com/forum/forumdisplay.php?f=125&type=list&order=desc&sort=lastpost&page={pageIdx}',
                meta={'pageIdx': pageIdx, 'pageTemp': pageTemp, 'pageGlobal': pageGlobal, 'pageDict': pageDict, 'dont_redirect': True},
                callback=self.parse,
                errback=self.error
            )
            print("2========")

    def parse(self, response):
        print(f"=======parse url={response.url}, status={response.status}, meta={response.meta}")

    def error(self, response):
        pass
import scrapy
from scrapy_splash import SplashRequest
from yuanjisong.items import YuanjisongItem
import time

class YuanjisongSpider(scrapy.Spider):
    name = "yuanjisong"
    allowed_domains = ["yuanjisong.com"]
    start_urls = [
        #"https://www.yuanjisong.com/job/"
       "https://www.yuanjisong.com/job/101611"
    ]
    i = 612
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    }

    def parse(self, response):
        #self.parse_item(response)
        print("==1=======")
        YJS = YuanjisongItem()
        title_flag = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/h2/text()").extract()
        print("===2======")
        print(title_flag)
        print("====3=====")
        if title_flag:
            print("111")
            YJS['url'] = response.url
            YJS['title'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/h2/text()").extract()[
                0]
            YJS['cooperation'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/ul/li[2]/text()").extract()[0]
            YJS['day_rate'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[3]/div/ul/li[2]/text()").extract()[0]
            YJS['total_rate'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[4]/div/ul/li[2]/text()").extract()[0]
            YJS['task_time'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[5]/div/ul/li[2]/text()").extract()[0]
            YJS['area1'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[2]/text()").extract()[0]
            YJS['area2'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[3]/text()").extract()[0]
            YJS['area3'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[4]/text()").extract()[0]
            requirement_tmp = response.selector.xpath("/html/body/div[2]/div[1]/div[3]/div/div/p/text()").extract()
            YJS['requirement'] = ''
            for i in range(len(requirement_tmp)):
                YJS['requirement'] += requirement_tmp[i]
            YJS['status'] = response.selector.xpath("/html/body/div[2]/div[1]/div[4]/div/a/text()").extract()[0]
            print(YJS['status'])
            if YJS['status'] == '已完成':
                YJS['participants'] = 0
            elif YJS['status'] == '投递职位':
                YJS['participants'] = \
                response.selector.xpath("/html/body/div[2]/div[1]/div[4]/div/span/i/text()").extract()[0]

            print(YJS)
            yield YJS

        url = "https://www.yuanjisong.com/job/101{:0>3d}".format(self.i)
        print(url)
        time.sleep(5)
        yield scrapy.Request(url, callback=self.parse, headers=self.headers)
        self.i = self.i + 1

        if self.i > 1000:
            return


    def parse_item(self, response):
        print("==1=======")
        YJS = YuanjisongItem()
        title_flag = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/h2/text()").extract()
        print("===2======")
        print(title_flag)
        print("====3=====")
        if title_flag:
            print("111")
            YJS['url'] = response.url
            YJS['title'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/h2/text()").extract()[0]
            YJS['cooperation'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/div/ul/li[2]/text()").extract()[0]
            YJS['day_rate'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[3]/div/ul/li[2]/text()").extract()[0]
            YJS['total_rate'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[4]/div/ul/li[2]/text()").extract()[0]
            YJS['task_time'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[5]/div/ul/li[2]/text()").extract()[0]
            YJS['area1'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[2]/text()").extract()[0]
            YJS['area2'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[3]/text()").extract()[0]
            YJS['area3'] = response.selector.xpath("/html/body/div[2]/div[1]/div[2]/div[2]/div[6]/div/ul/li[4]/text()").extract()[0]
            requirement_tmp = response.selector.xpath("/html/body/div[2]/div[1]/div[3]/div/div/p/text()").extract()
            YJS['requirement'] = ''
            for i in range(len(requirement_tmp)):
                YJS['requirement'] += requirement_tmp[i]
            YJS['status'] = response.selector.xpath("/html/body/div[2]/div[1]/div[4]/div/a/text()").extract()[0]
            print(YJS['status'])
            if YJS['status'] == '已完成':
                YJS['participants'] = 0
            elif YJS['status'] == '投递职位':
                YJS['participants'] = response.selector.xpath("/html/body/div[2]/div[1]/div[4]/div/span/i/text()").extract()[0]

            print(YJS)
            yield YJS
            #return YJS

        #cooperation = response.selector.xpath("/text()").extract()


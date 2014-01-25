from scrapy.contrib.spiders import XMLFeedSpider
from hkaqhi.items import HkaqhiItem
from datetime import datetime

class Aqhi24Spider(XMLFeedSpider):
    name = 'aqhi24'
    allowed_domains = ['aqhi.gov.hk']
    start_urls = ['http://www.aqhi.gov.hk/epd/ddata/html/out/24aqhi_Eng.xml']
    #iterator = 'iternodes' # you can change this; see the docs
    #itertag = 'item' 
    itertag = 'item'
    tl = '%a, %d %b %Y %X +0800'
    newid = {'Central/Western': '45fd',
        'Eastern': 'e1a6',
        'Kwun Tong': 'fb71',
        'Sham Shui Po': 'db46',
        'Kwai Chung': '30e8',
        'Tsuen Wan': '228e',
        'Yuen Long': '1f2c',
        'Tuen Mun': '537c',
        'Tung Chung': 'f322',
        'Tai Po': '6e9c',
        'Sha Tin': '2c5f',
        'Tap Mun': '233a',
        'Causeway Bay': '5ca5',
        'Central': 'f9dd',
        'Mong Kok': '9c57'}
    oldid = {'Central/Western': '80',
        'Eastern': '73',
        'Kwun Tong': '74',
        'Sham Shui Po': '66',
        'Kwai Chung': '72',
        'Tsuen Wan': '77',
        'Yuen Long': '70',
        'Tuen Mun': '82',
        'Tung Chung': '78',
        'Tai Po': '69',
        'Sha Tin': '75',
        'Tap Mun': '76',
        'Causeway Bay': '71',
        'Central': '79',
        'Mong Kok': '81'}

    def parse_node(self, response, selector):
        i = HkaqhiItem()
        i['stationtype'] = selector.select('type/text()').extract()[0]
        i['name'] = selector.select('StationName/text()').extract()[0]
        i['time'] = int(datetime.strptime(selector.select('DateTime/text()').extract()[0], self.tl).strftime('%s'))
        i['aqhi'] = selector.select('aqhi/text()').extract()[0]
        i['id'] = self.newid[i['name']]
        i['stationid'] = self.oldid[i['name']]
        return i



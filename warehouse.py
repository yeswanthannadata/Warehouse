import scrapy
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.selector import Selector
import re

class Warehouse(BaseSpider):
    name = 'warehouse'
    start_urls = []
    url = 'http://www.indiawarehousing.in/projects/warehouse-godown-gujarat/page/%s/'
    
    for i in range(1,4):
        start_urls.append(url % i)
    
    def parse(self,response):
        sel = Selector(response)
        urls = sel.xpath('//div[@class="info"]//a//@href').extract()
        for url in urls:
            yield Request(url,self.parse_details)
    
    def parse_details(self,response):
        sel = Selector(response)
        title = ''.join(sel.xpath('//div[@class="col-md-9 col-sm-9"]//h1//text()').extract())
        images = ' <> '.join(sel.xpath('//div[@class="property-slide"]//img/@src').extract())
        location = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Location")]/following-sibling::dd/text()').extract()[0]
        pro_available = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Property Avai")]/following-sibling::dd/span/text()').extract()[0]
        pro = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Property")]/following-sibling::dd/text()').extract()[0]
        try:
            total = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Total")]/following-sibling::dd/text()').extract()[0]
        except:
            total = ''
        try:
	    squareft = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Sq.")]/following-sibling::dd/text()').extract()[0]
	except:
	    squareft = ''
        try:
            baths = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Baths")]/following-sibling::dd/text()').extract()[0]
        except:
            baths = ''
        try:
	    parking = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Parking")]/following-sibling::dd/text()').extract()[0]
	except:
	    parking = ''
        try:
	    water = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Water")]/following-sibling::dd/text()').extract()[0]
	except:
	    water = ''
        try:
	    security = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Security")]/following-sibling::dd/text()').extract()[0]
	except:
	    security = ''
        try:
            other_detail = sel.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Other")]/following-sibling::dd/text()').extract()[0]
        except:
            other_detail = ''
        aminities = ' <> '.join(sel.xpath('//section[@id="description"][2]//p/text()').extract())
        pro_doc = ' <> '.join(sel.xpath('//div[@class="property-detail"]/ol//li//a/@href').extract())
        description = sel.xpath('//div[@class="col-md-8 col-sm-12"]//section//text()').extract()[1]
	description = description.strip('Property Description')
	if description == '':
	    description = ' '.join(response.xpath('//div[@class="col-md-8 col-sm-12"]/section[@id="description"][1]/text()').extract()).replace('\n','').replace('\r','').strip()
	try:
	    property_floor = response.xpath('//div[@class="col-md-4 col-sm-12"]//dt[contains(text(),"Property Floor")]/following-sibling::dd/text()').extract()[0]
	except:
	    property_floor = ''
	youtube_url = ''.join(response.xpath('//div[@class="video"]/iframe/@src').extract())
	
	print 'url : ',response.url
	print 'title : ',title
	print 'location : ',location
	print 'property available for : ',pro_available
	print 'property type : ',pro
	print 'youtube url : ',youtube_url
	print 'total floor : ',total
	print 'property floor : ', property_floor
	print 'baths : ',baths
	print 'square feet: ',squareft
	print 'parking : ',parking
	print 'water : ',water
	print 'security : ',security
	print 'other details : ',other_detail
	print 'project document : ',pro_doc
	print 'description : ',description
	print 'images : ',images
	print 'aminities : ',aminities


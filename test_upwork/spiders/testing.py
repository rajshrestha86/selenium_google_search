# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.selector import Selector
import urllib3

class TestingSpider(scrapy.Spider):
    name = 'testing'
    allowed_domains = ['https://www.telluriderealestatecorp.com/our-agents/']
    start_urls = ['http://www.telluriderealestatecorp.com/our-agents/']


    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get(self.start_urls[0])
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "agents-container")))
        sleep(10)



    def parse(self, response):
       html=self.driver.page_source
       print("Scraping Data: ")
       html_page=Selector(type="html", text=html)
       agents=html_page.xpath('//*[@class="agents-agent"]')
       for agent in agents:
           agent_info=agent.xpath('.//*[@class="agent-info"]')
           name=agent_info.xpath('.//*[@itemprop="name"]/text()').extract_first()
           job_title=agent_info.xpath('.//*[class="title pipe-after"]/text()').extract_first()
           print(name)
       # print(self.driver.find_element_by_xpath('//*[@class="agents-agents"]').text)
       print('Daata Found')


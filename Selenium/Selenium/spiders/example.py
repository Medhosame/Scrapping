from codecs import code_page_decode
from lib2to3.pgen2.driver import Driver
from telnetlib import SE
from tkinter import Button
import scrapy
from selenium import webdriver
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector


class ExampleSpider(scrapy.Spider):
    name ='example'
    def start_requests(self):
            yield SeleniumRequest(
                url='https://en.wikipedia.org/wiki/Main_Page',
                wait_time=3,
                callback=self.parse
            )


    def parse(self, response):
            driver=response.meta['driver']
            # code_page=driver.page_source
            # print(code_page)
            champderecherche=driver.find_element_by_xpath("//input[@type='search']")
            champderecherche.send_keys('iphone 13')
            driver.implicitly_wait(5)

            boutton=driver.find_element_by_xpath("/html/body/div[7]/a")
            boutton.click()

            driver.implicitly_wait(3)
            print(driver.current_url)


            boutton500= driver.find_element.by_xpath("//a[@title='Afficher 500 résultats par page']")
            boutton500.click()

            code_page=driver.page_source
            response_cleaned=Selector(text=code_page)

            resultats= response_cleaned.xpath("//ul[@class='mv-search-results']/li")

            for resultat in resultats:
                lien= resultat.xpath('.//a/@href').get()
                title=resultat.xpath('//a/@title').get()
                yield{
                    'title':title,
                    'url':f'https://en.wikipedia.org{lien}'
                }
                #scrapy runspider example.py -o data.json
                #ctrl+k et ctrl f pour fomarter



import scrapy
import pickle

class MySpider(scrapy.Spider):
    name='corona_crawler'

    def start_requests(self):

        urls = []
        urls.append("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?/embed/fd0k_hbXWcQ")


        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        Coronavirus_Cases = response.xpath("//div[@class='maincounter-number']/span/text()").extract()[0]
        Deaths = response.xpath("//div[@class='maincounter-number']/span/text()").extract()[1]
        Recovered = response.xpath("//div[@class='maincounter-number']/span/text()").extract()[2]
        
        

        number_of_country = len(response.xpath("//tbody/tr/td[2]/a/text()").extract())

        Table_Info = [] #contain table
        
        this_Country =  response.xpath("//tbody/tr/td[2]/a/text()").extract()
        Country = list(dict.fromkeys(this_Country)) # in code asami keshvarhaye tekrari ra pak mikonad

        Total_Cases = response.xpath("//tbody/tr/td[3]/text()").extract()
        New_Cases = response.xpath("//tbody/tr/td[4]/text()").extract()
        Total_Deaths = response.xpath("//tbody/tr/td[5]/text()").extract()
        New_Deaths = response.xpath("//tbody/tr/td[6]/text()").extract()
        Total_Recoverd = response.xpath("//tbody/tr/td[7]/text()").extract()
        Active_Cases = response.xpath("//tbody/tr/td[9]/text()").extract()
        Serious_Critical = response.xpath("//tbody/tr/td[10]/text()").extract()
        Tot_Cases_1Mpop = response.xpath("//tbody/tr/td[11]/text()").extract()
        all_world = response.xpath("//tbody/tr[0]/td/text()").extract()

        Table_Info.append(Country)
        Table_Info.append(Total_Cases)
        Table_Info.append(New_Cases)
        Table_Info.append(Total_Deaths)
        Table_Info.append(New_Deaths)
        Table_Info.append(Total_Recoverd)
        Table_Info.append(Active_Cases)
        Table_Info.append(Serious_Critical)
        Table_Info.append(Tot_Cases_1Mpop)


        with open('static/DB/coronaDB.dat','wb') as f:
            pickle.dump(Coronavirus_Cases, f)
            pickle.dump(Deaths, f)
            pickle.dump(Recovered, f)
            pickle.dump(Table_Info, f)
        
            # f.write("hamashon:"+str(Coronavirus_Cases)+"\n"+"fotiha:"+str(Deaths)+"\n"+"bebhbod:"+str(Recovered)+"\n"+str(Table_Info))
        



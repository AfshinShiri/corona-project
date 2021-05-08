import subprocess

def run_spider():
    spider_name = "corona_crawler" #esme spidere aslimon
 
    subprocess.check_output(["scrapy","crawl",spider_name]) #in hamon code hast e khodet bara scrapy to cmd mizadi alan khodkar shode
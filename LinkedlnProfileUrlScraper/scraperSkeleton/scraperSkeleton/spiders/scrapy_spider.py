import scrapy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import drivers
import parameter


class QuotesSpider(scrapy.Spider):
    # Enter your Scrapy Spider name
    name = "LinkedlnCrawler"
    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 10
# Enter the web domain which have to scrape
    allowed_domains = ["linkedln.com"]
    handle_httpstatus_list = [999]

#This function will call the login function and then parse function
    def start_requests(self):
        drivers.driver.get(parameter.Url)
        time.sleep(2)
        search_query = drivers.driver.find_element('name', 'q')
        search_query.send_keys(parameter.Query)
        time.sleep(0.5)
        search_query.send_keys(Keys.RETURN)
        time.sleep(2)
        #Iterating over each Page on Google for related searchQuery
        for i in range(1, parameter.noOfUrls):
            organic_result = drivers.driver.find_elements('xpath', '//*[@class="yuRUbf"]/a[@href]')
            urlList= []
            for organic_url in organic_result:
                if not 'google' in organic_url.get_attribute("href"):
                    urlList.append(organic_url.get_attribute("href"))
            for profileUrl in urlList:
                column_name = 'linkedinProfileUrl'
                with open(parameter.fileName, 'a') as file1:
                    # Check if file is empty
                    if file1.tell() == 0:
                        file1.write(column_name + '\n')
                    # Write profileUrl data
                    file1.write(profileUrl + '\n')
                # print(url)
                yield scrapy.Request(url=profileUrl, callback=self.parse)
            nextButton = drivers.driver.find_element(By.XPATH,
                                             '/html/body/div[6]/div/div[11]/div/div[4]/div/div[2]/table/tbody/tr/td[12]/a/span[2]')
            drivers.driver.execute_script("arguments[0].click();", nextButton)
            time.sleep(0.5)
        drivers.driver.quit()

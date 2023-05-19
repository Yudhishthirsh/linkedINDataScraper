# linkedINDataScraper

1) Open the project and go to the LinkedlnProfileUrlScraper in your windows terminal or on linux operating system.

2) Install all the required python packages using below command: 

        pip install -r requirements.txt

3) Now go to the project directory using command below:

         cd LinkedlnProfileUrlScraper

4) After reaching LinkedlnProfileUrlScraper directory run below command to create the Python path over all the directories and files in the project.

   a) Command for Windows OS:

              command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" # Abslolute path of this "LinkedlnProfileUrlScraper" directory
  
       While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.

   b) Command for linux OS:   

              Command : export PYTHONPATH="Absolute Path of Directory" # Abslolute path of this "LinkedlnProfileUrlScraper" directory i your linux machine
  
      In this case there is no need to change backward slash.

5) Now, to scrape publicly available data from  LinkelIn you. Need to update the parameter.py file as given below.
   
   a) Url='https://www.google.com'

   b) SearchQuery : on the basis which we need to scrape data
        
         Query= 'site:linkedin.com/in/ AND'+'"City"'  #  In place of city, city name can be entered example : California

   c)Enter the relative path of your chromedriver (Ensure that there is chrome browser application installed in your machine)
    
          For Windows OS : chromeDriverPath = "./chromedriver.exe"
    
          For linux Machinne: chromeDriverPath = "./chromedriver" #In case when running this script in linux machine then need to update the chromeDriverPath.
          
    Need to save the latest chromedriver versions for both linux and windows OS in order to run script successfully.
    
    link for chromedrivers:  https://chromedriver.chromium.org/


   d)   noOfUrls = 1000 (How many Linkedin URLs need to be scraped)

6)Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below 

     Command : cd .\scraperSkeleton\

7) After reaching to the scraperSkeleton directory Run following command in terminal. 

     Command : scrapy crawl LinkedlnCrawler --nolog 

8) The outputfile of the scraped records is generated inside scraperSkeleton(outer) folder having random name which has nomenclature as given below.

     Output File name exaample : 20230518142546cfzl3.csv, 

     a) Where 20230518 is the date on which file is created

     b) Where 142546 followed by date is the time at which the file is created.
 
     c) After time there are 5 alphanumeric characters

Notes:
1) This automated Script run successfully in the scrapy framework and able to scrape approx. 500 Linkedin profile URLs after that google asking for captcha verification.

2) These Linked Profile URLs can be further used to scrape the profile data on linkedin.

3) In this case google is use to change tags and Xpath frequently, in order to overcome that element not found error need to update the Xpath and the tags. Otherwise this 

   script will not be locate the elements on web page and hence it will not able to scrape the data.

# linkedINDataScraper

1) Open the project and go to the LinkedlnProfileUrlScraper in your windows terminal or on linux operating system.

2) Install Python virtual environment, scrapy package in pycharm, install instaloader package using pip install instaloader , install pandas into the terminal using pip install pandas command in the Terminal or cli to install all these packages use command: 

        pip install -r requirements.txt

3) Now go to the project directory using command below:

         cd LinkedlnProfileUrlScraper

4) After reaching LinkedlnProfileUrlScraper directory run below command to create the Python path over all the directories and files in the project.

   a) Command for Windows OS:

       command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" (Abslolute path of this "LinkedlnProfileUrlScraper" directory)
  
       While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.

   b) Command for linux OS:   

      Command : export PYTHONPATH="Absolute Path of Directory"  (Abslolute path of this "LinkedlnProfileUrlScraper" directory i your linux machine)
  
      In this case there is no need to change backward slash.

5) Now,
   To scrape data from facebook public groups you need a facebook login. Need to add your credentials in parameter.py file.

   a)Linkedln_username = 'Enter the Username'
   
   b)Linkedln_password = 'Enter the password'
   
   c) Url='https://www.google.com'

   d) SearchQuery : on the basis which we need to scrape data
        
        Query= 'site:linkedin.com/in/ AND'+'"California"'

   e)Enter the relative path of your chromedriver (Ensure that there is chrome browser application installed in your machine)
    
        For Windows OS : chromeDriverPath = "./chromedriver.exe"
    
        For linux Machinne: chromeDriverPath = "./chromedriver" (In case when running this script in linux machine then need to update the chromeDriverPath.)


   f)   noOfUrls = 1000 (How many Linkedin URLs need to be scraped)

6)Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below 

    Command : cd .\scraperSkeleton\

7) After reaching to the scraperSkeleton directory Run following command in terminal. 

    Command : scrapy crawl fbCrawler --nolog 

8) The outputfile of the scraped records is generated inside scraperSkeleton(outer) folder having random name which has nomenclature as given below.

     Output File name exaample : 20230518142546cfzl3.csv, 

     a) Where 20230518 is the date on which file is created

     b) Where 142546 followed by date is the time at which the file is created.
 
     c) After time there are 5 alphanumeric characters

Notes:
1) This automated Script run successfully in the scrapy framework and able to scrape approx. 500 Linkedin profile URLs after that google asking for captcha verification.

2) These Linked Profile URLs can be further used to scrape the profile data on linkedin.

# linkedDataScraper

Open the project and go to the LinkedlnProfileUrlScraper in your windows terminal or on linux operating system.

install Python virtual environment, scrapy package in pycharm, install instaloader package using pip install instaloader , install pandas into the terminal using pip install pandas command in the Terminal or cli to install all these packages use command: 

pip install -r requirements.txt

Now go to the project directory using command below:

cd LinkedlnProfileUrlScraper

After reaching LinkedlnProfileUrlScraper directory run below command to create the Python path over all the directories and files in the project.

Command for Windows OS:

   command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" (Abslolute path of this "LinkedlnProfileUrlScraper" directory)
  
  While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.

Command for linux OS:   

   Command : export PYTHONPATH="Absolute Path of Directory"  (Abslolute path of this "LinkedlnProfileUrlScraper" directory i your linux machine)
  
  In this case there is no need to change backward slash.

Now,
To scrape data from facebook public groups you need a facebook login. Need to add your credentials in parameter.py file.

1)Facebook_username = 'Enter Your Email or Username'

2)Facebook_password = 'Password'

#url from which need to scrape data

3)URL= "https://www.facebook.com/groups/1225966920763001" #(sample URL)

#Enter the relative path of your chromedriver

4)Ensure that there is chrome browser application installed in your machine
    
    For Windows OS : relative_path = "./chromedriver.exe"
    
    For linux Machinne: relative_path = "./chromedriver" (In case when running this script in linux machine then need to update the chromeDriverPath.)

#Enter number of scrolls you want.

5)noOfScrolls = 100 

 Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below cd .\scraperSkeleton\

After reaching to the scraperSkeleton directory Run following command in terminal. 

Command : scrapy crawl fbCrawler --nolog 

The outputfile of the scraped records is generated inside scraperSkeleton(outer) folder having random name which has nomenclature as given below.

Output File name exaample : 20230518142546cfzl3.csv, 

1) Where 20230518 is the date on which file is created

2) Where 142546 followed by date is the time at which the file is created.
 
3) After time there are 5 alphanumeric characters

Notes:
1) This automated Script run successfully in the scrapy framework and able to scrape approx. 500 Linkedin profile URLs after that google asking for captcha verification.

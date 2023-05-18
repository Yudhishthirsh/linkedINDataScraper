import random
import string
import time
#Linkedln Credentials
import uuid
from datetime import datetime
Linkedln_username = 'Enter the Username'
Linkedln_password = 'Enter the password'
Url='https://www.google.com'
#SearchQuery : on the basis which we need to scrape data
Query= 'site:linkedin.com/in/ AND'+'"California"'
#Change only the city name for what location you searching the linkedln user profiles
#Enter the relative path of your chromedriver
relative_path = "./chromedriver.exe"

# Define the Random file name
length = 5
# Generate a random string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Get the current timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
fileName = timestamp + random_string + '.csv'
print("Your output file is: ",fileName )


#Enter number of Urls you want to extract.
noOfUrls = 1000

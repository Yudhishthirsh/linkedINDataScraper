from selenium import webdriver
import parameter

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(parameter.relative_path, chrome_options=chrome_options)
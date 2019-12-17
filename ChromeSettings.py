# coding=utf-8
from selenium import webdriver
from time import sleep

class ChromeSettings:
    def __init__(self,chrome_path):
        self.chrome_path=chrome_path

    def settingChrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        try:
            driver = webdriver.Chrome(self.chrome_path, chrome_options=chrome_options)
            return driver
        except:
            print ('Driver yuklemede hata...')

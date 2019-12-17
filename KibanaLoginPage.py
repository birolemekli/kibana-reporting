# coding=utf-8
from time import sleep

class KibanaLoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.__kibana_url="http://kibana:5601"
        self.__kibana_username="user"
        self.__kibana_password="password"

    def loginPage(self):
        print("Kibana'ya giriş yapılıyor...")
        self.driver.get(self.__kibana_url)
        sleep(4)
        try:

            _username = self.driver.find_element_by_id('sg.username')
            _username.clear()
            _username.send_keys(self.__kibana_username)
            sleep(0.5)
            _password = self.driver.find_element_by_id('sg.password')
            _password.clear()
            _password.send_keys(self.__kibana_password)
            sleep(0.5)
            button = self.driver.find_element_by_id('sg.login')
            button.click()
            sleep(0.5)
            return self.driver
        except:
            print ('Login sayfasinda bir hata meydana geldi...')

    def getKibanaUrl(self):
        return self.__kibana_url

    def setKibanaUrl(self,url):
        self.__kibana_url=url

    def getKibanaUserName(self):
        return self.__kibana_username

    def setKibanaUserName(self, username):
        self.__kibana_username = username

    def setKibanaPassword(self, password):
        self.__kibana_password = password

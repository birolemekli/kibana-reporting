# coding=utf-8
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScreenShotPage:
    def __init__(self,driver,screenshot_url):
        self.driver=driver
        self.screenshot_url=screenshot_url

    def screenShotPage(self):
        try:
            self.driver.get(self.screenshot_url)
            dashboard=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"kibana-body\"]/div/div[2]/div[1]/nav/a")))
            assert dashboard=="Dashboard"
            name = self.driver.find_element_by_xpath('//*[@id="kibana-body"]/div/div[2]/div[1]/nav/span').text
            print ('{0} yuklenmesi icin bekleniyor...'.format(name))
            full = self.driver.find_element_by_xpath('//*[@id="kibana-body"]/div/div[3]/div/div[2]/dashboard-app/kbn-top-nav/kbn-top-nav-helper/span/div[1]/div[1]/button/span/span')
            full.click()
            sleep(15)
            el = self.driver.find_element_by_tag_name('body')
            total_height = el.size["height"] + 1000
            self.driver.set_window_size(1920, total_height)
            return name
        except:
            print ('ScreenshotPage bölümünde hata meydana  geldi...')

    def screenShotSave(self,name):
        try:
            date = datetime.datetime.now()
            date = date.date()
            self.driver.save_screenshot('./screenshots/{0}-{1}.png'.format(str(date), name))
            sleep(1)
            image_name = (str(date) + "-" + name + ".png")
            return image_name
        except:
            print ('screenShotSave bölümünde hata meydana geldi...')
        finally:
            self.driver.quit()
            print ("Driver kapatildi...")
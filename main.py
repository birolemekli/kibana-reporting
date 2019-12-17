#!/usr/bin/env python
# coding=utf-8
import ChromeSettings,KibanaLoginPage,ScreenShotPage,Mail

# chromedriver hangi klasör içerisinde olduğu chromedriver_path içerisine belirtilmelidir
chromedriver_path="./chromedriver/chromedriver"

# Kibana->dashboard->share->permalink->short url ile alınan url bilgileri aşağıdaki dizine eklenir.
# Verilen dashboard sayısı kadar gider ss alır mail atar
short_screenshots=['http://kibana:5601/goto/bf63aebefc4cb85f3a85b23ec6207141']

# short_screenshots elemanı kadar rapor alır ve mail atar
for i in range(len(short_screenshots)):
    try:
        chrome = ChromeSettings.ChromeSettings(chromedriver_path)
        driver = chrome.settingChrome()
        kibanaLogin = KibanaLoginPage.KibanaLoginPage(driver)
        driver = kibanaLogin.loginPage()
        screenShot=ScreenShotPage.ScreenShotPage(driver,short_screenshots[i])
        name=screenShot.screenShotPage()
        image_name=screenShot.screenShotSave(name)
        mail = Mail.Mail(image_name)
        mail.sendMail()
    except:
        print ("Main.py for döngüsünde hata meydana geldi...")












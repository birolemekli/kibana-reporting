# Kibana Reportin

- Search guard login ekranı bulunan ELK yapısındaki Kibana arayüzündeki Dashboardların ekran görüntülerini alarak mail atan Python ve Selenium tabanlı bir geliştirmedir.

### İlk olarak selenium kurulumu ile başlayalım

`$ pip install selenium`

- chromedriver_path yeri belirtilir
- short_screenshots kibana dashboard short url bilgileri girilir. Birden fazla olan url , ile ayrılarak diziye eklenir.

- KibanaLoginPage dosyasındaki __kibana_url,__kibana_username,__kibana_password değişkenleri set set edilir.

##### Örnek KibanaLoginPage

        kibanaLogin = KibanaLoginPage.KibanaLoginPage(driver)
        kibanaLogin.setKibanaUrl("https://kibana:5601")
        kibanaLogin.setKibanaUserName("username")
        kibanaLogin.setKibanaPassword("password")
        driver = kibanaLogin.loginPage()

- Mail dosyasındaki __smtp_host, __mail_from, __mail_from_password, __mail_to değişkenleri set edilir.

##### Örnek Mail
        mail = Mail.Mail(image_name)
        mail.setFrom("mail@hotmail.com")
        mail.setFromPassword("password")
        mail.setHost("10.10.10.10:25")
        mail.setMailTo("send@hotmail.com,log@gmail.com,test@gmail.com")
        mail.sendMail()

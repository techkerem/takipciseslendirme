from gtts import gTTS
from playsound import playsound
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#buraya en son takipci sayinizi yazin
mem = 2022

x=1
while x<10:

    #@ kismindan sonra kendi kullanici adinizi koyun
    driver.get('https://www.tiktok.com/@krmersoz')

    #hata verirse chrome da kaynagi incele tusuna basip takipci sayiniza tiklayin ve copy full path diyip assagiya ekleyin
    takipci = driver.find_element("xpath", '/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong').text

    if int(takipci) > int(mem):

        #soylegecegi metin
        text_val = f"{'Hayırlı olsun yeni bir takipçi kazandın. Artik' + takipci + 'kişi seni takip ediyor. Çok teşekkür ederim!'}"
        language = 'tr'
        obj = gTTS(text=text_val, lang=language, slow=False)

        time.sleep(1)

        obj.save("temp.mp3")
        time.sleep(1)
        playsound("temp.mp3")

        mem = takipci

    #kac saniye aralikla kontrol ediyor
    time.sleep(1)

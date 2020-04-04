from selenium import webdriver
import time
from termcolor import colored,cprint
import getpass #getpass.getpass(prompt='Password: ', stream=None) ile komut satırında gözükmeyen şifre alınıyor.
from selenium.webdriver.common.keys import Keys #takipçi dialogunda scroll bar hareketi
import re # Verilen markerler arasındaki stringi bulmak için
import random # Rastgele süre ayarlamak için kullanıldı 
import urllib.request



class Instagram(object):
    def __init__(self):
        print()
        print("*********************")
        print(self.color("--- SEÇİM YAPINIZ ---",2))
        print("*********************")
        print()
        print("[+] 1. Fotoğraf indir ")
        print("[+] 2. Bir videoyu indir ")
        print("[+] 3. Tüm paylaşımaları indir ")
        print("[+] 4. Tüm paylaşımları beğen ")
        print(self.color("[+] 5. Tüm paylaşımları beğenmekten vazgeç ",1))
        print("[+] 6. Belirli bir paylaşımı beğen ")
        print(self.color("[+] 7. Belirli bir paylaşımı beğenmekten vazgeç ",1))
        print(self.color("[+] 8. Tüm paylaşımları beğenmekten vazgeç ",1))
        print(self.color("[+] 9. Bir kulanıcıyı engelle ",1))
        print("[+] 10. Bir kulanıcının engelini kaldır")
        print(self.color("[+] 11. Anasayfadaki tüm postlara yorum yap ",2))
        print(self.color("[+] 12. Seni takip etmeyenleri takipten çık ",1))
        print(self.color("[+] 13. Bir kullanıcının takip ettiği tüm kullanıcıları takip et ",3)) # OK
        print(self.color("[+] 14. Bir kulanıcıyı takipten çık",1))
        print("[+] 15. Bir kullanıcıyı takip et ") # OK
        print()
        print("*********************")

        self.selection = int(input("Seçiminiz(Sayı giriniz): "))
        self.selectFunc(self.selection)
      
    def startBrowser(self): # Selenium'u çalıştıran fonksiyon

        self.username_input = input("Kullanıcı adınız: ")

        self.password_input = input("Şifreniz: ")

        print("[*] Tarayıcı Başlatılıyor...")
        print("---------------------------")
        print("[*] İnstagrama giriş yapılıyor...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

        #executuble_path ile oynamayınız. chromedriver.exe'nin instagram.py ile aynı klasörde olması yeterli olacaktır.
        self.browser = webdriver.Chrome(executable_path=".\chromedriver.exe",chrome_options=options)

        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)

        self.loginInsta(self.username_input,self.password_input)



    def loginInsta(self,username_input,password_input): #İnstagrama giriş yapan fonksiyon


        self.username_page = self.browser.find_element_by_name("username")
        self.password_page = self.browser.find_element_by_name("password")
        self.username_page.send_keys(username_input)
        self.password_page.send_keys(password_input)
        time.sleep(2)

        self.login = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
        self.login.click()
        time.sleep(5)


   

        

    def color(self,message,durum):
        if durum==1:
            return colored(message,"red")
        elif durum==2:
            return colored(message,"green")
        elif durum==3:
            return colored(message,"blue")

    def selectFunc(self,selection):
        if selection ==1:
            resim = input("İndirmek istediğiniz resmin linki: ")
            self.startBrowser()
            self.browser.get(resim)
            img = self.browser.find_element_by_css_selector('img.FFVAD')
            src = img.get_attribute('src')

            # download the image
            urllib.request.urlretrieve(src, "resim.jpg")


            print()
        
        if selection ==2:
            print()
        
        if selection ==3:
            print()

        if selection ==4:
            print(4)

        if selection ==5:
            print()
            
        if selection ==6:
            print()
        
        if selection ==7:
            print()
        
        if selection ==8:
            print()

        if selection ==9:
            print()

        if selection ==10:
            print()
        
        if selection ==11:
            print()
        
        if selection ==12:
            self.randomTime = random.uniform(2, 5)
            self.startBrowser()
            self.browser.get("https://instagram.com/{}/".format(self.username_input))
            time.sleep(1.5)
            numFollowers=(self.browser.find_element_by_xpath("//li[2]/a/span").text) 
            numFollowings=int(self.browser.find_element_by_xpath("//li[3]/a/span").text)
            print("Takipçi sayısı: "+(numFollowers))
            print("Takip edilen kişi sayısı: "+str(numFollowings))

# -- Takip edilenlerin listesi
            followingsLink = self.browser.find_element_by_css_selector(' ul > li:nth-child(3) > a')
            followingsLink.click()
            time.sleep(2)
            followingsDialog = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowingsInList = len(followingsDialog.find_elements_by_css_selector('li'))
        
            followingsDialog.click()
            actionChain = webdriver.ActionChains(self.browser)
            #
            numFollowings = 100.4
            #
            while (numberOfFollowingsInList < int(numFollowings)):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.7)
                followingsDialog.click()
                numberOfFollowingsInList = len(followingsDialog.find_elements_by_css_selector('li'))
            
            
            count=1
            followingsList = []
            for user in followingsDialog.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                countPrint = "{}. takip edilen: ".format(count)
                cprint(countPrint+userLink,'blue'.format(count))
                count +=1
                followingsList.append(userLink)
                if (len(followingsList) == numFollowings):
                    break
            self.browser.get("https://instagram.com/{}/".format(self.username_input))
            time.sleep(3)
# -- Takipçi listesi
            followersLink = self.browser.find_element_by_css_selector(' ul > li:nth-child(2) > a')
            followersLink.click()
            time.sleep(2)
            followersDialog = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowingsInList = len(followersDialog.find_elements_by_css_selector('li'))
        
            followersDialog.click()
            actionChain = webdriver.ActionChains(self.browser)
            while (numberOfFollowingsInList < int(numFollowers)):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.7)
                followersDialog.click()
                numberOfFollowingsInList = len(followersDialog.find_elements_by_css_selector('li'))
            
            
            count=1
            followersList = []
            for user in followersDialog.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                countPrint = "{}. takipçi: ".format(count)
                cprint(countPrint+userLink,'blue'.format(count))
                count +=1
                followersList.append(userLink)
                if (len(followersList) == numFollowers):
                    break
 # -- Takipten çıkma           
            notFollowing = []

            for person in followingsList:
                if person  not in followersList:
                    notFollowing.append(person)
            
            for user in notFollowing:
                pattern = ".com/(.*?)/"
                username = re.search(pattern,user).group(1)
                print(username + " sizi takip etmiyor.")
                time.sleep(0.5)
                self.browser.get(user)
                time.sleep(self.randomTime)
                self.unfollowBtn = self.browser.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button")
                self.unfollowBtn.click()
                time.sleep(1)
                lastunFollowBtn = self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_")
                lastunFollowBtn.click()
                cprint(username + " kişisi takipten çıkıldı.",'green')
                time.sleep(1)
                
                
            self.browser.close()
            print(str(len(notFollowing)) + " kişi takipten çıkıldı.")
    
        if selection ==13:
            person = input("Takip ettiği kişileri takip etmek istediğiniz kişinin kullanıcı adı: ")
            self.startBrowser()
            time.sleep(2)
            self.browser.get("https://www.instagram.com/{}/".format(person))
            time.sleep(1)

            numFollows=(self.browser.find_element_by_xpath("//li[2]/a/span").text) 
            numFollowings=int(self.browser.find_element_by_xpath("//li[3]/a/span").text)
            print("Takipçi sayısı: "+(numFollows))
            print("Takip edilen kişi sayısı: "+str(numFollowings))
            
            followingsLink = self.browser.find_element_by_css_selector(' ul > li:nth-child(3) > a')
            followingsLink.click()
            time.sleep(2)
            followingsDialog = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
            numberOfFollowingsInList = len(followingsDialog.find_elements_by_css_selector('li'))
        
            followingsDialog.click()
            actionChain = webdriver.ActionChains(self.browser)
            while (numberOfFollowingsInList < int(numFollowings)):
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(0.7)
                followingsDialog.click()
                numberOfFollowingsInList = len(followingsDialog.find_elements_by_css_selector('li'))
            
            
            count=1
            followingsList = []
            for user in followingsDialog.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                countPrint = "{}. takipçi: ".format(count)
                cprint(countPrint+userLink,'blue'.format(count))
                count +=1
                followingsList.append(userLink)
                if (len(followingsList) == numFollowings):
                    break

            for following in followingsList:
                pattern = ".com/(.*?)/"
                username = re.search(pattern,following).group(1)
                print("Kullanıcı: "+username)
                self.browser.get(following)
                #Gizli Hesap Takibi
                if "This Account is Private" in self.browser.page_source:
                    follow_btn = self.browser.find_element_by_css_selector("button.BY3EC")
                    if follow_btn.text == 'Follow' or follow_btn.text == 'Follow Back':
                        follow_btn.click()
                        print("{} kullanıcısına başarıyla takip isteği gönderildi.".format(username))

                    elif follow_btn.text == 'Requested':
                        print("{} kullancısına zaten takip isteği gönderilmiş.".format(username))

                    else:
                        print("{} kullancısı zaten takip ediliyor".format(username))

                #Herkese açık hesap takibi
                else:
                    follow_btn = self.browser.find_element_by_css_selector("button._5f5mN")
                    if follow_btn.text == 'Follow' or follow_btn.text == 'Follow Back':
                        follow_btn.click()
                        print("{} kullanıcısı başarıyla takip edilmeye başlandı.".format(username))

                    else:
                        print("{} kullancısı zaten takip ediliyor".format(username))
            print("İşlem başarıyla tamamlandı !")

        if selection ==14:
            toUnFollow = input("Takipten çıkmak istediğiniz kişinin username'i: ")
            self.startBrowser()
            self.browser.get("https://www.instagram.com/{}/".format(toUnFollow))
            self.unfollowBtn = self.browser.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button")
            self.unfollowBtn.click()
            time.sleep(0.5)
            lastunFollowBtn = self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_")
            lastunFollowBtn.click()
            print(toUnFollow + " kişisi takipten çıkıldı.")
            self.browser.close()
            


        if selection ==15:
            toFollow = input("Takip edilecek kişinin username'i: ") #Takip edilecek kişi - Arama çubuğuna yaz
            self.startBrowser()
            self.browser.get("https://www.instagram.com/{}/".format(toFollow))
            time.sleep(3)

            #Gizli Hesap Takibi
            if "This Account is Private" in self.browser.page_source:
                follow_btn = self.browser.find_element_by_css_selector("button.BY3EC")
                if follow_btn.text == 'Follow' or follow_btn.text == 'Follow Back':
                    follow_btn.click()
                    print("{} kullanıcısına başarıyla takip isteği gönderildi.".format(toFollow))

                elif follow_btn.text == 'Requested':
                    print("{} kullancısına zaten takip isteği gönderilmiş.".format(toFollow))

                else:
                    print("{} kullancısı zaten takip ediliyor".format(toFollow))

            #Herkese açık hesap takibi
            else:
                follow_btn = self.browser.find_element_by_css_selector("button._5f5mN")
                if follow_btn.text == 'Follow' or follow_btn.text == 'Follow Back':
                    follow_btn.click()
                    print("{} kullanıcısı başarıyla takip edilmeye başlandı.".format(toFollow))

                else:
                    print("{} kullancısı zaten takip ediliyor".format(toFollow))



    #def ahmet(self):
        """
        • Bir fotoğraf indirme
        • Bir videoyu indirme
        • Tüm paylaşımları indirme
         """

        
    #def furkan(self):

        """
        • Tüm paylaşımları beğenme
        • Tüm paylaşımları beğenmekten vazgeçme
        • Belirli bir paylaşımı beğenme
        • Belirli bir paylaşımı beğenmekten vazgeçme
        """



    #def nesim(self):

        """
        • Bir kullanıcıyı engelleme
        • Bir kullanıcının engelini kaldırma
        • Postlara yorum yapma
         """



insta = Instagram()
    
    

 



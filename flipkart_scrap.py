import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


class Flip_scrap():

    def __init__(self):

        


        self.current_path = os.getcwd()
        self.url = 'https://www.flipkart.com'
        
        self.driver_path = os.path.join(os.getcwd(), 'chromedriver')
        self.driver = webdriver.Chrome(self.driver_path)

    def flip_load(self):

        self.driver.get(self.url)
        try:
            popup_close = self.driver.find_element_by_class_name('_29YdH8')
            popup_close.click()
            print('pop-up closed')
        except:
            pass
      
        search_query = self.driver.find_element_by_class_name('LM6RPg')
        search_query.send_keys('gaming laptop'  + '\n')
        time.sleep(2)
        page_html = self.driver.page_source
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def file_create(self):


        headings = ["Name", "Storage_details", "Screen_size", "Operating_system", "RAM", "Processor", "Warranty", "Price in Rupees"]
        self.file_csv = open('gaming_laptop_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=headings)
        self.mycsv.writeheader()

    def scrap_web(self):

        for j in range (9):
            
            time.sleep(1)
            gaming_laptop = (self.soup.find_all('div', class_='_3O0U0u'))
            for i in gaming_laptop:
                Name = i.find('img', class_='_1Nyybr')['alt']
                price = i.find('div', class_='_1vC4OE _2rQ-NK')
                details = i.find_all("li")
                processor = details[0].text
                ram = details[1].text
                opos = details[2].text
                storagesize = details[3].text
                screensize = details[4].text
                warrantydet= details[5].text

                price = price.text[1:]
                if 'cm' in screensize:
                    self.mycsv.writerow({"Name": Name, "Storage_details": storagesize, "Screen_size": screensize, "Operating_system": opos, "RAM": ram, "Processor": processor, "Warranty": warrantydet, "Price in Rupees": price})
                

            next_query = self.driver.find_element_by_xpath("//span[text()='Next']")
            next_query.click()
            time.sleep(2)

    def quitprocess(self):

        self.driver.quit()
        self.file_csv.close()

if __name__ == "__main__":

    Flip_scrap = Flip_scrap()
    Flip_scrap.flip_load()
    Flip_scrap.file_create()
    Flip_scrap.scrap_web()
    Flip_scrap.quitprocess()
  
    print("Mission Accomplished")

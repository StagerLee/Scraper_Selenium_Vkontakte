import pandas as pd
import time
from tkinter import N
from turtle import shearfactor
from xml.etree.ElementTree import Comment
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PATH = ChromeDriverManager().install()

driver = webdriver.Chrome()
actions = ActionChains(driver)

all = ["https://vk.com/vk_moscow"] #, "https://vk.com/aif_ru", 'https://vk.com/kpru', 'https://vk.com/spb.live']

Result = []
for one in all:
    driver.get(one)
    #Login table
    def x (a):
        a.click
    #Scroll
    for i in range (3000):
        actions.move_to_element(driver.find_element(By.CSS_SELECTOR, ' #footer_wrap')).click().perform()
        if 'Aug' in driver.find_elements(By.CSS_SELECTOR, ' .deep_active .PostHeader .rel_date')[-1].text:
            print("== END ==")
            break
        try:
            x(driver.find_element(By.CSS_SELECTOR, '.UnauthActionBox__close'))
        except:
            pass
        content = driver.find_elements(By.CSS_SELECTOR, ".deep_active")
        print(len(content))
        for i in content:
            try:
                Date = i.find_element(By.CSS_SELECTOR, '.PostHeader .rel_date').text
            except:
                continue
            try:
                Name_author = i.find_element(By.CSS_SELECTOR, '.PostHeader .author').text
            except:
                Name_author = None
            try:
                comment = i.find_element(By.CSS_SELECTOR, '.wall_text .wall_post_text').text.replace('\n\n','\n')
            except:
                continue
            try:
                image_comment = i.find_element(By.CSS_SELECTOR, '.wall_text .page_post_thumb_last_row').get_attribute('href')
            except:
                image_comment = None
            try:
                like = i.find_element(By.CSS_SELECTOR, '.PostButtonReactions__title').text
            except:
                like = None
            try:
                Shear = i.find_element(By.CSS_SELECTOR, '._share .PostBottomAction__count--withBg').text
            except:
                Shear = None
            try:   
                Sub_comment = []
                sub = i.find_elements(By.CSS_SELECTOR, '.wall_reply_text')
                for s in sub:
                    Sub_comment.append('--> ' + s.text.replace('\n', ''))
            except:
                Sub_comment = None
            try:
                image_sub_comment = []
                im = i.find_elements(By.CSS_SELECTOR, '.replies .page_post_thumb_last_row')
                for m in im:
                    image_sub_comment.append(m.get_attribute('href'),'\n')
            except:
                image_sub_comment = None

            try:
                x(driver.find_element(By.CSS_SELECTOR, '.UnauthActionBox__close'))
            except:
                pass
            
            yes = []
            if 'война' in comment or 'войска' in comment or 'бои' in comment or 'умер' in comment or 'атаки' in comment or 'русская атаки' in comment or 'Евросоюз' in comment or 'Укра' in comment or 'Украины' in comment or 'Донбасса' in comment or 'Воен' in comment or 'Воен операц' in comment:
                yes.append('Very')
            else:
                pass
            for k in Sub_comment:
                if 'война' in k or 'войска' in k or 'бои' in k or 'умер' in k or 'атаки' in k or 'русская атаки' in k or 'Евросоюз' in k or 'Укра' in k or 'Украины' in k or 'Донбасса' in k or 'Воен' in k or 'Воен операц' in k:
                    yes.append('Very')
                else:
                    pass
            print('=============')
            print('yes = ', yes)
            print('=============')
            if 'Very' not in yes:
                continue
            data = {'Name_author': Name_author, 'Date': Date, 'comment': comment, 'image_comment': image_comment, 'like': like, 'Share': Shear, 'Sub_comment': Sub_comment, 'image_sub_comment': image_sub_comment}
            print(data)
            Result.append(data)
        df = pd.DataFrame(Result)
        df.to_excel('test.xlsx', index=False)
    df = pd.DataFrame(Result)
    df.to_excel('test.xlsx', index=False)

            
        


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:23:26 2024

@author: admin
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time
import pandas as pd
from PIL import Image
from io import BytesIO



service = Service(executable_path=ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")

# start Chrome using the service keyword
driver = webdriver.Chrome(service=service, options=chrome_options)

# On renseigne l'URL à laquelle on veut accéder
url = "https://professeur-layton.fandom.com/fr/wiki/Cat%C3%A9gorie:%C3%89nigmes"
driver.get(url)
driver.execute_script("document.body.style.zoom = '25%'")
time.sleep(2)
enigmes = driver.find_elements(By.CLASS_NAME ,"category-page__member-link")
liste_lien = []
for elem in enigmes:
    #On transforme les éléments web scrappé pour n'obtenir que les liens href associés
    liste_lien.append(elem.get_attribute("href"))

time.sleep(5)


data = []
for lien in liste_lien :
    driver.get(lien)
    driver.execute_script("document.body.style.zoom = '55%'")
    title = driver.find_elements(By.XPATH ,'//*[@id="firstHeading"]/span')
    
    num_enigme = driver.find_elements(By.XPATH ,'//*[@id="mw-content-text"]/div/div[1]/div[2]/table/tbody/tr[4]/td')
    
    image_enigme = driver.find_element(By.XPATH ,'//*[@id="mw-content-text"]/div/div[1]/div[2]/table/tbody/tr[2]/td/div/div/a/img')
    image_url = image_enigme.get_attribute('src')
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    sommaire = driver.find_element(By.XPATH,'//*[@id="mw-toc-heading"]')
    driver.execute_script("arguments[0].scrollIntoView();", sommaire)
    time.sleep(2)
    
    enonce_title = driver.find_element(By.XPATH ,'//*[@id="Énoncé"]')
    indice_title = driver.find_element(By.XPATH ,'//*[@id="Indices"]')
    
    time.sleep(2)
    enigme = []
    '''
    for i in range(1,5):
        enigme_part = enonce_title.find_element(By.XPATH, f'following-sibling::p[{i}]')
        if  enigme_part!=indice_title :
            enigme_partext = enigme_part.text
            enigme.append(enigme_partext)
    
    enigme = enigme[:-1]
    '''
    enigme = driver.find_elements(By.XPATH, "//*[@id='mw-content-text']/div/p[preceding-sibling::p[contains(text(), 'Énoncé')] and following-sibling::p[contains(text(), 'Indices')]]")

    liste_indice = []
    #title_indice = driver.find_element(By.XPATH,'//*[@id="Indices"]')
    #driver.execute_script("arguments[0].scrollIntoView();", enonce_title)
    time.sleep(2)
    
    #indice1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mw-content-text"]/div/div[3]/div/div[1]/ul/li[2]')))
    #indice1.click()
    time.sleep(1)
    indice1_texte = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[3]/div/div[3]/div/p/text()')
    #indice1_texte = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[4]/div/div[3]')
    liste_indice.append(indice1_texte.text)
    print(enigme.text)
    print(indice1_texte)
    time.sleep(2)

    indice2 = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[3]/div/div[1]/ul/li[3]')
    indice2.click()
    indice2_texte = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[4]/div/div[4]/div/p')
    liste_indice.append(indice2_texte.text)
    time.sleep(2)

    indice3 = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[3]/div/div[1]/ul/li[4]')
    indice3.click()
    indice3_texte = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div/div[4]/div/div[5]/div/p')
    liste_indice.append(indice3_texte.text)

    
    reponse = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div/p[7]')

    # Append the collected data as a dictionary
    data.append({
        'Title': title,
        'Numéro': num_enigme,
        'Image': image,
        'Enigme': enigme,
        'Indices': liste_indice,
        'Solution': reponse
    })
df = pd.DataFrame(data)
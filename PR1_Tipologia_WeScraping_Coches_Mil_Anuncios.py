# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:25:06 2021

@author: Usuario
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #hasta que los elementos carguen
from selenium.webdriver.support import expected_conditions as EC #condicion esperada
from selenium.webdriver.common.by import By
import time
import pandas as pd


import warnings
warnings.filterwarnings('ignore')
#Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Usuario\\Documents\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)


driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

#Inicializar navegador
driver.get('https://www.milanuncios.com')



WebDriverWait(driver, 15)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.sui-AtomButton.sui-AtomButton--primary.sui-AtomButton--solid.sui-AtomButton--center'.replace(' ', '.'))))\
    .click()
    
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#form-search-suggester-input.sui-AtomInput-input.sui-AtomInput-input-m.sui-AtomInput-input--rounded')))\
    .send_keys('coche')


#<span class="ma-SharedAutosuggestListOption-Title"><span><em class="ma-SharedHighlightSubstringText-match">coche</em></span></span>

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'span.ma-SharedAutosuggestListOption-Title')))\
    .click()


#funciona con un artículo:
#/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/main/div[2]/article[1]/div/div[2]

#/html/body/div[1]/div[2]/div[3]
WebDriverWait(driver, 150)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div[2]/div[3]')))

full_path = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]')

texto_columnas = full_path.text

print(texto_columnas)


    
    


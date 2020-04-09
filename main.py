#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Automate Youtube

from selenium import webdriver #Importamos webdriver
from selenium.webdriver.common.keys import Keys #Uso del teclado
import time #Tiempo de espera

class BotYoutube():
    def __init__(self):
        self.driver = webdriver.Chrome() #Creamos chromedriver

    def link(self):
        self.driver.get("https://www.youtube.com/") #Accedemos a la URL.
        time.sleep(5) #Tiempo de espera
        
    def search_youtube(self):
        time.sleep(5)
        #Obtenemos la ruta del buscador mediante 'xpath':
        btn_search = self.driver.find_element_by_xpath('//*[@id="search"]')
        btn_search.send_keys(self.terminal) #Escribimos en el terminal
        btn_search.send_keys(Keys.ENTER) #Le damos ENTER
        time.sleep(5)

    def list_one(self):
        time.sleep(5)
        music = self.driver.find_element_by_xpath('//*[@id="dismissable"]')
        music.click()
    
    def search_terminal(self):
        # Escribimos en el terminal.
        self.terminal = str(input("Buscar: "))

    def run(self):
        while True: # Repeticion infinita.
            self.search_terminal()
            self.link()
            self.search_youtube()
            self.list_one()

            

if __name__ == '__main__':
    bot = BotYoutube() # Objecto.
    bot.run() # Corremos el Bucle run().

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep
from random import randrange
from tkinter import *
from tkinter import messagebox as MessageBox


def test(msg, msg1):
    MessageBox.showinfo("Prueba",msg) # título, mensaje
    MessageBox.showinfo("Link","Para mayor información consulta el siguiente link gracias: " + msg1) # título, mensaje

class Hello (unittest.TestCase):
    
    @classmethod
    def setUpClass (cls): #ejecuta todo lo necesario antes de hacer una prueba
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = cls.driver
        driver = cls.driver        
        driver.get('https://google.com')

    def test_hello(self): #Acciones para automatizar
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('música moderna')
        search_field.submit()
        
        number_random = randrange(9,10)
        articule_search = driver.find_element_by_xpath(f'//*[@id="rso"]/div[4]/div/div/div[2]/div[1]').text
        articule_link = driver.find_element_by_xpath(f'//*[@id="rso"]/div[3]/div/div/div[1]/a/div').text
                
        test(articule_search,articule_link)

    @classmethod
    def tearDown(cls): #Acciones para finalizar (Cerra la ventana del navegador)
        cls.driver.quit()


if __name__ == '__main__':    
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'report', report_name = 'hello-report'))

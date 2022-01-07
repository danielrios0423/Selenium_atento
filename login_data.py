import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

from time import sleep

class login_data(unittest.TestCase):
    
    @classmethod
    def setUpClass (cls): #ejecuta todo lo necesario antes de hacer una prueba
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = cls.driver    
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Form Authentication').click()

    def test_login(self): #Acciones para automatizar
        driver = self.driver
        login_user = driver.find_element_by_name('username')
        login_user.clear()
        login_user.send_keys('tomsmith')

        login_password = driver.find_element_by_name('password')
        login_password.clear()
        login_password.send_keys('SuperSecretPassword!')
        login_password.submit()

        sleep(2)

        verification_login = driver.find_element_by_xpath('//*[@id="content"]/div/h2').text
        if verification_login == 'Secure Area':
            print('holaaaaaaaaa')
            driver.find_element_by_link_text('Logout').click()
       
        sleep(1)

    @classmethod
    def tearDown(cls): #Acciones para finalizar (Cerra la ventana del navegador)        
        cls.driver.quit()

if __name__ == '__main__':    
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'report', report_name = 'login-data-report'))

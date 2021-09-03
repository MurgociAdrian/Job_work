import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class TestScripts:

    
    def __init__(self):
        
        self.driver = None


    def dec_check_func(f):

        def inner_f(self):

            self.driver = webdriver.Chrome('C:/Users/Adrian23/PycharmProjects/ex_1/chromedriver.exe')
            self.driver.maximize_window()

            try:
                f(self)
            except Exception as e:
                print(e)
            finally:
                self.driver.close()

        return inner_f


    @dec_check_func
    def get_last_py_release(self):

        self.driver.get('https://www.python.org/')

        a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[@id='downloads']")))
        ActionChains(self.driver).move_to_element(a).perform()
        self.driver.find_element_by_xpath("//ul[@class='subnav menu']/li[@class='tier-2 element-1']"
                                          "/a[text() ='All releases']").click()

        rel_list = self.driver.find_elements_by_xpath("//div[@class='row download-list-widget']"
                                                      "/ol[@class='list-row-container menu']/li")
        last_rel = rel_list[0].find_elements_by_xpath("//span[@class='release-number']/a")

        print(last_rel[0].text)


    @dec_check_func
    def check_for_5_ex(self):

        self.driver.get('https://www.python.org/')

        search_box = self.driver.find_element_by_xpath("//input[@id='id-search-field']")
        search_box.send_keys('decorator')
        search_box.send_keys(Keys.RETURN)

        results_list = self.driver.find_elements_by_xpath("//ul[@class='list-recent-events menu']/li")
        results_list[0].find_element_by_xpath("//h3/a").click()

        self.driver.find_element_by_xpath("//ul[@class='simple']/li/a[text() = 'Examples']").click()

        nr_ex = self.driver.find_elements_by_xpath("//div[@id='examples']/ol[@class='arabic']/li")   # $x in cons

        if len(nr_ex) == 5:
            print("Ok, 5 elem.")
        else:
            print("Not ok")



if __name__ == "__main__":

    ses1 = TestScripts()
    ses1.get_last_py_release()
    ses1.check_for_5_ex()


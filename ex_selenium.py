import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class ClassPOM:


    @staticmethod
    def open_downloads_dropdown_submenu(driver_name):

        a = WebDriverWait(driver_name, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[@id='downloads']")))
        ActionChains(driver_name).move_to_element(a).perform()


    @staticmethod
    def click_all_releases_element(driver_name):

        driver_name.find_element_by_xpath("//ul[@class='subnav menu']/li[@class='tier-2 element-1']"
                                          "/a[text() ='All releases']").click()


    @staticmethod
    def return_last_release_version(driver_name):

        rel_list = driver_name.find_elements_by_xpath("//div[@class='row download-list-widget']"
                                                      "/ol[@class='list-row-container menu']/li")
        return rel_list[0].find_elements_by_xpath("//span[@class='release-number']/a")


    @staticmethod
    def search_in_box(driver_name, key_name):

        search_box = driver_name.find_element_by_xpath("//input[@id='id-search-field']")
        search_box.send_keys(key_name)
        search_box.send_keys(Keys.RETURN)


    @staticmethod
    def click_first_search_result(driver_name):

        results_list = driver_name.find_elements_by_xpath("//ul[@class='list-recent-events menu']/li")
        results_list[0].find_element_by_xpath("//h3/a").click()


    @staticmethod
    def click_examples_from_content(driver_name):

        driver_name.find_element_by_xpath("//ul[@class='simple']/li/a[text() = 'Examples']").click()


    @staticmethod
    def return_nr_of_examples(driver_name):

        return driver_name.find_elements_by_xpath("//div[@id='examples']/ol[@class='arabic']/li")   # $x in cons



class TestScripts:

    
    def __init__(self):
        
        self.driver = None


    def dec_check_func(f):

        def inner_f(self):

            try:
                self.driver = webdriver.Chrome('C:/Users/Adrian23/PycharmProjects/ex_1/chromedriver.exe')
                self.driver.maximize_window()
                self.driver.get('https://www.python.org/')
                f(self)
            except Exception as e:
                print(e)
            finally:
                self.driver.close()

        return inner_f


    @dec_check_func
    def get_last_py_release(self):

        ClassPOM.open_downloads_dropdown_submenu(self.driver)
        ClassPOM.click_all_releases_element(self.driver)

        list_versions = ClassPOM.return_last_release_version(self.driver)

        print(list_versions[0].text)


    @dec_check_func
    def check_for_5_ex(self):

        ClassPOM.search_in_box(self.driver, 'decorator')

        ClassPOM.click_first_search_result(self.driver)

        ClassPOM.click_examples_from_content(self.driver)

        nr_ex = ClassPOM.return_nr_of_examples(self.driver)

        if len(nr_ex) == 5:
            print("Ok, 5 elem.")
        else:
            print("Not ok")



if __name__ == "__main__":

    ses1 = TestScripts()
    ses1.get_last_py_release()
    ses1.check_for_5_ex()


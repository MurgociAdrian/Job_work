from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class ParentClassPOM:


    GLOBAL_DRIVER_OBJ = None


    def __init__(self):

        self.driver_obj = ParentClassPOM.GLOBAL_DRIVER_OBJ


    def initiate_browser_instance(self):

        self.driver_obj = webdriver.Chrome('C:/Users/agmurgoci/PycharmProjects/ex_1/chromedriver.exe')
        self.driver_obj.maximize_window()
        self.driver_obj.get('https://www.python.org/')
        ParentClassPOM.GLOBAL_DRIVER_OBJ = self.driver_obj


    def close_browser_instance(self):

        self.driver_obj.close()
        ParentClassPOM.GLOBAL_DRIVER_OBJ = None



class MainPage(ParentClassPOM):


    def search_in_box(self, key_name):
        search_box = self.driver_obj.find_element_by_xpath("//input[@id='id-search-field']")
        search_box.send_keys(key_name)
        search_box.send_keys(Keys.RETURN)


    def open_dropdown_submenu(self, submenu_name):
        dropdown_submenu = WebDriverWait(self.driver_obj, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@id='" + submenu_name + "']")))
        ActionChains(self.driver_obj).move_to_element(dropdown_submenu).perform()


    def click_element_from_dropdown_submenu(self, element_name):
        self.driver_obj.find_element_by_xpath(f"//ul[@class='subnav menu']/li[@class='tier-2 element-1']"
                                              f"/a[text() ='{element_name}']").click()



class ReleasePage(ParentClassPOM):


    def return_specific_first_row_from_py_table(self, column):

        return self.driver_obj.find_element_by_xpath(f"//ol[@class='list-row-container menu']/li"
                                                     f"/span[@class='{column}']")


    def return_last_release_version(self):

        rel_list = self.driver_obj.find_elements_by_xpath("//div[@class='row download-list-widget']"
                                                          "/ol[@class='list-row-container menu']/li")
        return rel_list[0].find_element_by_xpath("//span[@class='release-number']/a").text


    def search_string_in_specific_release_table(self, column, string_to_search):

        list_rel_table = self.driver_obj.find_element_by_xpath("//div[@class='row download-list-widget']"
                                                               "/ol[@class='list-row-container menu']")
        list_rel_nr = list_rel_table.find_elements_by_xpath(f"//li/span[@class='{column}']/a")

        for item in list_rel_nr:

            if string_to_search in item.text:
                return True

        return False


    def return_date_for_specific_version(self, string_last_py_ver):

        list_rel_table = self.driver_obj.find_element_by_xpath("//div[@class='row download-list-widget']"
                                                               "/ol[@class='list-row-container menu']")
        list_rel_nr = list_rel_table.find_elements_by_xpath("//li/span[@class='release-number']/a")
        list_rel_date = list_rel_table.find_elements_by_xpath("//li/span[@class='release-date']")

        list_comb_rel_nr_date = zip(list_rel_nr, list_rel_date)

        for item in list_comb_rel_nr_date:
            if string_last_py_ver in item[0].text:
                return item[1].text

        return '''Version not found'''



class SearchResultPage(ParentClassPOM):

    def click_first_search_result(self):
        self.driver_obj.find_element_by_xpath("//ul[@class='list-recent-events menu']/li/h3/a").click()



class ResultPage(ParentClassPOM):

    def click_hyperlink_from_content(self, chapter_name):
        self.driver_obj.find_element_by_xpath(f"//ul[@class='simple']/li/a[text() = '{chapter_name}']").click()

    def return_count_of_paragraphs(self, chapter_name):
        return len(self.driver_obj.find_elements_by_xpath(f"//div[@id='{chapter_name}']/ol[@class='arabic']/li"))
        # $x in cons

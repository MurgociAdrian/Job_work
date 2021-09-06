import time
from datetime import datetime
from dateutil import parser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class ParentClassPOM:


    def __init__(self, driver_obj):
        self.driver_obj = driver_obj



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
        return rel_list[0].find_element_by_xpath("//span[@class='release-number']/a")


    def search_string_in_specific_release_table(self, column, string_to_search):

        list_rel_table = self.driver_obj.find_element_by_xpath("//div[@class='row download-list-widget']"
                                                               "/ol[@class='list-row-container menu']")
        list_rel_nr = list_rel_table.find_elements_by_xpath(f"//li/span[@class='{column}']/a")

        for item in list_rel_nr:

            if string_to_search in item.text:
                return True


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
        return self.driver_obj.find_elements_by_xpath(f"//div[@id='{chapter_name}']/ol[@class='arabic']/li")
        # $x in cons



class TestScripts:


    def __init__(self):

        self.driver = None


    def dec_check_func(f):

        def inner_f(self):

            try:
                self.driver = webdriver.Chrome('C:/Users/agmurgoci/PycharmProjects/ex_1/chromedriver.exe')
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

        main_page = MainPage(self.driver)
        main_page.open_dropdown_submenu("downloads")
        main_page.click_element_from_dropdown_submenu("All releases")

        release_page = ReleasePage(self.driver)

        last_version = release_page.return_last_release_version()

        print(last_version.text)
        print(" ")


    @dec_check_func
    def check_for_5_ex(self):

        main_page = MainPage(self.driver)
        main_page.search_in_box('decorator')

        search_result_page = SearchResultPage(self.driver)
        search_result_page.click_first_search_result()

        result_page = ResultPage(self.driver)
        result_page.click_hyperlink_from_content("Examples")

        nr_ex = result_page.return_count_of_paragraphs("examples")

        if len(nr_ex) == 5:
            print("Ok, 5 elem.")
        else:
            print("Not ok")


    @dec_check_func
    def check_coresp_rel_for_latest_py_version(self):

        main_page = MainPage(self.driver)
        main_page.open_dropdown_submenu("downloads")
        main_page.click_element_from_dropdown_submenu("All releases")

        release_page = ReleasePage(self.driver)
        last_py_version = release_page.return_specific_first_row_from_py_table("release-version")
        bool_coresp = release_page.search_string_in_specific_release_table("release-number", last_py_version.text)

        if bool_coresp is True:
            print("There is a corresponding ....\n")
        else:
            print("No corresponding .... \n")


    @dec_check_func
    def check_rel_date_after_py_rel(self):

        main_page = MainPage(self.driver)
        main_page.open_dropdown_submenu("downloads")
        main_page.click_element_from_dropdown_submenu("All releases")

        release_page = ReleasePage(self.driver)
        obj_last_py_vers_date = release_page.return_specific_first_row_from_py_table("release-start")
        obj_last_py_version = release_page.return_specific_first_row_from_py_table("release-version")
        date_last_py_vers = datetime.strptime(obj_last_py_vers_date.text, "%Y-%m-%d")

        string_last_rel_date = release_page.return_date_for_specific_version(obj_last_py_version.text)
        date_last_rel = parser.parse(string_last_rel_date)

        if date_last_py_vers < date_last_rel:
            print("OK! -> The date for latest release version (coresp to latest py vers) is more recently. ")
        else:
            print("Error!")



if __name__ == "__main__":
    ses1 = TestScripts()
    ses1.get_last_py_release()
    ses1.check_coresp_rel_for_latest_py_version()
    ses1.check_for_5_ex()
    ses1.check_rel_date_after_py_rel()

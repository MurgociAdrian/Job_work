import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



class ParentClassPOM:


    GLOBAL_DRIVER_OBJ = None


    def __init__(self):

        self.driver_obj = ParentClassPOM.GLOBAL_DRIVER_OBJ


    def initiate_browser_instance(self):

        self.driver_obj = webdriver.Chrome('C:/Users/Adrian23/PycharmProjects/ex_1/chromedriver.exe')
        self.driver_obj.maximize_window()
        self.driver_obj.get('https://demoqa.com/text-box')

        ParentClassPOM.GLOBAL_DRIVER_OBJ = self.driver_obj


    def close_browser_instance(self):

        time.sleep(1)
        self.driver_obj.close()
        ParentClassPOM.GLOBAL_DRIVER_OBJ = None


    def close_bottom_ad(self):

        self.driver_obj.find_element_by_xpath("//div[@id='fixedban']/div/div/a[@id='close-fixedban']").click()
        print("Bottom ad is closed.")


    def check_link_is_reachable_for_right_side_ad(self):

        obj_right_side_ad1_link = self.driver_obj.find_element_by_xpath("//div[@classname='Advertisement-1']/a[@href]")
        r = requests.get(obj_right_side_ad1_link.get_attribute("href"))
        if r.status_code == 200:
            print("Ad_1 (right side ad) link is reachable")
        else:
            r.raise_for_status()


    def click_element_from_left_pannel_menu(self, element_name):

        self.driver_obj.find_element_by_xpath(f"//div[@class='left-pannel']//span[text()='{element_name}']").click()



class TextBoxPage(ParentClassPOM):


    LIST_AVAILABLE_ID_FOR_TEXTBOX = ["userName", "userEmail", "currentAddress", "permanentAddress"]


    def write_in_textbox(self, text_box_name, text_to_write):

        html_tag = "BadTag!"

        if text_box_name == TextBoxPage.LIST_AVAILABLE_ID_FOR_TEXTBOX[0] or \
           text_box_name == TextBoxPage.LIST_AVAILABLE_ID_FOR_TEXTBOX[1]:
            html_tag = "input"
        elif text_box_name == TextBoxPage.LIST_AVAILABLE_ID_FOR_TEXTBOX[2] or \
             text_box_name == TextBoxPage.LIST_AVAILABLE_ID_FOR_TEXTBOX[3]:
            html_tag = "textarea"
        else:
            print("Wrong textbox name! Options are: userName, userEmail, currentAddress, permanentAddress")

        text_box = self.driver_obj.find_element_by_xpath(f"//form[@id='userForm']//{html_tag}[@id='{text_box_name}']")

        text_box.clear()
        text_box.send_keys(text_to_write)


    def click_submit_button(self):

        ActionChains(self.driver_obj).move_to_element(
                                      self.driver_obj.find_element_by_xpath(
                                      "//div[@class='sidebar-content pattern-backgound shadow widget-divider-off']")).perform()
        self.driver_obj.find_element_by_xpath("//button[@id='submit']").click()

        # check if actually did something
        try:
            self.driver_obj.find_element_by_xpath("//form[@id='userForm']/div[@id='output']/"
                                                  "div[@class='border col-md-12 col-sm-12']")
        except NoSuchElementException:
            return False

        return True


    def check_if_answer_is_shown(self, list_with_textbox_written_text=None):


        list_shown_answer = self.driver_obj.find_elements_by_xpath("//form[@id='userForm']/div[@id='output']"
                                                                   "/div[@class='border col-md-12 col-sm-12']/p")

        if list_with_textbox_written_text is None:
            list_with_textbox_written_text = TextBoxPage.return_list_with_current_textbox_info(self)

        for i, written_text in enumerate(list_with_textbox_written_text):
            if written_text not in list_shown_answer[i].text:
                return False

        return True


    def return_list_with_current_textbox_info(self):

        list_to_return = []
        html_tag = "input"
        for i, id_name in enumerate(TextBoxPage.LIST_AVAILABLE_ID_FOR_TEXTBOX):
            if i == 2:
                html_tag = "textarea"
            list_to_return.append(self.driver_obj.find_element_by_xpath(f"//form[@id='userForm']//"
                                                                        f"{html_tag}[@id='{id_name}']").get_attribute('value'))

        return list_to_return



class CheckBoxPage(ParentClassPOM):


    LIST_WITH_SELECTED_NAMES = []


    def click_expand_or_collapse_all_button(self, button_name):

        self.driver_obj.find_element_by_xpath(f"//div[@class='body-height']//button[@title='{button_name}']").click()


    def check_if_there_is_something_expanded(self):

        try:
            self.driver_obj.find_element_by_xpath("//div[@class='check-box-tree-wrapper']"
                                                  "//li[@class='rct-node rct-node-parent rct-node-expanded']")
        except NoSuchElementException:
            return False

        return True


    def return_displayed_results(self):

        try:
            obj_list_with_displayed_text = self.driver_obj.find_elements_by_xpath("//div[@class='check-box-tree-wrapper']"
                                                                                  "//div[@id='result']"
                                                                                  "/span[@class='text-success']")
        except NoSuchElementException:
            print("Element not found or nothing is displayed.")
            return False

        list_with_displayed_text = []
        for item in obj_list_with_displayed_text:
            list_with_displayed_text.append(item.text)

        if not list_with_displayed_text:
            return False
        else:
            return list_with_displayed_text


    def make_action_on_box_item(self, item_name, action_name):

        if action_name == "Click":
            self.driver_obj.find_element_by_xpath(f"//label[@for='tree-node-{item_name}']").click()
            if item_name in CheckBoxPage.LIST_WITH_SELECTED_NAMES:
                CheckBoxPage.LIST_WITH_SELECTED_NAMES.remove(item_name)
            else:
                CheckBoxPage.LIST_WITH_SELECTED_NAMES.append(item_name)
            return True

        if action_name == "Toggle":
            all_visible_elements = self.driver_obj.find_elements_by_xpath("//span[@class='rct-text']")
            for item in all_visible_elements:
                try:
                    item.find_element_by_xpath(f"label[@for='tree-node-{item_name}']")
                except NoSuchElementException:
                    continue
                else:
                    item.find_element_by_xpath(f"button[@aria-label='{action_name}']").click()
                    return True

        return False


    @staticmethod
    def check_if_all_selected_are_displayed(list_with_displayed_results):

        for item in CheckBoxPage.LIST_WITH_SELECTED_NAMES:
            if item in list_with_displayed_results:
                if item == 'home':
                    # trebuie luate toate cazurile .....
                    break
                else:
                    continue
            else:
                print(f"Item {item} is not displayed.")
                return False

        return True



class RadioButtonPage(ParentClassPOM):


    def click_radio_button_and_check_displayed(self, button_name):

        self.driver_obj.find_element_by_xpath(f"//label[@for='{button_name}Radio']").click()
        try:
            displayed_string = self.driver_obj.find_element_by_xpath("//p[@class='mt-3']").text
        except NoSuchElementException:
            print("Pressed button did nothing.")
            return None

        if displayed_string.lower() == f"you have selected {button_name}":
            return True
        else:
            print("Displayed text is not identical with what was expected after the button was pressed.")
            return False



class WebTablesPage(ParentClassPOM):
    pass


class ButtonsPage(ParentClassPOM):


    def check_double_click_me_button(self):

        obj_double_click_button = self.driver_obj.find_element_by_xpath("//button[@id='doubleClickBtn']")
        obj_double_click_button.click()
        ActionChains(self.driver_obj).context_click(obj_double_click_button).perform()
        try:
            self.driver_obj.find_element_by_xpath("//p[@id='doubleClickMessage']")
        except NoSuchElementException:
            pass
        else:
            print("Double Click Button worked for a simple left/right click.")
            return False

        ActionChains(self.driver_obj).double_click(obj_double_click_button).perform()
        if "You have done a double click" == self.driver_obj.find_element_by_xpath("//p[@id='doubleClickMessage']").text:
            return True
        else:
            print("Expected message is not the same with displayed message.")
            return False


    def check_right_click_me_button(self):

        obj_right_click_button = self.driver_obj.find_element_by_xpath("//button[@id='rightClickBtn']")
        obj_right_click_button.click()
        ActionChains(self.driver_obj).double_click(obj_right_click_button).perform()
        try:
            self.driver_obj.find_element_by_xpath("//p[@id='rightClickMessage']")
        except NoSuchElementException:
            pass
        else:
            print("Right Click Button worked for a click/double-click.")
            return False

        ActionChains(self.driver_obj).context_click(obj_right_click_button).perform()
        if "You have done a right click" == self.driver_obj.find_element_by_xpath("//p[@id='rightClickMessage']").text:
            return True
        else:
            print("Expected message is not the same with displayed message.")
            return False


    def check_click_me_button(self):

        obj_list_buttons = self.driver_obj.find_elements_by_xpath("//div[@class='mt-4']")
        obj_click_button = None
        for item in obj_list_buttons:
            if item.text == "Click Me":
                obj_click_button = item

        ActionChains(self.driver_obj).context_click(obj_click_button).perform()
        try:
            self.driver_obj.find_element_by_xpath("//p[@id='dynamicClickMessage']")
        except NoSuchElementException:
            pass
        else:
            print("Click Button worked for a right click.")
            return False

        obj_click_button.find_element_by_xpath("button[@type='button']").click()
        if "You have done a dynamic click" == self.driver_obj.find_element_by_xpath("//p[@id='dynamicClickMessage']").text:
            return True
        else:
            print("Expected message is not the same with displayed message.")
            return False




# a = ParentClassPOM()
# a.initiate_browser_instance()
# a.click_element_from_left_pannel_menu('Check Box')
# checkbox = CheckBoxPage()
# checkbox.click_expand_or_collapse_all_button('Expand all')
# #print(checkbox.check_if_there_is_something_expanded())
# #print(checkbox.return_displayed_results())
# # print(checkbox.make_action_on_box_item('home', 'Click'))
# # time.sleep(1)
# # print(checkbox.make_action_on_box_item('home', 'Toggle'))
# # time.sleep(1)
# # print(checkbox.make_action_on_box_item('home', 'Toggle'))
# # time.sleep(1)
# # print(checkbox.make_action_on_box_item('home', 'Click'))
# print(checkbox.make_action_on_box_item('workspace', 'Click'))
# print(checkbox.make_action_on_box_item('veu', 'Click'))
# print(checkbox.make_action_on_box_item('desktop', 'Click'))
# print(checkbox.make_action_on_box_item('office', 'Click'))
# print(checkbox.make_action_on_box_item('office', 'Toggle'))
# print(checkbox.make_action_on_box_item('office', 'Click'))
# print(checkbox.make_action_on_box_item('excelFile', 'Click'))
# print(checkbox.make_action_on_box_item('home', 'Click'))
# l = checkbox.return_displayed_results()
# print("\n")
# print(checkbox.check_if_there_is_something_expanded())
# print("\n")
# print(checkbox.return_displayed_results())
# print("\n")
# print(checkbox.check_if_all_selected_are_displayed(l))
# print(CheckBoxPage.LIST_WITH_SELECTED_NAMES)
# # # j = TextBoxPage()
# # #j.close_bottom_ad()
# # #j.check_link_is_reachable_for_right_side_ad()
# # #list_with_info = ["Adrian 23 !.", "a3fm3@yahoo.com", "ceva", "Str Medg, Bl h2, ap 26 :)"]
# # j.write_in_textbox("userName", "Adrian 23 !.")
# # j.write_in_textbox("userEmail", "a3fm3yahoo.com")
# # j.write_in_textbox("currentAddress", "ceva")
# # j.write_in_textbox("permanentAddress", "Str Medg, Bl h2, ap 26 :)")
# # if j.click_submit_button():
# #     print(j.check_if_answer_is_shown())
# # else:
# #     print("smth wrong")
# # j.write_in_textbox("userName", "1111111111111")
# # j.write_in_textbox("permanentAddress", "Etaj 8")
# # j.write_in_textbox("userEmail", "hhhhhhh@yahoo.com")
# # if j.click_submit_button():
# #     print(j.check_if_answer_is_shown())
# # else:
# #     print("smth wrong")
# time.sleep(1)
# a.close_browser_instance()

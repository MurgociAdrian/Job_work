import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    driver = webdriver.Chrome('C:/Users/Adrian23/PycharmProjects/ex_1/chromedriver.exe')  # instance of chrome

    driver.get('https://www.python.org/')


    driver.find_element_by_link_text("All releases").click()
    rel = driver.find_element_by_css_selector("span.release-number a")
    print(rel.text)

    # search_bar.clear()

    search_box = driver.find_element_by_name('q')
    search_box.send_keys('decorator')
    search_box.send_keys(Keys.RETURN)
    driver.find_element_by_partial_link_text("Decorators").click()
    driver.find_element_by_link_text("Examples").click()
    ex = driver.find_element_by_id("examples")
    nr_ex = ex.find_elements_by_xpath("//ol[@class='arabic']/li")
    print(len(nr_ex))  # ?????????????????

    driver.quit()

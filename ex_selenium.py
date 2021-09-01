import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    driver = webdriver.Chrome('C:/Users/Adrian23/PycharmProjects/ex_1/chromedriver.exe')  # instance of chrome

    driver.get('https://www.python.org/')

    time.sleep(1)

    # search_box = driver.find_element_by_name('q')
    #
    # search_box.send_keys('ChromeDriver')
    #
    # search_box.submit()

    driver.find_element_by_link_text("All releases").click()
    rel = driver.find_element_by_css_selector("span.release-number a")
    print(rel.text)

    # search_bar.clear()
    # search_bar.send_keys("getting started with python")
    # search_bar.send_keys(Keys.RETURN)
    # print(driver.current_url)

    time.sleep(1)

    driver.quit()

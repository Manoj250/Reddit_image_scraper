# uses chromedriver to scrape the links from the website

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class scraper:
    def __init__(self, url, scroll_count, restricted=False, delay_to_load_website=10, delay_to_load_page=3):
        self.url = url
        self.scroll_count = scroll_count
        self.delay_to_load_website = delay_to_load_website
        self.delay_to_load_page = delay_to_load_page
        self.restricted = restricted
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)

        driver.get(self.url)

        if(self.restricted):
            driver.find_element_by_xpath(
                '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div[1]/div/div/div[2]/button').click()

        time.sleep(self.delay_to_load_website)

        for i in range(0, self.scroll_count):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            print("scrolling"+str(i))
            time.sleep(self.delay_to_load_page)

        links = []
        images = driver.find_elements_by_css_selector('img[alt="Post image"]')

        print("got "+str(len(images))+" images")

        for img in images:
            links.append(img.get_attribute('src'))

        print("writing to file")
        with open("p.json", "w") as outfile:
            json.dump(links, outfile)
        print("done")
        driver.close()


new = scraper(url="https://www.reddit.com/r/whatisthisthing/", scroll_count=1
              ,restricted=False, delay_to_load_website=10, delay_to_load_page=3)

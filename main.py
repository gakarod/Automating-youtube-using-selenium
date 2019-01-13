
import bs4
import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()

# Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://www.youtube.com')
search = browser.find_element_by_name('search_query')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN)


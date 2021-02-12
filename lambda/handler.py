from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def hello(event, context):
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome('/opt/chromedriver',chrome_options=options)

    driver.get('https://www.prothomalo.com/')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     # Wait to load page
    time.sleep(2)

    page = driver.page_source
    soup = BeautifulSoup(page, features='html.parser')


    titles = ''
    h2_tags = soup.find_all('h2')
    for h2_tag in h2_tags:
         titles = titles + h2_tag.text + ','

    driver.close();
    driver.quit();

    response = {
        "statusCode": 200,
        "body": titles
    }

    return response


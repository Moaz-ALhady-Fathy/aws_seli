from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.headless = True
wd = webdriver.Chrome('/content/chromedriver',options=chrome_options)
wd.get("https://www.classcentral.com/")
print(wd.page_source)

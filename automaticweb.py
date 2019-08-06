import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
word_username= "" <-HERE YOUR WORDPRESS USER, and PASSWORD
word_password=""

driver=webdriver.Chrome(executable_path="C:\\Users\.....\chromedriver.exe") <- HERE YOURS

keyword=[] <- HERE YOUR KEYWORDS
url= "https://www.youtube.com/results?search_query="
y=0
driver.get('https://example.com/wp-admin/')
time.sleep(3)

user=driver.find_element_by_xpath("//*[@id='user_login']")

user.send_keys(word_username)

time.sleep(5)
passw=driver.find_element_by_xpath("//*[@id='user_pass']")
passw.send_keys(word_password)
driver.find_element_by_xpath("//*[@id='user_pass']").send_keys(Keys.ENTER)
time.sleep(8)
driver.find_element_by_xpath("//*[@id='wp-admin-bar-new-content']/a/span[1]").click()
elem=driver.find_element_by_xpath('//*[@id="post-title-0"]')
elem.send_keys(Keys.CONTROL,Keys.ALT, Keys.SHIFT, "m")


time.sleep(3)

for e in keyword:
    print("Página" + e)
    driver.find_element_by_xpath("//*[@id='wp-admin-bar-new-content']/a/span[1]").click()
    time.sleep(2)
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="post-title-0"]')

    elem.send_keys("[TOP 10] videos " + " " + e )
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    v = "&sp=EgIQAQ%253D%253D"
    driver.get(url+e+v)
    s=driver.find_elements_by_xpath('//*[@id="video-title"][@class="yt-simple-endpoint style-scope ytd-video-renderer"][starts-with(@href, "/watch?v=")]')
    time.sleep(5)
    n=(e)
    a = s[:10]
    o=0
    for i in a :
            o+=1
            time.sleep(5)
            t = i.get_attribute("title")
            h = i.get_attribute("href")

            time.sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            elem=driver.find_element_by_xpath('//*[@id="post-title-0"]')
            body=driver.find_element_by_xpath('//*[@id="post-content-0"]')
            body=driver.find_element_by_xpath('//*[@id="post-content-0"]')
            time.sleep(2)
            body.send_keys(Keys.ENTER)
            body.send_keys(Keys.ENTER)
            body.send_keys(o)
            body.send_keys(" ")
            body.send_keys(". ")
            body.send_keys(t)
            body.send_keys(Keys.ENTER)
            time.sleep(2)
            body.send_keys(Keys.ENTER)
            time.sleep(2)
            body.send_keys(h)
            body.send_keys(Keys.ENTER)
            body.send_keys(Keys.ENTER)
            time.sleep(2)
            body.send_keys(Keys.CONTROL, "s")
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.window(driver.window_handles[0])
    body.send_keys(Keys.CONTROL, "s")


    time.sleep(10)

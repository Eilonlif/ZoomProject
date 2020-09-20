import selenium
from time import sleep
import re


def getZoomLink(driver,  Class):
    for i in range(300):
        try:
            tmpclass = driver.find_element_by_xpath(f"//*[@id=\"pane-side\"]/div[1]/div/div/div[{i}]/div/div/div[2]/div[1]/div[1]/div/span").text
            print(tmpclass)
            if Class in tmpclass:
                driver.find_element_by_xpath(f"//*[@id=\"pane-side\"]/div[1]/div/div/div[{i}]/div/div/div[2]/div[1]/div[1]/div/span").click()
                sleep(5)
                return getLastMsgs(driver, 50)
        except selenium.common.exceptions.NoSuchElementException:
            pass


def getLastMsgs(driver, msgs):  # Looking at the 30 last messages or so, if you want more you need to scroll up
    print("Going threw massages...")
    for i in range(msgs, 0, -1):
        for j in range(msgs, 0, -1):
            try:
                msg = driver.find_element_by_xpath(f"//*[@id=\"main\"]/div[3]/div/div/div[{j}]/div[{i}]/div/div/div/div[1]/div").text
                if "zoom" in msg:
                    try:
                        return re.search("(?P<url>https?://[^\s]+)", msg).group("url")
                    except AttributeError:
                        pass
            except selenium.common.exceptions.NoSuchElementException:
                pass


def openWhatsapp(driver):
    driver.get('https://web.whatsapp.com/')
    sleep(10)


def joinZoomMeeting(driver, ClassName):
    openWhatsapp(driver)
    link = getZoomLink(driver, ClassName)
    driver.get(link)


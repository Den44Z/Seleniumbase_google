from seleniumbase import SB
from selenium.webdriver.common.action_chains import ActionChains

import codecs
import os
import time
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumbase.common.exceptions import LinkTextNotFoundException
from seleniumbase.common.exceptions import TextNotVisibleException
from seleniumbase.config import settings
from seleniumbase.fixtures import page_utils
from seleniumbase.fixtures import shared_utils
startingurl = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&service=accountsettings&ifkv=ARZ0qKICjNE5FX66OG4RjV7KK4CQ9ukg9IyudMLCCaw2mm4OqG0x0rd0J95k-fg24Jxbe9h_HXCTtw&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
# asıl bu reviev_url ='https://www.google.com/search?client=opera-gx&q=hayvanat+bahçesi+antalya&sourceid=opera&ie=UTF-8&oe=UTF-8#ip=1'
#review_url = 'https://www.google.com/maps/place/Antalya+Zoo/@36.9514564,30.6243335,14.25z/data=!4m16!1m7!3m6!1s0x14c38f97cd35bad3:0x5b85efc6298e4977!2sAntalya+Zoo!8m2!3d36.9461922!4d30.6360373!16s%2Fg%2F11p0259wxq!3m7!1s0x14c38f97cd35bad3:0x5b85efc6298e4977!8m2!3d36.9461922!4d30.6360373!9m1!1b1!16s%2Fg%2F11p0259wxq?entry=ttu'
#review_text= 'güzeldi'
def post_review(driver, url, review_text):
    print('post review started')
    driver.open(url)
    try:
        #driver.click('span.GMtm7c.fontTitleSmall') #button //*[@id="gsr"]
        driver.sleep(10)
        driver.click(".B1InU") #----------------------------button //*[@id="gsr"]
        driver.sleep(10)
        driver.switch_to_frame('iframe[name="goog-reviews-write-widget"]')
        #driver.switch_to.frame('iframe[name="goog-reviews-write-widget"]')
        print('swiched to widget')
        driver.type("#c2", "That was great")  # Click on the "Write a review"
        print('reviewed')
        driver.sleep(10)
        driver.click('div.s2xyy[role="radio"][aria-label="Four stars"]')
        #driver.click('div.s2xyy[role="radio"][aria-label="Dört yıldız"][aria-checked="false"]')

        driver.hover_and_click(hover_selector="#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button", click_selector="#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button")
        #driver.hover_and_click(click_selector= ".VfPpkd-LgbsSe",click_by=".VfPpkd-LgbsSe") # .VfPpkd-RLmnJb   click('.VfPpkd-LgbsSe')  .VfPpkd-vQzf8d
        print('hovered')
        driver.sleep(3)
#        actions = ActionChains(driver)
#        actions.move_to_element("button.VfPpkd-LgbsSe").move_by_offset(10, 5).click().perform()
#        driver.type('#c2', review_text)  button.VfPpkd-vQzf8d span.VfPpkd-vQzf8d  'span.V67aGc'
        driver.click("#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button")            #click('button > .VfPpkd-vQzf8d')            #click('span.VfPpkd-vQzf8d')
        print('hovered 2')
        driver.sleep(1)

        driver.assert_text('Thank you for your review!','#yDmH0d > c-wiz > div > div > div > c-wiz > div > div:nth-child(2) > div > div:nth-child(1) > div > button > span')

    except Exception as e:
        print(f"An error occurred while posting a review: {e}")

def log_in_and_post_review(account):
    username, password, review_url, review_text = account
    with SB(uc=True) as driver:
        if not driver.undetectable:
            driver.get_new_driver(undetectable=True)
        try:
            driver.get(startingurl)
            driver.sleep(2)
            driver.wait_for_element('input[type="email"]')
            driver.type('input[type="email"]', username)
            driver.sleep(1)
            driver.click('div[id="identifierNext"]')
            driver.sleep(2)
            driver.wait_for_element('input[type="password"]', timeout=10)
            driver.type('input[type="password"]', password)
            driver.sleep(1)
            driver.click('div[id="passwordNext"]')
            driver.sleep(2)
            driver.get(review_url)
            driver.sleep(2)

            post_review(driver, review_url, review_text)
            driver.sleep(2)
            # Add logout logic here if necessary
            # Sign out
            # Click on the account icon
            driver.get('https://myaccount.google.com/?utm_source=OGB&utm_medium=app')
            driver.sleep(2)
            #driver.click('#gb > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div > a')  # Click on the account icon or similar element
            driver.sleep(1)
            # Click on "Sign out"
            #driver.click('#yDmH0d c-wiz > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > span:nth-child(2) > a > span:nth-child(2) > div > div')

        except Exception as e:
            print(f"An error occurred with account {username}: {e}")

accounts = [('rdadszucchi@gmail.com', 's55jommo988m',
'https://www.google.com/search?gs_ssp=eJzj4tVP1zc0LDAwMrUsryg0YLRSNagwNEk2tkizNE9OMTZNSkwxtjKoME2yME1NSzYzsrRINbE0N_eSTMwrScypTFTISKwsS8xLLFFISsw4vDy1OBMAtC4ZlQ&client=opera-gx&q=antalya+hayvanat+bahçesi&sourceid=opera&ie=UTF-8&oe=UTF-8',
             'Great experience!')]
#https://www.google.com/maps/api/js/ReviewsService.LoadWriteWidget2?key=AIzaSyBcv0QfUNUfBwo8pIGJ3teNCkaluSGUWus&authuser=0&hl=en-GB&origin=https%3A%2F%2Fwww.google.com&pb=!2m1!1sChIJ07o1zZePwxQRd0mOKcbvhVs!7b1&cb=53571027
for account in accounts:
    log_in_and_post_review(account)

def hover_and_click(
    driver,
    hover_selector,
    click_selector,
    hover_by="css selector",
    click_by="css selector",
    timeout=settings.SMALL_TIMEOUT,
    js_click=False,
):
    """
    Fires the hover event for a specified element by a given selector, then
    clicks on another element specified. Useful for dropdown hover based menus.
    @Params
    driver - the webdriver object (required)
    hover_selector - the css selector to hover over (required)
    click_selector - the css selector to click on (required)
    hover_by - the hover selector type to search by (Default: "css selector")
    click_by - the click selector type to search by (Default: "css selector")
    timeout - number of seconds to wait for click element to appear after hover
    js_click - the option to use js_click() instead of click() on the last part
    """
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    element = driver.find_element(by=hover_by, value=hover_selector)
    hover = ActionChains(driver).move_to_element(element)
    for x in range(int(timeout * 10)):
        try:
            hover.perform()
            element = driver.find_element(by=click_by, value=click_selector)
            if js_click:
                driver.execute_script("arguments[0].click();", element)
            else:
                element.click()
            return element
        except Exception:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)
    plural = "s"



def hover_and_click(
    driver,
    hover_selector,
    click_selector,
    hover_by="css selector",
    click_by="css selector",
    timeout=settings.SMALL_TIMEOUT,
    js_click=False,
):
    """
    Fires the hover event for a specified element by a given selector, then
    clicks on another element specified. Useful for dropdown hover based menus.
    @Params
    driver - the webdriver object (required)
    hover_selector - the css selector to hover over (required)
    click_selector - the css selector to click on (required)
    hover_by - the hover selector type to search by (Default: "css selector")
    click_by - the click selector type to search by (Default: "css selector")
    timeout - number of seconds to wait for click element to appear after hover
    js_click - the option to use js_click() instead of click() on the last part
    """
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    element = driver.find_element(by=hover_by, value=hover_selector)
    hover = ActionChains(driver).move_to_element(element)
    for x in range(int(timeout * 10)):
        try:
            hover.perform()
            element = driver.find_element(by=click_by, value=click_selector)
            if js_click:
                driver.execute_script("arguments[0].click();", element)
            else:
                element.click()
            return element
        except Exception:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)
    plural = "s"

def hover_element_and_click(
    driver,
    element,
    click_selector,
    click_by="css selector",
    timeout=settings.SMALL_TIMEOUT,
):
    """
    Similar to hover_and_click(), but assumes top element is already found.
    """
    start_ms = time.time() * 1000.0
    stop_ms = start_ms + (timeout * 1000.0)
    hover = ActionChains(driver).move_to_element(element)
    for x in range(int(timeout * 10)):
        try:
            hover.perform()
            element = driver.find_element(by=click_by, value=click_selector)
            element.click()
            return element
        except Exception:
            now_ms = time.time() * 1000.0
            if now_ms >= stop_ms:
                break
            time.sleep(0.1)
    plural = "s"


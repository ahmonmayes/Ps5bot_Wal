from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import random
import time


class PS5Bot:

    def __init__(self, first_name, last_name, email, address, phone, credit_number,
                 credit_month, credit_year, credit_ccv, chrome_path):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone = phone
        self.credit_number = credit_number
        self.credit_month = credit_month
        self.credit_year = credit_year
        self.credit_ccv = credit_ccv
        self.driver = webdriver.Chrome(chrome_path)
        #self.driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501')     #Website needs to be updated to the webpage of desire

    def slowdown(self):
        random_wait_time = random.randrange(5.0, 10.0)
        print(random_wait_time)
        time.sleep(random_wait_time)

    def add_ps5_to_cart_and_checkout(self):
        checkOut = ('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/'
                    'div[3]/div/div/div[2]/div/div[2]/div/button[1]')
        continueWithoutAccount = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]'
                                  '/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span')

        while (True):
            try:
                #self.driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/994712501')    #Website needs to be updated to the webpage of desire
                try:
                    actions = ActionChains(self.driver)
                    el = self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div/p')   #selects area above captcha
                    actions.move_to_element_with_offset(el, 60, 160).click_and_hold().perform()   # moves cursor down 10 and to right 10 of element in xpath el and click and hold
                    actions.pause(11)                                                            # pauses the hold so click can release
                    actions.release(el).perform()
                except MoveTargetOutOfBoundsException:
                    print("Target out of bounds for action chain")
                addToCart = self.driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span')
                addToCart.click()
                break
            except NoSuchElementException:
                print("Out of stock")
                print("waiting....")
                time.sleep(10)


        self.clickButton(checkOut)
        self.clickButton(continueWithoutAccount)

    def filling_shipping_info(self):
        firstContinue = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[3]/button/span')
        firstName = '//*[@id="firstName"]'
        lastName = '//*[@id="lastName"]'
        email = '//*[@id="email"]'
        address = '//*[@id="addressLineOne"]'
        phone = '//*[@id="phone"]'
        confirmInfo = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/'
                       'div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span')
        useThisAddy = ('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div[7]/div/button[2]/span')

        self.clickButton(firstContinue)
        self.enterData(firstName, self.first_name)
        self.enterData(lastName, self.last_name)
        self.enterData(phone, self.phone)
        self.enterData(email, self.email)
        self.enterData(address, self.address)
        self.clickButton(confirmInfo)
        self.clickButton(useThisAddy)

    def fill_out_payment_and_order(self):  # FILLS OUT PAYMENT
        creditCardNum = '//*[@id="creditCard"]'
        creditExpireMonth = '//*[@id="month-chooser"]'
        creditExpireYear = '//*[@id="year-chooser"]'
        creditCVV = '//*[@id="cvv"]'
        reviewOrder = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div'
                       '/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span/span/span')
        placeOrder = ('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div/form/div/button/span')

        self.enterData(creditCardNum, self.credit_number)
        self.enterData(creditExpireMonth, self.credit_month)
        self.enterData(creditExpireYear, self.credit_year)
        self.enterData(creditCVV, self.credit_ccv)
        self.clickButton(reviewOrder)
        self.clickButton(placeOrder)

    def clickButton(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception:
            time.sleep(1)
            self.clickButton(xpath)

    def enterData(self, field, data):
        try:
            self.driver.find_element_by_xpath(field).send_keys(data)
            pass
        except Exception:
            time.sleep(1)
            self.enterData(field, data)


if __name__ == "__main__":
    personal_info = dict(
        first_name="",                                                   #this section needs to be filled in
        last_name="",
        email="",
        address="",
        phone="",
        credit_number="",
        credit_month="",
        credit_year="",
        credit_ccv="",
        chrome_path="C:\Program Files (x86)\chromedriver.exe"                 #needs the most updated chromedriver in this file path
    )

    bot = PS5Bot(**personal_info)
    bot.add_ps5_to_cart_and_checkout()
    bot.filling_shipping_info()
    bot.fill_out_payment_and_order()
from selenium.webdriver.common.by import By

from Utilities.AddressForm import AddressForm


class HomePage:

    search_bar = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    item_text_footer = (By.CSS_SELECTOR, "div div div div h2 span")
    item_grid = (By.XPATH, "//img[@alt='Sponsored Ad - Apple iPhone 15 (128 GB) - Black']")
    add_to_cart_button = (By.XPATH, "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']")
    cart_button = (By.CSS_SELECTOR, "input[aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    login_input = (By.CSS_SELECTOR, "input[type$='email']")
    proceed_to_checkout = (By.CSS_SELECTOR, "input[value='Proceed to checkout']")
    continue_login_button = (By.XPATH, "//input[@id='continue']")
    opt_on_your_phone = (By.CSS_SELECTOR, "span input[id='continue']")
    enter_otp_field = (By.XPATH,"//div[@id='cvf-input-code-container']")
    submit_otp_continue_button = (By.XPATH, "(//span[@id='cvf-submit-otp-button'])[1]")




    def __init__(self, driver):
        self.driver = driver

    def getSearch_bar(self):
        print("***************************************")
        search_field = self.driver.find_element(*self.search_bar)
        homePage = AddressForm(self.driver)
        print("***************************************2")
        search_field.send_keys("Iphone 15")
        search_field.submit()
        return homePage

    def getItem_text_footer(self):
        return self.driver.find_elements(*self.item_text_footer)

    def getItemGrid(self):
        return self.driver.find_element(*self.item_grid)

    def getAddtoCartButton(self):
        return self.driver.find_element(*self.add_to_cart_button)

    def getProceedToCart(self):
        return self.driver.find_element(*self.cart_button)

    def getLoginInput(self):
        return self.driver.find_element(*self.login_input)

    def getProceedToCheckOut(self):
        return self.driver.find_element(*self.proceed_to_checkout)

    def getContinueButton(self):
        return self.driver.find_element(*self.continue_login_button)

    def getOTP(self):
        return self.driver.find_element(*self.opt_on_your_phone)

    def getEnterOTPField(self):
        return self.driver.find_element(*self.enter_otp_field)

    def getSubmitOTPButton(self):
        return self.driver.find_element(*self.submit_otp_continue_button)

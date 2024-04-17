import time

import select
from selenium.webdriver.support.select import Select

from test.BaseClass import BaseClass
from test.HomePageObject import HomePage

# We have created a Test Add to Cart Class where the Test case execution will be start
class Test_add_to_cart(BaseClass):
    driver = None
    pincode = 201301
    city = "Noida"
    def test_add_to_cart(self):

        homepage = HomePage(self.driver)
        homePage = homepage.getSearch_bar()

        # Scroll the screen
        self.driver.execute_script("window.scrollTo(0, 1000);")

        # List of the relevant item names
        items = homepage.getItem_text_footer()
        print("Check")
        item_found = False

        for item in items:
            itemText = item.text
            print(itemText)

            if itemText == "Apple iPhone 15 (128 GB) - Black":
                homepage.getItemGrid().click()
                print("Item found Successfully")
                item_found = True
                break

            else:
                print("Item Not Found")

        time.sleep(1)

        # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        # Click on Add to Cart Button
        homepage.getAddtoCartButton().click()
        time.sleep(2)
        # Click on cart button once the item is added to cart
        homepage.getProceedToCart().click()
        time.sleep(2)
        # Click on Proceed to Buy button from the detail page
        homepage.getProceedToCheckOut().click()
        time.sleep(2)
        # click and Enter the Email Id or Mobile Number for Login
        homepage.getLoginInput().click()
        homepage.getLoginInput().send_keys("9582978060")
        time.sleep(2)
        # CLick on Continue Button
        homepage.getContinueButton().click()
        time.sleep(5)
        # click on get on OTP on you phone button
        homepage.getOTP().click()
        time.sleep(10)
        # Enter the OTP on text field
        homepage.getEnterOTPField().click()
        time.sleep(10)
        homepage.getSubmitOTPButton().click()
        time.sleep(2)
        # CLick on Add Address button
        homePage.getAddressButton().click()
        time.sleep(2)
        # Enter the Name in the field
        homePage.getFirstName().send_keys("Ashish")
        time.sleep(2)
        # Enter the Mobile Number in the field
        homePage.getMobileNumber().send_keys(9582978060)
        time.sleep(2)
        # Enter the Pincode
        homePage.getPincode().send_keys(Test_add_to_cart.pincode)
        time.sleep(2)
        # Enter the Flat Address
        homePage.getFlatAddress().send_keys("Flat No -1205 Amarpa")
        time.sleep(2)

        # Enter the Street field
        homePage.getStreetAddress().send_keys("Sector 76")
        time.sleep(2)
        # Enter the Landmark
        homePage.getLandmark().send_keys("Sector 76")
        time.sleep(2)
        # Click on dropdown Buutton
        state_dropdown = homePage.getStateDropdown()
        state_dropdown.click()
        # Select the State from dropdown
        select_state = homePage.getSelectDropdown()
        select_state.click()
        # Click on the checkbox
        homePage.getCheckBox().click()
        time.sleep(2)
        # CLick on Use this Address button
        homePage.getUseThisAddress().click()
        time.sleep(2)

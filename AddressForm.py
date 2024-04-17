from selenium.webdriver.common.by import By


class AddressForm:
    # Here we have declared the variable and pass it to the specified method to get the accurate location path
    
    add_address_button = (By.XPATH, "//a[@id='add-new-address-popover-link']")
    first_name = (By.XPATH , "//input[@id='address-ui-widgets-enterAddressFullName']")
    mobile_number = (By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']")
    pincode = (By.CSS_SELECTOR, "#address-ui-widgets-enterAddressPostalCode")
    flat_address = (By.CSS_SELECTOR, "#address-ui-widgets-enterAddressLine1")
    street_address = (By.CSS_SELECTOR, "#address-ui-widgets-enterAddressLine2")
    landmark = (By.CSS_SELECTOR, "#address-ui-widgets-landmark")
    city = (By.CSS_SELECTOR, "#address-ui-widgets-enterAddressCity")
    state_drop_down = (By.CSS_SELECTOR, "span[id='address-ui-widgets-enterAddressStateOrRegion'] span[role='button']")
    select_state = (By.CSS_SELECTOR, "#address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId_33")
    check_box = (By.CSS_SELECTOR, "#address-ui-widgets-use-as-my-default")
    use_this_address_button = (By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']")


    def __init__(self, driver):
        self.driver = driver

    def getAddressButton(self):
        return self.driver.find_element(*self.add_address_button)

    def getFirstName(self):
        return self.driver.find_element(*self.first_name)

    def getMobileNumber(self):
        return self.driver.find_element(*self.mobile_number)

    def getPincode(self):
        return self.driver.find_element(*self.pincode)

    def getFlatAddress(self):
        return self.driver.find_element(*self.flat_address)

    def getStreetAddress(self):
        return self.driver.find_element(*self.street_address)

    def getLandmark(self):
        return self.driver.find_element(*self.landmark)

    def getCity(self):
        return self.driver.find_element(*self.city)

    def getStateDropdown(self):
        return self.driver.find_element(*self.state_drop_down)

    def getSelectDropdown(self):
        return self.driver.find_element(*self.select_state)

    def getCheckBox(self):
        return self.driver.find_element(*self.check_box)

    def getUseThisAddress(self):
        return self.driver.find_element(*self.use_this_address_button)


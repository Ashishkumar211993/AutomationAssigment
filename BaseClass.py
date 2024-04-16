import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("BrowserInvocation")
class BaseClass:
    driver = None

    def verifyLinkPresence(self, text):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))).click()


import pytest
from selenium import webdriver


# Going to Invocation the browser first
@pytest.fixture(scope="class")
def BrowserInvocation(request):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.quit()


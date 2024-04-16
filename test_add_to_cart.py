import time

from test.BaseClass import BaseClass
from test.HomePageObject import HomePage


class Test_add_to_cart(BaseClass):
    driver = None

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







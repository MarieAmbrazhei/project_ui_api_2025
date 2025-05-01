from pages.base_page import BasePage
from pages.locators.product_locators import ProductLocators as ProductLoc


class ProductPage(BasePage):
    def add_to_cart(self):
        self.click_button(ProductLoc.ADD_TO_CART_BUTTON)

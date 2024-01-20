import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

navigate_url = "https://www.amazon.pl/"


@given('I open the Amazon website')
def open_amazon_website(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.get(navigate_url)
    context.driver.implicitly_wait(5)
    context.logger = logging.getLogger('selenium')
    context.logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    context.logger.addHandler(ch)


@when('I confirm the cookies')
def confirm_cookies(context):
    cookies = context.driver.find_element(By.ID, 'sp-cc-accept')
    if cookies:
        cookies.click()


@when('I search for the product "{product}"')
def search_for_product(context, product):
    context.logger.info(f"Searching for the product: {product}")
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('I click on the product')
def click_on_product(context):
    context.driver.find_element(By.XPATH,
                                '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div[2]/div[2]/h2/a/span').click()


@when('I click on the "Add to Cart" button')
def click_add_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('the cart should contain {quantity} product')
def verify_cart_contains_product(context, quantity):
    cart_count = context.driver.find_element(By.ID, 'nav-cart-count').text
    if quantity == cart_count:
        context.logger.info("Product successfully added to the cart")
    else:
        context.logger.error(f"Cart does not contain {quantity} product")
        context.driver.quit()

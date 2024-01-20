import logging
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

navigate_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@given('I open the OrangeHRM website')
def open_website(context):
    context.driver = webdriver.Chrome()
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


@when('I log in with username "{username}" and password "{password}"')
def login(context, username, password):
    context.logger.info("Logging into the website")
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()


@then('I should be successfully logged in')
def verify_login(context):
    try:
        context.driver.find_element(By.CLASS_NAME, "orangehrm-dashboard-grid")
        context.logger.info("Successfully logged in")
    except:
        context.logger.error("Login failed")


@when('I add a new employee with details {firstName}, {middleName}, {lastName}')
def add_employee(context, firstName, middleName, lastName):
    context.logger.info("Adding a new employee")
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()

    context.driver.find_element(By.NAME, 'firstName').send_keys(firstName)
    context.driver.find_element(By.NAME, 'middleName').send_keys(middleName)
    context.driver.find_element(By.NAME, 'lastName').send_keys(lastName)
    context.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()


@then('the employee should be successfully added')
def verify_employee_added(context):
    if context.driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/h6').text.find(
        'Test Testowy'):
        context.logger.info("Employee successfully added")
    else:
        context.logger.error("Failed to add employee")

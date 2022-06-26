from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class SeleniumPlaygroundPageLocators(object):
    file_download = (By.CSS_SELECTOR, '#__next > div > section.my-50 > div > div > div:nth-child(2) > div:nth-child(1) > ul > li:nth-child(6) > a')
    data_field = (By.XPATH, '//*[@id="textbox"]')
    generate_file = (By.ID, 'create')
    download_button = (By.XPATH, '//*[@id="link-to-download"]')

from XYZBankPage import SearchHelper
from selenium import webdriver

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://192.168.157.51:5556',
        options=chrome_options
    )
    # driver = webdriver.Chrome()
    test = SearchHelper(driver, "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    try:
        test.go_to_site()
        test.customer_login()
        test.select_actions('deposit')
        test.select_actions('withdrawn')
        test.select_actions('transaction')
        test.parsing_data()
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()

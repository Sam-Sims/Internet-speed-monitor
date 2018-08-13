from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from configparser import ConfigParser
import time
import csv


# TODO Implement a log
# TODO Implement command line arguments (-t time to run for continuous operation, -MB for megabytes/bits etc)
# TODO Exception handling

class Config:

    def __init__(self):
        config = ConfigParser()
        config.read('config.ini')
        self.driver_path = config.get('DRIVER', 'path')
        self.driver_type = config.get('DRIVER', 'type')
        self.enable_headless = config.get('DRIVER', 'enable_headless')
        self.enable_log = config.get('LOG', 'enable_log')


class SpeedTest:

    def __init__(self, config:Config):
        self.download = ""
        self.upload = ""
        self.ping = ""
        self.config = config
        self.driver = None
        self.wait = None

        try:
            # Create options for both firefox and chrome
            options = Options()
            options.add_argument("--headless")  # --headless
            options_chrome = webdriver.ChromeOptions()
            options_chrome.add_argument('headless')
            # Check if a driver type is specified
            if self.config.driver_type is not None:
                # Check if firefox is specified
                if self.config.driver_type == "firefox":
                    # If firefox is specified check if a path for the binary is specified
                    if self.config.driver_path is not None:
                        # If headless is true
                        if self.config.enable_headless == "true":
                            self.driver = webdriver.Firefox(executable_path=config.driver_path, firefox_options=options)
                        else:
                            self.driver = webdriver.Firefox(executable_path=config.driver_path)
                    # if no path is specified try default location (root directory)
                    else:
                        # Check if headless is true
                        if self.config.enable_headless == "true":
                            self.driver = webdriver.Firefox(firefox_options=options)
                        else:
                            self.driver = webdriver.Firefox()
                # Check if chrome is specified in the config
                elif self.config.driver_type == "chrome":
                    # If chrome is specified check if a path for the binary is specified
                    if self.config.driver_path is not None:
                        # Check if headless is true
                        if self.config.enable_headless == "true":
                            self.driver = webdriver.Chrome(executable_path=config.driver_path, chrome_options=options_chrome)
                        else:
                            self.driver = webdriver.Chrome(executable_path=config.driver_path)
                    # If no path is specified try default location (root directory)
                    else:
                        # Check if headless is true
                        if self.config.enable_headless == "true":
                            self.driver.webdriver.Chrome(chrome_options=options_chrome)
                        else:
                            self.driver = webdriver.Chrome()
                else:
                    print("Please specify a valid driver type!")
            else:
                print("Some kind of error loading the config")

            self.wait = WebDriverWait(self.driver, 5)

        except WebDriverException as e:
            print("Driver creation failed: ", str(e))

    def run_test(self):
        self.driver.get("http://www.speedtest.net/")
        cookie_button = self.driver.find_element_by_id('_evidon-banner-acceptbutton')
        cookie_button.click()
        button = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Go')]")))
        button.click()
        time.sleep(40)

    def store_values(self):
        self.ping = str(self.driver.find_element_by_xpath("//span[contains(@class, 'result-data-large number result-data-value ping-speed')]").text)
        self.download = str(self.driver.find_element_by_xpath("//span[contains(@class, 'result-data-large number result-data-value download-speed')]").text)
        self.upload = str(self.driver.find_element_by_xpath("//span[contains(@class, 'result-data-large number result-data-value upload-speed')]").text)

    # Deconstructor to dispose of the webdriver
    def __del__(self):
        if self.driver is not None:
            self.driver.quit()


class Output:

    def __init__(self, speedtest:SpeedTest):
        self.speedtest = speedtest
        self.speedtest_download = self.speedtest.download
        self.speedtest_upload = self.speedtest.upload
        self.speedtest_ping = self.speedtest.ping

    def write_csv(self):
        with open('speeds.csv', mode='a') as speeds:
            fieldnames = ['Date', 'Time', 'Ping', 'Download', 'Upload']
            writer = csv.DictWriter(speeds, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow({'Date': (time.strftime("%d/%m/%Y")), 'Time': time.strftime("%H:%M"), 'Ping': self.speedtest_ping, 'Download': self.speedtest_download, 'Upload': self.speedtest_upload})


# This is for testing only
def main():
    config = Config()
    st = SpeedTest(config)
    st.run_test()
    st.store_values()
    output = Output(st)
    output.write_csv()



if __name__ == "__main__":
    main()
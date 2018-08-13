from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv


# TODO Implement a log
# TODO Implement command line arguments (-t time to run for continuous operation, -MB for megabytes/bits etc)
# TODO Exception handling

class SpeedTest:
    # TODO Implement a config file to point to the geckodriver binary?

    def __init__(self):
        self.download = ""
        self.upload = ""
        self.ping = ""
        self.driver = None
        self.wait = None

        try:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox()  # Starts firefox with options defined above
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
    st = SpeedTest()
    st.run_test()
    st.store_values()
    output = Output(st)
    output.write_csv()


if __name__ == "__main__":
    main()
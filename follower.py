from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "chefsteps"
MY_USER_NAME = "user name"
MY_PASSWORD = "password"


class InstaFollower:

    def __init__(self):
        self.chrome_driver_path = "/Users/alina/Development/chromedriver"
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(MY_USER_NAME)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        not_now_button_1 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button_1.click()
        time.sleep(8)

        not_now_button_2 = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_button_2.click()
        time.sleep(8)

    def find_followers(self):
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(5)

        select = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        select.click()
        time.sleep(5)

        followers = self.driver.find_element(By.CSS_SELECTOR, "ul li a")
        followers.click()
        time.sleep(5)

        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                time.sleep(1)

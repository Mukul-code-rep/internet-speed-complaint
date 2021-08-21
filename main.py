from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from time import sleep

promisedUp = 200
promisedDown = 200
twitter_email = os.environ.get('email')
twitter_password = os.environ.get('password')


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver = '/Users/mukulperiwal/Downloads/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')
        start_button = self.driver.find_element_by_css_selector('.start-button a.js-start-test')
        start_button.click()

        sleep(45)
        self.down = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

        return self.down, self.up

    def tweet_at_provider(self):
        self.driver.get('https://www.twitter.com/login/')
        sleep(2)

        email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(twitter_email)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(twitter_password)
        sleep(2)
        twitter_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        twitter_login.send_keys(Keys.ENTER)

        sleep(5)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()

        sleep(2)
        type_tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        type_tweet.send_keys(f'Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promisedDown}down/{promisedUp}up?')

        sleep(2)
        send_tweet = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send_tweet.click()

        sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot()

down, up = bot.get_internet_speed()

if down < promisedDown or up < promisedUp:
    bot.tweet_at_provider()

# Standard Imports
import time
import random

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# Project Imports
from SessionData import SessionData

class TinderSession:

    SESSION_URL = "https://tinder.com/"
    RETRY_DELAY_SECONDS = 5

    def __init__(self, username, password, driver_path, DEBUG=False):
        self.username = username
        self.password = password
        
        print("Starting WebDriver")
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get(self.SESSION_URL)
        self.root_handle = self.driver.current_window_handle
        self.DEBUG = DEBUG
        
    def login_facebook(self):
        if not self._is_logged_in():
            if (self.DEBUG):
                input("Press 'Enter' to click 'Log In'")
            self._click_login_button()
            
            # Click the "Log in with Facebook" button
            css_selector = "[aria-label='Log in with Facebook']"
            wait = WebDriverWait(self.driver, self.RETRY_DELAY_SECONDS)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                                   css_selector)))
            time.sleep(1)
            if (self.DEBUG):
                input("Press 'Enter' to click 'Log in with Facebook'")
            self.driver.find_element(By.CSS_SELECTOR, css_selector).click()
            self._focus_pop_up()
            
            print("Reached Facebook login page")
            self.driver.find_element(By.ID, "email").send_keys(self.username)
            self.driver.find_element(By.ID, "pass").send_keys(self.password)
            time.sleep(1)
            
            # Username + password sent, click login button
            if (self.DEBUG):
                input("Press 'Enter' to log in with Facebook'")
            self.driver.find_element(By.ID, "loginbutton").click()
            print("Logged in via Facebook")
            self.driver.switch_to.window(self.root_handle)
            time.sleep(5)
        
    def process_permissions(self, allow_notifications=False):
        if (self.DEBUG):
            input("Press 'Enter' to allow location")
        self._allow_location()
        if (self.DEBUG):
            input( "Press 'Enter' to set notification permission to "
                  f"{allow_notifications}") 
        self._set_notification_permission(allow_notifications)
        if (self.DEBUG):
            input("Press 'Enter' to accept cookies")
        self._accept_cookies()
        
    def auto_swipe(self, number, like_percentage):
        for i in range(number):            

            # Prior to each swipe, check for pop ups
            pop_up = self._get_pop_up()
            if (pop_up is not None):
                if (self.DEBUG):
                    input("Press 'Enter' to close pop up")
                pop_up.click()
            time.sleep(2)
            
            # There may be multiple pop-ups on top of each other
            # Keep checking until not found
            while (pop_up is not None):
                pop_up = self._get_pop_up()
                if (pop_up is not None):
                    if (self.DEBUG):
                        input("Press 'Enter' to close pop up")
                    pop_up.click()
                time.sleep(2)
                
            # Introduce randomisation for rejecting user while swiping
            if (random.random() <= like_percentage):
                message = "User liked"
                xpath = "//span[text()='Like']/parent::span/parent::button"
                self.data.right_swipes += 1
            else:
                message = "User noped"
                xpath = "//span[text()='Nope']/parent::span/parent::button"
                self.data.left_swipes += 1

            print(message)
            element = self.driver.find_element(By.XPATH, xpath)
            if (self.DEBUG):
                input("Press 'Enter' to swipe")
            element.click()
            time.sleep(2)
            
    def save(self, filepath="session_data.csv"):
        end = datetime.datetime.now()
        self.data.duration_seconds = (end - self.data.start).total_seconds()
        self.data.total_swipes = self.data.left_swipes + self.data.right_swipes
        
        filetype = filepath.split('.')[-1]
        if (filetype == "csv"):
            self.data.to_csv(filepath)
        else:
            raise ValueError("Filetype not supported for saving")
        
    def end(self):
        self.driver.quit()
        
    def _is_logged_in(self):
        if ("tinder.com/app" in self.driver.current_url):
            return True
        else:
            return False
        
    def _click_login_button(self):
        xpath = "//span[text()='Log in']/parent::a"    
        wait = WebDriverWait(self.driver, self.RETRY_DELAY_SECONDS)
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        time.sleep(1)
        self.driver.find_element(By.XPATH, xpath).click()
        
    def _focus_pop_up(self):
        wait = WebDriverWait(self.driver, self.RETRY_DELAY_SECONDS)
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if (window_handle != self.root_handle):
                self.driver.switch_to.window(window_handle)
                break
                
    def _allow_location(self):
        wait = WebDriverWait(self.driver, self.RETRY_DELAY_SECONDS)
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
                                               "[aria-label='Allow']"))).click()
        print("Location permission accepted")
            
    def _set_notification_permission(self, allow_notifications):
        # Write me!
        pass
                                               
    def _accept_cookies(self):
        # Write me!
        pass
        
    def _get_pop_up(self):
        """A method for checking an pops that block UI on the page."""
        # Figure out cases for "homescreen" and "super-like"
        cases = \
        {
            "match"         : \
            {
                "method" : By.CSS_SELECTOR, 
                "value"  : "button[title='Back to Tinder']",
                "message": "Found match pop up" 
            },
            "platinum-offer": \
            {
                "method" : By.XPATH,
                "value"  : "//span[text()='Maybe Later']/parent::button",
                "message": "Found platinum offer pop up" 
            }
        }
        for switch, case in cases.items():
            try:
                button = self.driver.find_element(case["method"], case["value"])
                print(case["message"])
                return button
            except NoSuchElementException:
                continue
        return None

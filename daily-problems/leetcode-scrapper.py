from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from time import sleep
import json
import os

load_dotenv()

def initWebDriver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    return driver

def getDailyProblem(driver: webdriver.Firefox):
    driver.get(os.getenv("LEETCODE_URL"))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_login")))
    driver.find_element(By.ID, "id_login").send_keys(os.getenv("LEETCODE_USERNAME"))
    driver.find_element(By.ID, "id_password").send_keys(os.getenv("LEETCODE_PASSWORD"))
    driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
    sleep(10) #hacky fix to wait for the page to load
    daily_problem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/a")
    return daily_problem.get_attribute("href")

def saveDailyProblem(problem_url):
    with open("daily-problems.json", "w") as f:
        json.dump({"url": problem_url}, f)

def main():
    driver = initWebDriver()
    problem_url = getDailyProblem(driver)
    saveDailyProblem(problem_url)
    driver.quit()

if __name__ == "__main__":
    main()
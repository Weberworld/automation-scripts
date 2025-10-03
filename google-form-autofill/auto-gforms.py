import random
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def fill_form():
    # Find all question blocks
    questions = driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae")

    for question in questions:
        try:
            # Check for multiple choice options
            options = list(question.find_elements(By.CSS_SELECTOR, ".Od2TWd .docssharedWizToggleLabeledContainer"))
            if not options:
                # Check for checkboxes
                options = list(question.find_elements(By.CSS_SELECTOR, ".docssharedWizToggleLabeledContainer"))

            # Other options are mostly the last on the list,  skip the last option if there are more than 2 options
            if len(options) >= 3:
                options = options[:-1]
            if options:
                rand_opt = random.choice(options)
                rand_opt.click()
                continue

            # Check for text input
            text_inputs = question.find_elements(By.CSS_SELECTOR, "input[type='text'], textarea")
            for input_field in text_inputs:
                input_field.send_keys("Sample response")
        except Exception as e:
            print(f"Error processing question: {e}")

    # Check if there's a "Next" button for multi-page forms
    try:
        next_btn = driver.find_element(By.XPATH, "//span[text()='Next']/ancestor::div[@role='button']")
        next_btn.click()
        time.sleep(3)
        return True
    except Exception:

        return False


def run(form_url):
    # Open the Google Form
    driver.get(form_url)
    time.sleep(3)  # Wait for the form to load

    # Loop through pages if it's a multi-page form
    while True:
        fill_form()
        try:
            b = driver.find_element(By.XPATH, "//span[text()='Submit']")
            fill_form()
            b = driver.find_element(By.XPATH, "//span[text()='Submit']")
            b.click()
            time.sleep(3)
            break
        except:
            continue


if __name__ == "__main__":
    try:

        url = input("Enter google form url: ")
        loops = int(input("Enter number of times to run: "))
        show_browser = input("Show browser: (y / n): ").lower()

        # Setup Chrome WebDriver
        options = Options()
        options.add_argument("--start-maximized")
        if show_browser != "y":
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

        for i in range(loops):
            run(url)
            print(f"Completed run: {i + 1}")

        print("Form completed.")
        driver.quit()
    except Exception:
        print("Error occurred")
        sys.quit()

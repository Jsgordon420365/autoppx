# ver 20241205120000.0
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Define the Perplexity AI prompt
PROMPT = """
Context: This is a sample learning goal based on a recent conversation.
Requests: Describe the benefits of using AI in automating workflows.
Clarifications: Provide examples of how AI can enhance efficiency and improve productivity.
"""

# Initialize Selenium WebDriver
def initialize_webdriver():
    driver_path = "./chromedriver"  # Adjust path if necessary
    driver = webdriver.Chrome(executable_path=driver_path)
    return driver

def submit_prompt_to_perplexity(driver, prompt):
    driver.get("https://www.perplexity.ai")
    time.sleep(3)  # Allow page to load

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(prompt)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for response

def open_sources_in_tabs(driver):
    # Use BeautifulSoup to extract source links
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sources = soup.find_all("a", class_="source-link")

    # Open each source link in a new tab
    for source in sources:
        link = source['href']
        driver.execute_script(f"window.open('{link}', '_blank');")
        time.sleep(2)  # Slight delay to avoid browser overload

def main():
    driver = initialize_webdriver()

    try:
        # Step 1: Submit the prompt to Perplexity AI
        submit_prompt_to_perplexity(driver, PROMPT)

        # Step 2: Open source links in new tabs
        open_sources_in_tabs(driver)

        # Pause to allow user verification (or further automation steps)
        time.sleep(30)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

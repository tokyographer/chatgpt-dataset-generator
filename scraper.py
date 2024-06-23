from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_chat(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(5)  # Wait for the page to load fully

    data = {"Anonymous": [], "ChatGPT": []}
    
    # Find elements with the correct attribute
    user_messages = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role="user"]')
    chatgpt_messages = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role="assistant"]')
    
    for message in user_messages:
        data['Anonymous'].append(message.text.strip())
        
    for message in chatgpt_messages:
        data['ChatGPT'].append(message.text.strip())
    
    driver.quit()
    
    return data

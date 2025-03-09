import discord
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Discord credentials (replace with your email and password)
DISCORD_EMAIL = 'tet.ru.am.artos@gmail.com'
DISCORD_PASSWORD = 'tet.ru.am.artos@gmail.com'

# Channel link (replace with your channel link)
CHANNEL_LINK = 'https://discord.com/channels/1334088525397889055/1339159832938414130'

# Browser setup (headless mode)
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def find_input_field_and_send(message):
    try:
        print(f"Looking for the input field...")
        selectors = [
            'div[role="textbox"]',
            'div[class^="slateTextArea"]',
            'div[class*="messageInput"]',
        ]
        input_field = None
        for selector in selectors:
            try:
                input_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                print(f"Input field found using selector: {selector}")
                break
            except:
                continue

        if not input_field:
            raise Exception("Input field not found using any selector")

        print(f"Sending message: {message}")
        input_field.send_keys(message)
        input_field.send_keys(Keys.RETURN)
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

def login_with_email_password():
    try:
        print("Logging in with email and password...")
        driver.get('https://discord.com/login')
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        email_field.send_keys(DISCORD_EMAIL)
        password_field.send_keys(DISCORD_PASSWORD)
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()
        print("Login successful.")
    except Exception as e:
        print(f"Error during login: {e}")

def navigate_to_channel():
    try:
        print(f"Navigating to channel: {CHANNEL_LINK}")
        driver.get(CHANNEL_LINK)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"], div[class^="slateTextArea"], div[class*="messageInput"]'))
        )
        print("Channel loaded successfully.")
        return True
    except Exception as e:
        print(f"Error navigating to channel: {e}")
        return False

async def send_messages():
    while True:
        try:
            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo pray'...")
            find_input_field_and_send("owo pray")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 3'...")
            find_input_field_and_send("owo bj 3")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo pray'...")
            find_input_field_and_send("owo pray")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 3'...")
            find_input_field_and_send("owo bj 3")
            await asyncio.sleep(5)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up KING")  
            await asyncio.sleep(2)

            print("Sending 'Level up'...")  
            find_input_field_and_send("Level up LOVE")  
            await asyncio.sleep(2)  

            print("Sending 'MESSAGE FOR OWNER'...")  
            find_input_field_and_send("AS PER MY OWNER CHATGPT WAITING 2 MIN EXTRA TO PREVENT OWO BAN 💵💵💵💵")  
            await asyncio.sleep(75)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo pray'...")
            find_input_field_and_send("owo pray")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 3'...")
            find_input_field_and_send("owo bj 3")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo pray'...")
            find_input_field_and_send("owo pray")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(5)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 2'...")
            find_input_field_and_send("owo bj 2")
            await asyncio.sleep(20)

            print("Sending 'owo cf 55 t'...")
            find_input_field_and_send("owo cf 55")
            await asyncio.sleep(12)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(9)

            print("Sending 'owo s 16'...")
            find_input_field_and_send("owo s 16")
            await asyncio.sleep(15)

            print("Sending 'owo lucky'...")
            find_input_field_and_send("owo lucky")
            await asyncio.sleep(8)

            print("Sending 'owo cf 51 h'...")
            find_input_field_and_send("owo cf 51 h")
            await asyncio.sleep(16)

            print("Sending 'owo h'...")
            find_input_field_and_send("owo h")
            await asyncio.sleep(10)

            print("Sending 'owo s 24'...")
            find_input_field_and_send("owo s 24")
            await asyncio.sleep(13)

            print("Sending 'owo cf 56 t'...")
            find_input_field_and_send("owo cf 56 t")
            await asyncio.sleep(16)

            print("Sending 'owo bj 1'...")
            find_input_field_and_send("owo bj 1")
            await asyncio.sleep(5)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'WHAT IS UWU'...")
            find_input_field_and_send("UWU WAS HACKED")
            await asyncio.sleep(2)

            print("Sending 'UWU HACKED'...")
            find_input_field_and_send("UWU HACK SORRY")
            await asyncio.sleep(2)

            print("Sending 'MESSAGE FOR OWNER'...")
            find_input_field_and_send("AS PER MY OWNER CHATGPT WAITING 2.5 MIN EXTRA TO PREVENT OWO BAN💵💵💵💵")
            await asyncio.sleep(3)
        except Exception as e:
            print(f"Error in send_messages: {e}")
            print("Checking for reconnection...")  # Network reconnect handling
            await reconnect()

async def reconnect():
    while True:
        try:
            driver.get("https://www.google.com")  # Check internet connection
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
            print("Internet is back! Restarting Discord automation...")
            if navigate_to_channel():
                print("Restarting message automation...")
                await send_messages()
                break
        except Exception:
            print("No internet connection. Retrying in 10 seconds...")
            await asyncio.sleep(10)

# Start automation
print("Starting automation...")
login_with_email_password()
time.sleep(10)  # Wait 10 seconds before logging in again
login_with_email_password()
if navigate_to_channel():
    print("Starting message automation...")
    asyncio.run(send_messages())

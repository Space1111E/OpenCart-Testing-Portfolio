from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import traceback

def test_opencart_demo_login():
    chrome_options = Options()
    # Add a user-agent to reduce bot detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/114.0.0.0 Safari/537.36")
    # Optional: Disable automation flags
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    service = Service('C:/Users/USER/OneDrive/Desktop/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    try:
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        print("Page loaded")
        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        # Wait some extra seconds in case of slow load or interstitial
        time.sleep(5)

        # Optional: print page snippet to debug
        print(driver.page_source[:1000])

        email_input = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, "input-email"))
        )
        email_input.clear()
        email_input.send_keys("testuser@example.com")

        password_input = driver.find_element(By.ID, "input-password")
        password_input.clear()
        password_input.send_keys("Test1234!")

        login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        login_button.click()
        print("Clicked login button")

        time.sleep(3)  # wait after login attempt

        try:
            error_alert = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
            )
            error_text = error_alert.text
            if "Account has not been verified yet" in error_text:
                print("Login failed: Account not verified yet!")
                return
            else:
                print("Login failed with error:", error_text)
                return
        except:
            logout_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
            )
            print("Login successful! Logout link found.")

    except Exception as e:
        print(f"Exception during test: {e}")
        traceback.print_exc()
        driver.save_screenshot("error_screenshot.png")

    finally:
        # Replace input() with sleep if you want to see browser briefly during test
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    test_opencart_demo_login()

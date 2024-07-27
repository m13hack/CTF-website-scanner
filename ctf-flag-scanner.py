from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import time

def scan_page(url, flag_pattern):
    """Fetch the fully rendered page source and search for flags using the provided pattern."""
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    # Specify the path to chromedriver
    service = Service('/path/to/chromedriver')  # Update with your chromedriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for JavaScript to load (adjust as needed)
        page_source = driver.page_source  # Get the rendered page source
        flags = re.findall(flag_pattern, page_source)
        return flags, page_source
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return [], ""
    finally:
        driver.quit()

def scan_robots_txt(url, flag_pattern):
    """Fetch the robots.txt file and search for flags using the provided pattern."""
    if not url.endswith('/'):
        url += '/'
    robots_url = url + 'robots.txt'
    return scan_page(robots_url, flag_pattern)

def main():
    # Get user inputs
    website_url = input("Enter the website URL: ").strip()
    flag_type = input("Enter the flag type pattern (e.g., CTF{[^}]+}): ").strip()
    
    print(f"Scanning {website_url} for flags matching pattern: {flag_type}")
    
    # Scan the main page
    flags, page_source = scan_page(website_url, flag_type)
    if flags:
        print("Flags found in the main page:")
        for flag in flags:
            print(flag)
    else:
        print("No flags found in the main page.")
    
    # Optionally, print or save the page source
    # To print the page source (optional, for debugging purposes):
    # print("\nPage Source:\n", page_source)

    # Scan robots.txt
    flags, _ = scan_robots_txt(website_url, flag_type)
    if flags:
        print("Flags found in robots.txt:")
        for flag in flags:
            print(flag)
    else:
        print("No flags found in robots.txt.")

if __name__ == "__main__":
    main()

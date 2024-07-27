import requests
from bs4 import BeautifulSoup
import re
import exifread
from urllib.parse import urljoin

# Define the URL to scan
base_url = "http://example.com"

# Common patterns for CTF flags
flag_patterns = [r'FLAG{.*?}', r'CTF{.*?}', r'flag{.*?}']

def find_flags(text):
    flags = []
    for pattern in flag_patterns:
        flags.extend(re.findall(pattern, text))
    return flags

def scan_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            flags = find_flags(soup.get_text())
            if flags:
                print(f"Flags found on {url}: {flags}")

            # Check for comments in HTML source code
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            for comment in comments:
                flags = find_flags(comment)
                if flags:
                    print(f"Flags found in comments on {url}: {flags}")

            # Check linked JavaScript files
            for script in soup.find_all('script', src=True):
                script_url = urljoin(base_url, script['src'])
                scan_js(script_url)

            # Find and scan all links on the page
            for link in soup.find_all('a', href=True):
                link_url = urljoin(base_url, link['href'])
                scan_page(link_url)
        else:
            print(f"Failed to access {url}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def scan_js(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            flags = find_flags(response.text)
            if flags:
                print(f"Flags found in JavaScript on {url}: {flags}")
        else:
            print(f"Failed to access {url}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def scan_cookies(url):
    try:
        session = requests.Session()
        session.get(url)
        cookies = session.cookies
        for cookie in cookies:
            flags = find_flags(cookie.value)
            if flags:
                print(f"Flags found in cookies on {url}: {flags}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def scan_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        for header in headers.values():
            flags = find_flags(header)
            if flags:
                print(f"Flags found in headers on {url}: {flags}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

def scan_robots_txt(url):
    robots_url = urljoin(url, '/robots.txt')
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            flags = find_flags(response.text)
            if flags:
                print(f"Flags found in robots.txt on {robots_url}: {flags}")
        else:
            print(f"Failed to access {robots_url}")
    except requests.RequestException as e:
        print(f"Error accessing {robots_url}: {e}")

def scan_metadata(url):
    try:
        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        tags = exifread.process_file(response.raw)
        for tag in tags.values():
            flags = find_flags(str(tag))
            if flags:
                print(f"Flags found in metadata on {url}: {flags}")
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")

# Start scanning from the main URL
scan_page(base_url)
scan_cookies(base_url)
scan_headers(base_url)
scan_robots_txt(base_url)
# Add more function calls for other methods as necessary

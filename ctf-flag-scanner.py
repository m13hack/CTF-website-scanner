import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

def scan_website(url, flag_formats, max_pages=5):
    found_flags = []
    visited_pages = set()

    def scan_page(page_url):
        if page_url in visited_pages:
            return
        visited_pages.add(page_url)

        try:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            for flag_format in flag_formats:
                flags = re.findall(flag_format, soup.text)
                if flags:
                    found_flags.extend(flags)

            # Find all links on the page and scan them recursively
            for link in soup.find_all('a'):
                link_url = urljoin(page_url, link.get('href'))
                if link_url.startswith(url) and len(visited_pages) < max_pages:
                    scan_page(link_url)

        except Exception as e:
            print(f"Error scanning {page_url}: {str(e)}")

    scan_page(url)
    return found_flags

# Example usage
url = "http://example.com"
flag_formats = [r"FLAG{.*}", r"flag{.*}", r"CTF{.*}"]
found_flags = scan_website(url, flag_formats)
print("Found flags:")
for flag in found_flags:
    print(flag)

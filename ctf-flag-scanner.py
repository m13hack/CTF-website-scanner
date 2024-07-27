import requests
import re

def scan_page(url, flag_pattern):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            flags = re.findall(flag_pattern, response.text)
            return flags
        else:
            return []
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def scan_robots_txt(url, flag_pattern):
    if not url.endswith('/'):
        url += '/'
    robots_url = url + 'robots.txt'
    return scan_page(robots_url, flag_pattern)

def main():
    website_url = input("Enter the website URL: ").strip()
    flag_type = input("Enter the flag type pattern (e.g., CTF{[^}]+}): ").strip()
    
    print(f"Scanning {website_url} for flags matching pattern: {flag_type}")
    
    # Scan main page
    flags = scan_page(website_url, flag_type)
    if flags:
        print("Flags found in the main page:")
        for flag in flags:
            print(flag)
    else:
        print("No flags found in the main page.")

    # Scan robots.txt
    flags = scan_robots_txt(website_url, flag_type)
    if flags:
        print("Flags found in robots.txt:")
        for flag in flags:
            print(flag)
    else:
        print("No flags found in robots.txt.")

if __name__ == "__main__":
    main()

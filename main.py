from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep
import json

def get_taxonomy_html():
    """
    This function uses Selenium to navigate to the webpage and retrieve the HTML source code,
    saving it to a file.
    """
    url = 'https://bugcrowd.com/vulnerability-rating-taxonomy'

    # Set up the WebDriver for Chrome (if ChromeDriver is in your PATH, this should work without specifying the path)
    service = Service(executable_path='chromedriver.exe')  # Replace with the path to your ChromeDriver if needed
    driver = webdriver.Chrome(service=service)

    # Navigate to the URL
    driver.get(url)

    # Give time for the page to load completely
    sleep(3)

    # Get the page source (HTML)
    html_source = driver.page_source

    # Save the HTML source to a file
    with open('taxonomy.html', 'w', encoding='utf-8') as file:
        file.write(html_source)

    print("Downloaded and saved taxonomy.html using Selenium.")

    # Close the browser
    driver.quit()

def list_vulns_by_subcategory(html_file):
    with open(html_file, encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

        # Extract the JSON-like structure from the 'data-react-props' attribute
        taxonomy_data = soup.find('div', {'data-react-class': 'VrtPublic'}).get('data-react-props')
        taxonomy_json = json.loads(taxonomy_data)

        # Traverse the JSON structure and extract subcategories
        for category in taxonomy_json['vrtJson']:
            print(f"Category: {category['name']}")
            for subcategory in category.get('children', []):
                print(f"  Subcategory: {subcategory['name']}")
                for variant in subcategory.get('children', []):
                    print(f"    Variant: {variant['name']} (Priority: {variant.get('priority', 'N/A')})")


def main():
    get_taxonomy_html()
    list_vulns_by_subcategory('taxonomy.html')

if __name__ == '__main__':
    main()

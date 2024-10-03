from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from time import sleep

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

def list_vulns_by_priority(html_file):
    """
    This function parses an HTML file and lists the vulnerabilities by their priorities (P1 to P4)
    by looking for 'span' elements with priority classes and 'td' elements with specific vulnerability names.
    
    :param html_file: Path to the HTML file to be parsed.
    """
    with open(html_file, encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

        # Define priority levels and their corresponding badge classes
        priorities = {
            'P1': 'bc-badge--p1',
            'P2': 'bc-badge--p2',
            'P3': 'bc-badge--p3',
            'P4': 'bc-badge--p4'
        }

        for priority, badge_class in priorities.items():
            # Find all span elements with the priority badge class
            span_elements = soup.find_all('span', class_=f'bc-badge {badge_class}')
            
            if span_elements:
                print(f"\nListing {priority} vulnerabilities:")
                sleep(2)

                for span in span_elements:
                    # Find corresponding vulnerability name in 'td' element
                    td_element = span.find_parent('tr').find('td', {'data-label': 'Specific vulnerability name'})
                    if td_element:
                        print(f"{priority} Vulnerability: {td_element.text.strip()}")
            else:
                print(f"No {priority} vulnerabilities found.")

def main():
    get_taxonomy_html()
    list_vulns_by_priority('taxonomy.html')

if __name__ == '__main__':
    main()

# Vulnerability Taxonomy Scraper

This project was inspired by a hacksmarter video (aka Tyler Ramsbey) where he demoed this page in a bug bounty tip video.
I thought it would be a good practice scenario to scrape the page and create a json file that could be used for other purposes.

The original video can be found here [here](https://www.youtube.com/watch?v=hZeDl76TB7s)


Thanks to Tyler for the inspiration!


## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. **Python 3.x** - You can download it [here](https://www.python.org/downloads/).
2. **Chrome browser** - Make sure it's installed and up to date.
3. **ChromeDriver** - ChromeDriver must match the version of Chrome installed. You can download it from [here](https://chromedriver.chromium.org/downloads).

## Installation

1. **Clone the repository** (or copy the script):

   ```bash
   git clone https://github.com/your-repo/vuln-taxonomy-scraper.git
   cd vuln-taxonomy-scraper
    ```
2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

The chromedriver here is an exe but if on linux just specify the full path to the chromedriver in the script.

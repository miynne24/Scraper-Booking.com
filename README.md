# Booking.com Scraper

This project involves scraping data from Booking.com. The scraper extracts the following eight attributes for each hotel listing:

- Hotel Name
- Hotel Address
- Price
- Rating Score
- Average Review Rating
- Review Count
- Lodging Type
- URL

## Prerequisites

Before running the scraper, you need to install several packages and Chromium for Playwright. Below are the instructions for setting up your environment.

### Package Installation

1. **Activate your Python environment:**
   Open Command Prompt and activate your project environment by navigating to your project directory.
   ```
   C:\Users\Asus\PycharmProjects\BookingScraper\.venv\Scripts\activate
   ```

2. **Install necessary packages:**
   Install the required Python packages using pip.
   ```
   pip install playwright pandas openpyxl
   ```

3. **Install Chromium:**
   Install Chromium, which is required by Playwright for web scraping.
   ```
   playwright install chromium
   ```

   Alternatively, you can directly add these packages through your Integrated Development Environment (IDE), such as PyCharm.

## Running the Application

To execute the scraper, you have two options:

1. **From an IDE:**
   Run the script directly from your IDE (e.g., PyCharm). Make sure you are in the correct project environment where the dependencies were installed.

2. **Using Command Line:**
   Navigate to your project directory in your command prompt and run the scraper script:
   ```
   python booking_scraper.py
   ```

   You can scrape the data on booking.com as much as you want, you just need to change the value for scroll_step and timeout. Happy Scraping :)

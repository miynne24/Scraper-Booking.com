from playwright.sync_api import sync_playwright
import pandas as pd

def main():

    with sync_playwright() as p:

        destination = 'Kuala+Lumpur'
        checkin_date='2024-06-21'
        checkout_date='2024-06-23'
        lang='en'

        page_url=f'https://www.booking.com/searchresults.html?ss={destination}&ssne={destination}&ssne_untouched={destination}&label=gen173nr-1FCAEoggI46AdIM1gEaKEBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKX68izBsACAdICJGMxM2Q0NjE0LWRhZDEtNDY3Ni1iOThjLTNkNGEzZGFlMjg2ZdgCBeACAQ&sid=f9d0ad33086a56b2cc3cfecfe9bd03c7&aid=304142&lang={lang}&sb=1&src_elem=sb&src=index&dest_id=&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'

        browser=p.chromium.launch(headless=False)
        page=browser.new_page()

        try:
            page.goto(page_url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print("Failed to load the page:", e)
            # Optional: Retry or handle the error in other ways (e.g., try a different page or close the browser)

        # Incremental scrolling to load content
        scroll_step = 500
        last_position = page.evaluate("window.scrollY")
        while True:
            page.evaluate(f"window.scrollBy(0, {scroll_step})")
            page.wait_for_timeout(1000)
            current_position = page.evaluate("window.scrollY")
            if current_position == last_position:
                break
            last_position = current_position

        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_list = []
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['address'] = hotel.locator('//span[@data-testid="address"]').inner_text()
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]
            hotel_dict['lodgingtype'] = hotel.locator('//h4[@class="b290e5dfa6 cf1a0708d9"]').inner_text()
            hotel_dict['url'] = hotel.locator('//a[@data-testid="availability-cta-btn"]').get_attribute('href')

            # Extracting detailed deals information from the aria-label attribute
            deals_element = hotel.locator('//span[@data-testid="property-card-deal"]')
            if deals_element.count() > 0:
                hotel_dict['deals'] = deals_element.get_attribute('aria-label')
            else:
                hotel_dict['deals'] = "No deals available"

            hotel_dict['url'] = hotel.locator('//a[@data-testid="availability-cta-btn"]').get_attribute('href')

            hotels_list.append(hotel_dict)

        df = pd.DataFrame(hotels_list)
        df.to_csv('KL_list_hotel.csv', index=False)

        browser.close()

if __name__ =='__main__':
    main()

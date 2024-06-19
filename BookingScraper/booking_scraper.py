from playwright.sync_api import sync_playwright
import pandas as pd

def main():

    with sync_playwright() as p:

        checkin_date='2024-06-21'
        checkout_date='2024-06-23'
        destination='Johor+Bahru'

        page_url=f'https://www.booking.com/searchresults.ms.html?ss={destination}&ssne={destination}&ssne_untouched={destination}&label=gen173nr-1FCAEoggI46AdIM1gEaKEBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKX68izBsACAdICJGMxM2Q0NjE0LWRhZDEtNDY3Ni1iOThjLTNkNGEzZGFlMjg2ZdgCBeACAQ&sid=f9d0ad33086a56b2cc3cfecfe9bd03c7&aid=304142&lang=ms&sb=1&src_elem=sb&src=index&dest_id=-2405456&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults=2&no_rooms=1&group_children=0'

        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(page_url,timeout=60000)

        hotels = page.locator('//div[@data-testid="property-card"]').all()
        print(f'There are: {len(hotels)} hotels.')

        hotels_list = []
        for hotel in hotels:
            hotel_dict = {}
            hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()
            hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
            hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
            hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
            hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]

            hotels_list.append(hotel_dict)

        df = pd.DataFrame(hotels_list)
        df.to_csv('KL_list_hotel.csv', index=False)

        browser.close()

if __name__ =='__main__':
    main()
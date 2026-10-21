import requests
import json
import time

URL="https://nofluffjobs.com/api/joboffers/main"
destination_folder = "data/raw_nfj.json"

def fetch_data_from_api():
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
    
    current_page = 1
    total_pages = 1
    job_offers = []

    print("\nDonwloading the offers from NoFluffJobs")

    while current_page <= total_pages:

        params = {
            "pageTo": current_page,
            "pageSize": 20,
            "withSalaryMatch": "true",
            "salaryCurrency": "original",
            "salaryPeriod": "original",
            "region": "pl",
            "language": "pl-PL",
        }

        response = requests.get(URL, params=params, headers=headers)
        response.raise_for_status()

        response_json = response.json()
        offers_on_page = response_json.get("postings", [])

        if current_page == 1:
            total_pages = response_json.get("totalPages", 1)
            total_count = response_json.get("totalCount", 0)
            print(f"APIs number of offers: {total_count}. Number of pages: {total_pages}")

        if offers_on_page == []:
            print("\nNo offers left")
            break

        print(f"Donwloaded {len(offers_on_page)}. Total number of offers: {len(job_offers)}")

        job_offers.extend(offers_on_page)

        current_page += 1
        time.sleep(0.5)

    with open(destination_folder, "w", encoding="utf-8") as f:
                json.dump(job_offers, f, ensure_ascii=False, indent=4)

    print(f"\nOffers saved to {destination_folder}")

    print(f"\nDonwloading from NoFluffJobs done. Downloaded offers: {len(job_offers)}")

if __name__ == "__main__":
    fetch_data_from_api()
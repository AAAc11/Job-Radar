import requests
import time
import json
from pathlib import Path


def fetch_bdj_data_from_api():
    URL = "https://bulldogjob.pl/graphql"
    default_path = Path(__file__).resolve().parent.parent / "data" / "raw_bdj.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:159.0) "
        "Gecko/20100101 Firefox/159.0",
        "content-type": "application/json",
        "Origin": "https://bulldogjob.pl",
        "Referer": "https://bulldogjob.pl/companies/jobs",
    }

    page = 1

    payload = {
        "operationName": "searchJobs",
        "query": """query searchJobs
        ($page: Int,
        $perPage: Int,
        $filters: JobFilters,
        $order: JobsSearchOrderBy,
        $language: LocaleEnum,
        $country: String,
        $boostWhere: BoostWhere,
        $exclude: [ID!])
        {\n
        searchJobs(\n
        page: $page\n
        perPage: $perPage\n
        filters: $filters\n
        order: $order\n
        language: $language\n
        country: $country\n
        boostWhere: $boostWhere\n
        exclude: $exclude\n  ) {\n
        totalCount\n
        nodes {\n
        id\n
        company {\n
        name\n
        logo {\n
        url(style: \"list\")\n
        __typename\n        }\n
        __typename\n      }\n
        denominatedSalaryLong {\n
        money\n
        currency\n
        hidden\n
        __typename\n      }\n
        environment {\n
        remotePossible\n
        __typename\n      }\n
        redirectTo\n
        highlight\n
        city\n
        experienceLevel\n
        employmentType\n
        hiddenBrackets\n
        matchingUserBrackets\n
        position\n
        remote\n
        showSalary\n
        technologyTags\n
        contractB2b\n
        contractEmployment\n
        contractOther\n
        locale\n
        __typename\n    }\n
          __typename\n  }\n}\n""",
        "variables": {
            "country": "PL",
            "filters": None,
            "language": "pl",
            "page": page,
            "perPage": 50,
        },
    }

    all_offers = []
    total_number_of_offers = 0

    try:
        while True:
            payload["variables"]["page"] = page
            response = requests.post(URL, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            response = response.json()
            raw_data = (response.get("data") or {}).get("searchJobs") or {}
            total_number_of_offers = raw_data.get("totalCount") or 0
            nodes = raw_data.get("nodes") or []

            if not nodes:
                break

            all_offers.extend(nodes)

            print(
                f"Page: {page} | "
                f"Total number of offers: {total_number_of_offers} | "
                f"Downloaded offers: {len(all_offers)}"
            )

            if len(all_offers) >= total_number_of_offers:
                break

            page += 1

            time.sleep(1)

        default_path.parent.mkdir(parents=True, exist_ok=True)

        with open(default_path, "w", encoding="utf-8") as f:
            json.dump(all_offers, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Error occurred: {e}")
        raise


if __name__ == "__main__":
    print("Downloading data from BullDogJobs API")
    fetch_bdj_data_from_api()

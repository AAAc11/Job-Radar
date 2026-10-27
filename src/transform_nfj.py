import pandas as pd
import json


def get_location(locations):
    if not isinstance(locations, list) or len(locations) == 0:
        return None

    cities = []

    for location in locations:
        city = location.get("city")
        if city is not None and city not in cities:
            cities.append(city)

    if len(cities) > 0:
        cities = ", ".join(cities)
        return cities

    regions = []

    for location in locations:
        region = location.get("region")
        if region is not None and region not in regions:
            regions.append(region)

    if len(regions) > 0:
        regions = ", ".join(regions)
        return regions

    return None


def tranform_json_to_db():
    with open("data/raw_nfj.json", "r", encoding="utf-8") as raw_file:
        raw_data = json.load(raw_file)

        normalized_data = pd.json_normalize(raw_data)

        normalized_data = normalized_data.drop(
            columns=[
                "help4Ua",
                "reference",
                "searchBoost",
                "location.covidTimeRemotely",
                "location.hybridDesc",
                "logo.original",
                "logo.jobs_details",
                "logo.jobs_listing",
                "logo.jobs_details_2x",
                "logo.jobs_listing_2x",
                "logo.companies_details",
                "logo.companies_listing",
                "logo.jobs_details_webp",
                "logo.jobs_listing_webp",
                "logo.companies_details_2x",
                "logo.companies_listing_2x",
                "logo.jobs_details_2x_webp",
                "logo.jobs_listing_2x_webp",
                "logo.original_pixel_image",
                "logo.companies_details_webp",
                "logo.companies_listing_webp",
                "logo.companies_details_2x_webp",
                "logo.companies_listing_2x_webp",
                "topInSearch",
                "highlighted",
                "flavors",
                "tiles.values",
                "salary.disclosedAt",
                "salary.flexibleUpperBound",
                "salary.containsSalary",
                "referralBonus",
                "referralBonusCurrency",
                "location.fullyRemote",
                "regions",
            ]
        )

        normalized_data["seniority"] = normalized_data["seniority"].str[0]
        normalized_data["location.places"] = normalized_data["location.places"].apply(
            get_location
        )
        normalized_data["posted"] = pd.to_datetime(normalized_data["posted"], unit="ms")
        normalized_data["renewed"] = pd.to_datetime(
            normalized_data["renewed"], unit="ms"
        )
        normalized_data.columns = normalized_data.columns.str.replace(".", "_")

        return normalized_data


if __name__ == "__main__":
    tranform_json_to_db()

"""
Q1 - Houses of Ice and Fire
============================
Tasks:
    a. Fetch all houses and regions from the API
    b. Write the list to a text file
    c. Sort all houses alphabetically

API: https://anapioficeandfire.com/api/houses
Author: Intern Assignment
"""

import requests
import os

# ─── Configuration ────────────────────────────────────────────
BASE_URL    = "https://anapioficeandfire.com/api/houses"
OUTPUT_FILE = "houses_output.txt"
PAGE_SIZE   = 50       # Max records the API allows per page


def fetch_all_houses():
    """
    Fetches ALL houses from the API by looping through pages.
    The API is paginated — it gives 50 records per page max.
    We keep requesting next pages until we get an empty response.
    """
    all_houses = []
    page       = 1

    print("Fetching houses from API...")

    while True:
        params   = {"page": page, "pageSize": PAGE_SIZE}
        response = requests.get(BASE_URL, params=params)

        # Stop if the API returns an error
        if response.status_code != 200:
            print(f"Error fetching page {page}: HTTP {response.status_code}")
            break

        data = response.json()

        # Stop if no more records returned
        if not data:
            break

        all_houses.extend(data)
        print(f"  Page {page} fetched — {len(data)} houses")
        page += 1

    print(f"\nTotal houses fetched: {len(all_houses)}")
    return all_houses


def extract_house_region_list(houses):
    """
    From raw API data, pull out just the house name and region.
    Returns a list of dicts: [{"name": ..., "region": ...}, ...]
    """
    extracted = []

    for house in houses:
        name   = house.get("name", "Unknown House")
        region = house.get("region", "Unknown Region")

        # Skip entries with no name
        if name and name != "Unknown House":
            extracted.append({"name": name, "region": region})

    return extracted


def sort_houses_alphabetically(house_list):
    """
    Sorts the list of houses alphabetically by house name.
    Uses Python's built-in sorted() — no extra library needed.
    """
    return sorted(house_list, key=lambda h: h["name"].lower())


def write_to_text_file(sorted_houses, filename):
    """
    Writes all house names and their regions to a .txt file.
    Format per line: House Name  |  Region
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 65 + "\n")
        f.write("       HOUSES OF ICE AND FIRE — ALPHABETICAL LIST\n")
        f.write("=" * 65 + "\n")
        f.write(f"{'#':<5} {'House Name':<40} {'Region'}\n")
        f.write("-" * 65 + "\n")

        for index, house in enumerate(sorted_houses, start=1):
            f.write(f"{index:<5} {house['name']:<40} {house['region']}\n")

        f.write("-" * 65 + "\n")
        f.write(f"Total Houses: {len(sorted_houses)}\n")
        f.write("=" * 65 + "\n")

    print(f"Output written to: {filepath}")
    return filepath


def display_preview(sorted_houses, preview_count=10):
    """
    Prints a preview of the first N houses to the console.
    """
    print(f"\n{'='*65}")
    print(f"  PREVIEW — First {preview_count} Houses (Alphabetically Sorted)")
    print(f"{'='*65}")
    print(f"{'#':<5} {'House Name':<40} {'Region'}")
    print(f"{'-'*65}")

    for i, house in enumerate(sorted_houses[:preview_count], start=1):
        print(f"{i:<5} {house['name']:<40} {house['region']}")

    print(f"{'-'*65}")
    print(f"... and {len(sorted_houses) - preview_count} more houses in the output file.\n")


def main():
    print("=" * 65)
    print("  Q1 — Houses of Ice and Fire")
    print("=" * 65)

    # Step 1 — Fetch all houses from API
    raw_houses = fetch_all_houses()

    # Step 2 — Extract name + region from each house
    house_list = extract_house_region_list(raw_houses)

    # Step 3 — Sort alphabetically
    sorted_houses = sort_houses_alphabetically(house_list)
    print(f"Sorted {len(sorted_houses)} houses alphabetically.")

    # Step 4 — Write to text file
    write_to_text_file(sorted_houses, OUTPUT_FILE)

    # Step 5 — Show preview in console
    display_preview(sorted_houses)

    print("Q1 Complete! Check 'houses_output.txt' for the full list.")


if __name__ == "__main__":
    main()

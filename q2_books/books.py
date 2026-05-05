"""
Q2 - Books of Ice and Fire
===========================
Tasks:
    a. Read list of books from the API
    b. Create a dictionary: {book_name: [pages, date_of_release, ISBN, publisher]}
    c. Write that dictionary to a CSV file

API: https://anapioficeandfire.com/api/books
Author: Intern Assignment
"""

import requests
import csv
import os

# ─── Configuration ────────────────────────────────────────────
BASE_URL    = "https://anapioficeandfire.com/api/books"
OUTPUT_FILE = "books_output.csv"
PAGE_SIZE   = 50


def fetch_all_books():
    """
    Fetches ALL books from the API.
    Handles pagination automatically — keeps requesting
    next pages until no more records are returned.
    """
    all_books = []
    page      = 1

    print("Fetching books from API...")

    while True:
        params   = {"page": page, "pageSize": PAGE_SIZE}
        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            print(f"Error on page {page}: HTTP {response.status_code}")
            break

        data = response.json()

        if not data:
            break

        all_books.extend(data)
        print(f"  Page {page} fetched — {len(data)} book(s)")
        page += 1

    print(f"\nTotal books fetched: {len(all_books)}")
    return all_books


def build_books_dictionary(books):
    """
    Builds a dictionary from the raw API data.

    Structure:
        {
            "A Game of Thrones": [694, "1996-08-01", "978-0553103540", "Bantam Books"],
            "A Clash of Kings":  [768, "1999-02-02", "978-0553108033", "Bantam Books"],
            ...
        }

    - book_name      → key
    - numberOfPages  → index 0
    - released       → index 1 (date string cleaned up)
    - isbn           → index 2
    - publisher      → index 3
    """
    books_dict = {}

    for book in books:
        name          = book.get("name", "Unknown Title")
        pages         = book.get("numberOfPages", 0)
        date_released = book.get("released", "Unknown")
        isbn          = book.get("isbn", "Unknown")
        publisher     = book.get("publisher", "Unknown")

        # The API returns date in ISO format like "1996-08-01T00:00:00"
        # We clean it to just show the date part "1996-08-01"
        if "T" in date_released:
            date_released = date_released.split("T")[0]

        books_dict[name] = [pages, date_released, isbn, publisher]

    return books_dict


def write_to_csv(books_dict, filename):
    """
    Writes the books dictionary to a CSV file.

    CSV Columns:
        Book Name | Pages | Date of Release | ISBN | Publisher
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        writer.writerow(["Book Name", "Pages", "Date of Release", "ISBN", "Publisher"])

        # Write each book as a row
        for book_name, details in books_dict.items():
            pages, date_released, isbn, publisher = details
            writer.writerow([book_name, pages, date_released, isbn, publisher])

    print(f"CSV written to: {filepath}")
    return filepath


def display_dictionary_preview(books_dict):
    """
    Prints the dictionary to console in a readable format.
    """
    print(f"\n{'='*75}")
    print("  BOOKS DICTIONARY — {book_name: [pages, release_date, ISBN, publisher]}")
    print(f"{'='*75}")

    for book_name, details in books_dict.items():
        pages, date_released, isbn, publisher = details
        print(f"\n  Book      : {book_name}")
        print(f"  Pages     : {pages}")
        print(f"  Released  : {date_released}")
        print(f"  ISBN      : {isbn}")
        print(f"  Publisher : {publisher}")
        print(f"  {'-'*70}")

    print(f"\nTotal books in dictionary: {len(books_dict)}\n")


def main():
    print("=" * 75)
    print("  Q2 — Books of Ice and Fire")
    print("=" * 75)

    # Step a — Fetch all books from API
    raw_books = fetch_all_books()

    # Step b — Build the dictionary
    books_dict = build_books_dictionary(raw_books)
    print(f"Dictionary built with {len(books_dict)} entries.")

    # Step c — Write to CSV file
    write_to_csv(books_dict, OUTPUT_FILE)

    # Print dictionary to console
    display_dictionary_preview(books_dict)

    print("Q2 Complete! Check 'books_output.csv' for the full CSV.")


if __name__ == "__main__":
    main()

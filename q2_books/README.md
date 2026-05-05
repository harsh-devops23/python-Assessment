# Q2 — Books of Ice and Fire

## What This Does
Fetches all books from the Ice and Fire API, builds a Python dictionary
mapping each book name to its details, then writes everything to a CSV file.

## Tech Stack
- Python 3.x
- `requests` — API calls
- `csv` — built-in Python library for writing CSV files (no install needed)

## How to Run

### Step 1 — Install dependency
```
pip install -r requirements.txt
```

### Step 2 — Run the script
```
python books.py
```

### Output
- `books_output.csv` — CSV file with columns: Book Name, Pages, Date of Release, ISBN, Publisher
- Console also prints the full dictionary in readable format

## File Structure
```
q2_books/
├── books.py             ← Main script
├── requirements.txt     ← Dependencies
├── books_output.csv     ← Generated after running (auto-created)
└── README.md
```

## Dictionary Structure Created
```python
{
    "A Game of Thrones": [694, "1996-08-01", "978-0553103540", "Bantam Books"],
    "A Clash of Kings":  [768, "1999-02-02", "978-0553108033", "Bantam Books"],
    ...
}
```

## API Used
```
GET https://anapioficeandfire.com/api/books
```

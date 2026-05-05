# Q1 — Houses of Ice and Fire

## What This Does
Fetches all houses and their regions from the Ice and Fire API,
sorts them alphabetically, and writes the result to a text file.

## Tech Stack
- Python 3.x
- `requests` library — for making API calls

## How to Run

### Step 1 — Install dependency
```
pip install -r requirements.txt
```

### Step 2 — Run the script
```
python houses.py
```

### Output
- `houses_output.txt` — full alphabetically sorted list of all houses and regions

## File Structure
```
q1_houses/
├── houses.py            ← Main script
├── requirements.txt     ← Dependencies
├── houses_output.txt    ← Generated after running (auto-created)
└── README.md
```

## API Used
```
GET https://anapioficeandfire.com/api/houses?page=1&pageSize=50
```
The API is paginated. The script loops through all pages automatically
until all houses are collected.

# Q3 — Characters of Ice and Fire

## What This Does
Fetches all characters from the Ice and Fire API, counts how many TV seasons
each character appeared in, sorts them by appearances (most to least),
and writes the full sorted data to a formatted Excel file.

## Tech Stack
- Python 3.x
- `requests` — API calls
- `openpyxl` — writing formatted Excel (.xlsx) files

## How to Run

### Step 1 — Install dependencies
```
pip install -r requirements.txt
```

### Step 2 — Run the script
```
python characters.py
```

> Note: This script fetches a large dataset from the API.
> It may take 1–2 minutes to complete all page requests.

### Output
- `characters_output.xlsx` — Excel file with all character data sorted by season appearances
- Console also prints top 15 characters as a preview

## File Structure
```
q3_characters/
├── characters.py            ← Main script
├── requirements.txt         ← Dependencies
├── characters_output.xlsx   ← Generated after running (auto-created)
└── README.md
```

## Excel Columns
| Column           | Description                                  |
|------------------|----------------------------------------------|
| Rank             | Position after sorting by season count       |
| Character Name   | Name or alias of the character               |
| Gender           | Gender from API                              |
| Culture          | Cultural background                          |
| Status           | Alive or Deceased                            |
| Titles           | All titles held                              |
| Aliases          | Known aliases                                |
| Season Count     | Number of TV seasons appeared in             |
| Seasons Appeared | Which seasons (e.g. Season 1, Season 2...)   |
| Books Count      | Number of books appeared in                  |

## API Used
```
GET https://anapioficeandfire.com/api/characters?page=1&pageSize=50
```

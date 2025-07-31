# Samdesk - Interview

This script analyzes reactor level reports and counts how many are **safe** based on two conditions:

1. The numbers are strictly increasing or decreasing.
2. The difference between any two adjacent numbers is between 1 and 3 (inclusive).

## Files

- `safe.py` – The main Python script
- `sample_data.txt` – Example input data (one report per line)

## How to Run

```bash
python3 safe.py < sample_data.txt

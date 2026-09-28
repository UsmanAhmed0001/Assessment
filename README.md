# Crypto Price Fetcher using API

Fetches live Bitcoin, Ethereum and Solana prices in GBP, USD and EUR
from the CoinGecko API and saves each coin's prices to its own .csv file. Then also finds the highest, lowest coins and also the average in GBP as expected in extension part.

## Requirements

- Python 3.8 or later


## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python fetch_prices.py
```

This creates three .csv files in the project folder with the format as expected in the assessemnt. 

## Furthermore for Extension

Run this **after** `fetch_prices.py`, since it reads the CSV files:

```bash
python analyse_prices.py
```

It reads the three .csv back in, combines them into one pandas DataFrame,
and prints the highest-priced and lowest-priced coin in GBP and the average
GBP price across the three coins.
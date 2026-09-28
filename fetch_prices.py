import csv
import sys
import time
import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
CURRENCIES = ["gbp", "usd", "eur"]
COINS = {
    "bitcoin": "bitcoin.csv",
    "ethereum": "ethereum.csv",
    "solana": "solana.csv",
}


def fetch_prices(coin_id):
    """calling CoinGecko and returning a dict like {'gbp': x, 'usd': y, 'eur': z}."""
    params = {"ids": coin_id, "vs_currencies": ",".join(CURRENCIES)}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if coin_id not in data:
        raise ValueError(f"No data returned for {coin_id}: {data}")
    return data[coin_id]


def write_csv(filename, prices):
    """Write prices to a CSV with the header currency,price."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["currency", "price"])
        for currency in CURRENCIES:
            writer.writerow([currency, prices[currency]])


def main():
    failures = 0
    for coin_id, filename in COINS.items():
        try:
            prices = fetch_prices(coin_id)
            write_csv(filename, prices)
            print(f"Saved {filename}: {prices}")
        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"Failed for {coin_id}: {e}", file=sys.stderr)
            failures += 1
        time.sleep(1)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
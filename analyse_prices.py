import pandas as pd

FILES = {
    "bitcoin": "bitcoin.csv",
    "ethereum": "ethereum.csv",
    "solana": "solana.csv",
}


def load_combined():
    """Read the three CSVs into one DataFrame with a 'coin' column."""
    frames = []
    for coin, filename in FILES.items():
        df = pd.read_csv(filename)
        df["coin"] = coin
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def main():
    combined = load_combined()
    print("Combined data:")
    print(combined, "\n")

    gbp = combined[combined["currency"] == "gbp"].set_index("coin")["price"]

    highest = gbp.idxmax()
    lowest = gbp.idxmin()
    average = gbp.mean()

    print(f"Highest priced coin in GBP: {highest} (£{gbp[highest]:,.2f})")
    print(f"Lowest priced coin in GBP:  {lowest} (£{gbp[lowest]:,.2f})")
    print(f"Average GBP price:          £{average:,.2f}")


if __name__ == "__main__":
    main()
"""
normalize.py

This script contains functions to normalize data from Yahoo and WSJ CSV files
into a consistent format for further processing.
"""

import re
import pandas as pd


def normalize_yahoo(path_in, path_out="normalized_yahoo.csv"):
    """
    Normalize Yahoo CSV data.

    Args:
        path_in (str): Input CSV file path.
        path_out (str): Output normalized CSV file path.

    Returns:
        pandas.DataFrame: Normalized DataFrame.
    """
    df = pd.read_csv(path_in)

    df['price'] = df['Price'].apply(
        lambda x: float(str(x).split()[0].replace(',', '').strip())
    )
    df['change'] = df['Price'].apply(
        lambda x: float(str(x).split()[1].replace(',', '').strip())
        if len(str(x).split()) > 1 else 0
    )
    df['perc_change'] = df['Price'].apply(
        lambda x: float(str(x).split()[2].replace('%', '').replace(',', '').strip())
        if len(str(x).split()) > 2 else 0
    )

    rex = r'\(([A-Z]+)\)$'
    df['symbol'] = df['Name'].apply(
        lambda x: re.findall(rex, str(x))[0] if re.findall(rex, str(x)) else ""
    )
    df['company_name'] = df['Name'].apply(
        lambda x: re.sub(rex, '', str(x)).strip()
    )

    df['volume'] = df['Volume']

    out = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']]
    out.to_csv(path_out, index=False)
    return out


def normalize_wsj(path_in, path_out="normalized_wsj.csv"):
    """
    Normalize WSJ CSV data.

    Args:
        path_in (str): Input CSV file path.
        path_out (str): Output normalized CSV file path.

    Returns:
        pandas.DataFrame: Normalized DataFrame.
    """
    df = pd.read_csv(path_in)

    rex = r'\(([A-Z]+)\)$'
    df['symbol'] = df['Unnamed: 0'].apply(
        lambda x: re.findall(rex, str(x))[0] if re.findall(rex, str(x)) else ""
    )
    df['company_name'] = df['Unnamed: 0'].apply(
        lambda x: re.sub(rex, '', str(x)).strip()
    )

    df['price'] = df['Last'].apply(
        lambda x: float(str(x).replace(',', '').strip())
    )
    df['change'] = df['Chg'].apply(
        lambda x: float(str(x).replace(',', '').strip())
    )
    df['perc_change'] = df['% Chg'].apply(
        lambda x: float(str(x).replace('%', '').replace(',', '').strip())
    )
    df['volume'] = df['Volume']

    out = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']]
    out.to_csv(path_out, index=False)
    return out

if __name__ == "__main__":
    print("Normalizing Yahoo data...")
    yahoo_norm = normalize_yahoo("ygainers.csv")
    print(yahoo_norm.head())

    print("\nNormalizing WSJ data...")
    wsj_norm = normalize_wsj("wsjgainers.csv")
    print(wsj_norm.head())

    print("\nNormalization complete!")

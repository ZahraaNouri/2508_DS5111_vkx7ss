import sys
import os
import re
import pandas as pd
import pytest
# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bin.gainers.yahoo import GainerYahoo
from bin.gainers.wsj import GainerWSJ

@pytest.fixture
def setup_yahoo_csv(tmp_path):
    # Create Yahoo input CSV file with expected columns and sample data
    file_path = tmp_path / "ygainers.csv"
    df = pd.DataFrame({
        "Name": ["ABC Inc (ABC)", "XYZ Corp (XYZ)"],
        "Price": ["24.95 +5.31 (+27.04%)", "15.00 -1.00 (-6.25%)"],
        "Volume": [1000, 2000]
    })
    df.to_csv(file_path, index=False)
    os.chdir(tmp_path)
    return file_path

def test_yahoo_normalize(setup_yahoo_csv):
    gainer = GainerYahoo()
    gainer.normalize_data()
    # Read the output
    out = pd.read_csv("ygainers_normalized.csv")
    expected_cols = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    for col in expected_cols:
        assert col in out.columns
    # Can add more specific value checks if desired

@pytest.fixture
def setup_wsj_csv(tmp_path):
    file_path = tmp_path / "wsjgainers.csv"
    df = pd.DataFrame({
        "Unnamed: 0": ["Company A (AAA)", "Company B (BBB)"],
        "Last": ["15.00", "30.50"],
        "Chg": ["0.50", "-1.00"],
        "% Chg": ["+3.45%", "-3.20%"],
        "Volume": [1500, 3000]
    })
    df.to_csv(file_path, index=False)
    os.chdir(tmp_path)
    return file_path

def test_wsj_normalize(setup_wsj_csv):
    gainer = GainerWSJ()
    gainer.normalize_data()
    out = pd.read_csv("wsjgainers_normalized.csv")
    expected_cols = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    for col in expected_cols:
        assert col in out.columns

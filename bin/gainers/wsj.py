import os
import pandas as pd
from .base import GainerBase

class GainerWSJ(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("WSJ html download")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/gainers' > wsjgainers.html")

    def extract_csv(self):
        print("WSJ csv create")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('wsjgainers.csv')

    def normalize_data(self):
        print("WSJ normalize csv")
        import re
        import pandas as pd

        df = pd.read_csv("wsjgainers.csv")

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
            lambda x: float(re.findall(r'[-+]?[0-9]*\.?[0-9]+', str(x))[0])
            if re.findall(r'[-+]?[0-9]*\.?[0-9]+', str(x)) else 0
        )
        df['volume'] = df['Volume']

        out = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']]
        out.to_csv("wsjgainers_normalized.csv", index=False)
        print("WSJ normalized CSV saved as wsjgainers_normalized.csv")




if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerWSJ()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()

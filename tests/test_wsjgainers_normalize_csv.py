"""
Test Script for normalize_csv.py for wsjgainers_norm.csv
"""


#import pandas as pd
import sys
import pandas as pd
sys.path.append('.')
#import bin.normalize_csv


def test_normalize_csv():
    """
    Test Function for normalize_csv.py
    INPUT : The wsjgainers_norm.csv
    """


    df = pd.read_csv('wsjgainers_norm.csv')
    #Tests column names/proper number of columns
    expected_cols = {'symbol', 'price', 'price_change', 'price_percent_change'}
    assert set(df.columns) == expected_cols
    # Tests datatypes of columns
    assert df['symbol'].dtype == 'object'
    assert df['price'].dtype == 'float64'
    assert df['price_change'].dtype == 'float64'
    assert df['price_percent_change'].dtype == 'float64'
    # Test that all entries in symbol column are capital letters
    assert df['symbol'].str.isupper().all()

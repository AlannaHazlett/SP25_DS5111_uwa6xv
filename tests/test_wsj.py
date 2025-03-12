import sys
import os
import pandas as pd
sys.path.append('bin/gainers')
from wsj import *
from factory import * 
#import bin.normalize_csv
#'bin/gainers/wsj.py'

def test_download():
    #HTML is downloaded
    GF = GainerFactory('wsj')
    GF.get_downloader()
    assert os.path.exists('home/ubuntu/SP25_DS5111_uwa6xv/wsjgainers.html')
    #HTML converted to raw csv
    assert os.path.exists('home/ubuntu/SP25_DS5111_uwz6xv/wsjgainers.csv')

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

def test_save_with_timestamp():
    #places csv in home/ubuntu/SP25_DS5111_uwa6xv/collected_data/
    assert os.listdir('home/ubunutu/SP25_DS5111_uwa6xv/collected_data/')
    #adds time stamp to filename

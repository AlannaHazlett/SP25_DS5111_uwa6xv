"""
Test module for wsj.py
"""
import sys
import os
import pandas as pd
from factory import GainerFactory
sys.path.append('bin/gainers')
#from wsj import *
#from factory import *
#import bin.normalize_csv
#'bin/gainers/wsj.py'

def test_download():
    """
    Function to test if HTML for wsj gainers downloaded
    """
    #HTML is downloaded
    gf = GainerFactory('wsj')
    gf.get_downloader()
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
    """
    Test function to for timestamp in filename.
    """
    #places csv in home/ubuntu/SP25_DS5111_uwa6xv/collected_data/
    assert os.listdir('home/ubunutu/SP25_DS5111_uwa6xv/collected_data/')
    #adds time stamp to filename

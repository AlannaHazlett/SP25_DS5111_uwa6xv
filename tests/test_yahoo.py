import sys
import pandas as pd
from factory import *
sys.path.append('.')
#import bin.normalize_csv


def test_download():
    #downloads HTML
    GF = GainerFactory('yahoo')
    GF.get_downloader()
    assert os.path.exists('ygainers.html')#home/ubuntu/SP25_DS5111_uwa6xv/wsjgainers.html')
    #HTML converted to raw csv
    assert os.path.exists('ygainers.csv')#'home/ubuntu/SP25_DS5111_uwz6xv/wsjgainers.csv')


def test_normalize_csv():
    """
    Test Function for normalize() from yahoo.py
    INPUT : The ygainers_norm.csv
    """

    df = pd.read_csv('ygainers_norm.csv')
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

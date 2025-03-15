"""
Module to download, process, and save with timestampe the WSJ gainers.
"""
import os
from datetime import datetime
import pandas as pd
from download import GainerDownload
from process import GainerProcess
#Downloader
# pylint: disable=too-few-public-methods
class GainerDownloadWSJ(GainerDownload):
    """
    Class to download the WSJ gainers.
    """
    def __init__(self):
        """
        Initializing method
        """
        #super().__init__('https://www.wsj.com/market-data/stocks/us/movers')

    def download(self):
        """
        Method to download the WSJ gainers.
        """
        print("Downloading WSJ gainers")
        command = """sudo google-chrome-stable \
                  --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
                  'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html"""
        os.system(command)
        convert_command = """python -c 'import pandas as pd; \
                           raw = pd.read_html('wsjgainers.html'); \
                           raw[0].to_csv('wsjgainers.csv')'"""
        os.system(convert_command)
#Processor
class GainerProcessWSJ(GainerProcess):
    """
    Class to normalize or save with timestamp for WSJ gainers.
    """
    def __init__(self):
        """
        Initalizing method
        """
        #pass


    def normalize(self):
        """
        Method to transform raw csv into normalized csv. 
        This is comparable to previous version normalize_csv.py.
        """
        print("Normalizing WSJ gainers")
        wsjgainers = pd.read_csv('sample_data/wsjgainers.csv')
        assert wsjgainers.shape[1] == 6
        print('wsjgainers has been read')
        wsjgainers = wsjgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        wsjgainers = wsjgainers.rename({'Unnamed: 0':'symbol',
                                        'Last':'price',
                                        'Chg':'price_change',
                                        '% Chg':'price_percent_change'}, axis=1)
        wsjgainers['symbol'] = wsjgainers.symbol.str.extract(r'\((\w+)\)')
        wsjgainers = wsjgainers.astype({'symbol': 'str',
                                        'price': 'float',
                                        'price_change': 'float',
                                        'price_percent_change': 'float'})
        assert wsjgainers.shape[1] == 4
        wsjgainers.to_csv('wsjgainers_norm.csv', index = False)


    def save_with_timestamp(self):
        """
        Method to save the raw csv with a timestamp in the filename.
        """
        storage_path = '/home/ubuntu/SP25_DS5111_uwa6xv/collected_data/'
        current_time = datetime.fromtimestamp(datetime.now().timestamp())
        current_time = str(current_time)[:-7]
        print("Saving WSJ gainers")
        filename = "wsjgainers" + current_time + ".csv"
        filename = filename.replace(' ','_')
        os.rename('wsjgainers.csv', storage_path + filename)

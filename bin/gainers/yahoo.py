"""
Module for downloading, normalizing, and saving timestamp for Yahoo gainers.
"""
import os
from datetime import datetime
import pandas as pd
from bin.gainers.download import GainerDownload
from bin.gainers.process import GainerProcess
# Downloader
# pylint: disable=too-few-public-methods
class GainerDownloadYahoo(GainerDownload):
    """
    Class for downloading Yahoo gainers.
    """
    def __init__(self):
        """
        Initializing method
        """
        #super().__init__('https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200')


    def download(self):
        """
        Method to download Yahoo HTML and create CSV.
        """
        print("Downloading yahoo gainers")
        command ="""sudo google-chrome-stable \
                --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 \
                'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' \
                > ygainers.html"""
        os.system(command)
        convert_command = """python -c 'import pandas as pd; \
                          raw = pd.read_html("ygainers.html"); \
                          raw[0].to_csv("ygainers.csv")'"""
        os.system(convert_command)
        print("Done with convert command")


#Processor
class GainerProcessYahoo(GainerProcess):
    """
    Class for processing and saving with timestamp.
    """
    def __init__(self):
        """
        Initializing method
        """
        #super().__init__(choice='yahoo')
        #pass


    def normalize(self):
        """
        Method to normalize raw csv.
        This is similar to previous use of normalize_csv.py
        """
        print("Normalizing yahoo gainers")
        ygainers = pd.read_csv('ygainers.csv')
        assert ygainers.shape[1] == 13
        print('ygainers has been read')
        ygainers = ygainers[['Symbol','Price','Change','Change %']]
        ygainers = ygainers.rename({'Symbol':'symbol',
                                    'Price':'price',
                                    'Change':'price_change',
                                    'Change %':'price_percent_change'}, axis=1)
        ygainers['price'] = ygainers.price.str.split(' ', expand=True)[0]
        #Get rid of comma for thousands place, as it interferes with float conversion
        ygainers['price'] = ygainers.price.str.replace(',', '')
        ygainers['price_percent_change'] = ygainers.price_percent_change.str[1:-1]
        ygainers = ygainers.astype({'symbol': 'str',
                                    'price': 'float',
                                    'price_change': 'float',
                                    'price_percent_change': 'float'})
        assert ygainers.shape[1] == 4
        ygainers.to_csv('ygainers_norm.csv', index = False)


    def save_with_timestamp(self):
        """
        Method to save raw csv with timestamp in filename.
        """
        storage_path = '/home/ubuntu/SP25_DS5111_uwa6xv/collected_data/'
        current_time = datetime.fromtimestamp(datetime.now().timestamp())
        current_time = str(current_time)[:-7]
        print("Saving Yahoo gainers")
        filename = "ygainers" + current_time + ".csv"
        filename = filename.replace(' ','_')
        os.rename('ygainers.csv', storage_path + filename)

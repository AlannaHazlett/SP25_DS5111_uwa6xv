import os
from datetime import datetime
# Downloader
class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass
        

    def download(self):
        print("Downloading yahoo gainers")
        command = "sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html"
        os.system(command)
        convert_command = "python -c 'import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')'"
        os.system(convert_command)
      
#Processor
class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing yahoo gainers")
        ygainers = pd.read_csv('sample_data/ygainers.csv')
        assert ygainers.shape[1] == 13
        print('ygainers has been read')
        ygainers = ygainers[['Symbol','Price','Change','Change %']]
        ygainers = ygainers.rename({'Symbol':'symbol',
                                    'Price':'price',
                                    'Change':'price_change',
                                    'Change %':'price_percent_change'}, axis=1)
        ygainers['price'] = ygainers.price.str.split(' ', expand=True)[0]
        ygainers['price_percent_change'] = ygainers.price_percent_change.str[1:-1]
        ygainers = ygainers.astype({'symbol': 'str',
                                    'price': 'float',
                                    'price_change': 'float',
                                    'price_percent_change': 'float'})
        assert ygainers.shape[1] == 4
        ygainers.to_csv('ygainers_norm.csv', index = False)

    def save_with_timestamp(self, unnorm = True):
        storage_path = '/home/ubuntu/SP25_DS5111_uwa6xv/collected_data/'
        current_time = datetime.fromtimestamp(datetime.now().timestamp())
        current_time = str(current_time)[:-7]
        if unnorm:
            print("Saving Yahoo gainers")
            filename = "ygainers" + current_time + ".csv"
            filename = filename.replace(' ','_')
            os.rename('ygainers.csv', storage_path + filename) 
        else:
            print("Saving Yahoo gainers")
            filename = "ygainers_norm" + current_time + ".csv"
            filename = filename.replace(' ','_')
            os.rename('ygainers_norm.csv', storage_path + filename)
            

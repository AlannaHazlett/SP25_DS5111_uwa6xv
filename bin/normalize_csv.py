import pandas as pd
import sys
assert len(sys.argv)==2
print(sys.argv)
fname = sys.argv[1].strip()

def csv_normalizer(csv):
    if csv == 'sample_data/ygainers.csv':
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
        ygainers = ygainers.astype({'symbol': 'str', 'price': 'float', 'price_change': 'float', 'price_percent_change': 'float'})
        assert ygainers.shape[1] == 4
        ygainers.to_csv('ygainers_norm.csv', index = False)
    elif csv == 'sample_data/wsjgainers.csv':
        wsjgainers = pd.read_csv('sample_data/wsjgainers.csv')
        assert wsjgainers.shape[1] == 6
        print('wsjgainers has been read')
        wsjgainers = wsjgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        wsjgainers = wsjgainers.rename({'Unnamed: 0':'symbol',
                                        'Last':'price',
                                        'Chg':'price_change',
                                        '% Chg':'price_percent_change'}, axis=1)
        wsjgainers['symbol'] = wsjgainers.symbol.str.extract(r'\((\w+)\)')
        wsjgainers = wsjgainers.astype({'symbol': 'str', 'price': 'float', 'price_change': 'float', 'price_percent_change': 'float'})
        assert wsjgainers.shape[1] == 4
        wsjgainers.to_csv('wsjgainers_norm.csv', index = False)
    else:
        print('That is not an accepted csv at this time.')
csv_normalizer(fname)

import pandas as pd
import sys
assert len(sys.argv)==2
print(sys.argv)
fname = sys.argv[1].strip()

def csv_normalizer(csv):
    if csv == 'sample_data/ygainers.csv':
        ygainers = pd.read_csv('sample_data/ygainers.csv')
        print('ygainers has been read')
        ygainers = ygainers[['Symbol','Price','Change','Change %']]
        ygainers = ygainers.rename({'Symbol':'symbol',
                                    'Price':'price',
                                    'Change':'price_change',
                                    'Change %':'price_percent_change'}, axis=1)
        ygainers.to_csv('ygainers_norm.csv', index = False)
    elif csv == 'sample_data/wjsgainers.csv':
        wjsgainers = pd.read_csv('sample_data/wjsgainers.csv')
        print('wjsgainers has been read')
        wjsgainers = wjsgainers[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        wjsgainers = wjsgainers.rename({'Unnamed: 0	':'symbol',
                                        'Last':'price',
                                        'Chg':'price_change',
                                        '% Chg':'price_percent_change'}, axis=1)
        wjsgainers.to_csv('wjsgainers_norm.csv', index = False)
    else:
        print('That is not an accepted csv at this time.')
csv_normalizer(fname)

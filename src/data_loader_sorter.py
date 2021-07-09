import pandas as pd
import numpy
import csv

def data_loader(filename,n):
    """loads data from filename"""
    
    
    
    if filename.endswith('.xlsx'):
        raw = pd.read_excel(filename,header=None)
    elif filename.endswith('.csv'):
        raw = pd.read_csv(filename,header=None)
    else:
        raw = pd.read_table(filename,header=None,delimiter=';')
        if len(raw.columns) != n:
            raw = pd.read_table(filename,header=None,delimiter=',')
            if len(raw.columns) != n:
                raw = pd.read_table(filename,header=None,delimiter=':')
                if len(raw.columns) != n:
                    raw = pd.read_table(filename,header=None,delimiter='/')
                    if len(raw.columns) != n:
                        print('ERROR: set delimiter to \';\' and rerun')
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        pass
    if type(raw.iloc[0,0]) == str:
        feat_list = raw[0].tolist()
        unique_feat = list(set(feat_list))
        unique_keys = dict.fromkeys(unique_feat)
        unique_values = list(range(0,len(unique_keys)))
        unique_dict = dict(zip(unique_keys, unique_values))
        """"Create key:value file to record ID original values"""
        w = csv.writer(open("ID_key.csv", "w"))
        for key, val in unique_dict.items():
            w.writerow([key, val])
        print('raw_pre:', raw)
        raw[0] = raw[0].map(unique_dict)
        print('raw_post:', raw)
    elif type(raw.iloc[0,0]) == numpy.int64:
        pass
    else:
        pass   
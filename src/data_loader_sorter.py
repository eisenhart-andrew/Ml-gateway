import pandas as pd
import numpy
import csv
from sklearn.preprocessing import StandardScaler  

def data_loader(filename,n):
    """
    loads data from filename
    
    n = number of columns
    filenam = data source
    
    """
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
                        print('ERROR: set delimiters to \';\' and rerun')
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        pass
    it=0
    while it < len(raw.columns):
        if type(raw.iloc[0,it]) == str:
            feat_list = raw[it].tolist()
            unique_feat = list(set(feat_list))
            unique_keys = dict.fromkeys(unique_feat)
            unique_values = list(range(0,len(unique_keys)))
            unique_dict = dict(zip(unique_keys, unique_values))
            """"Create key:value file to record ID original values"""
            w = csv.writer(open(f"./../Keys/ID_key-{it}.csv", "w"))
            for key, val in unique_dict.items():
                w.writerow([key, val])
            raw[it] = raw[it].map(unique_dict)
            
        elif type(raw.iloc[0,it]) == numpy.bool_:
            feat_list = raw[it].tolist()
            unique_feat = list(set(feat_list))
            unique_keys = dict.fromkeys(unique_feat)
            unique_values = list(range(0,len(unique_keys)))
            unique_dict = dict(zip(unique_keys, unique_values))
            """"Create key:value file to record ID original values"""
            w = csv.writer(open(f"./../Keys/ID_key-{it}.csv", "w", newline=''))
            for key, val in unique_dict.items():
                w.writerow([key, val])
            raw[it] = raw[it].map(unique_dict)
        else:
            pass
        it += 1
    return raw


def remove_missing(data,threshold):
    """ remove NaN or missing data """
    
    missing = data.isna().sum()
    if missing.sum() == 0:
        no_missing = data
        print('No missing Data')
    elif missing.sum()/len(data)*100 < threshold:
        no_missing = data.dropna(axis=1)
        print(f'Removing {missing.sum()} entries. These make up \
              {missing.sum()/len(data)*100} % of the total data.')
    else:
        numeric = data.select_dtypes(include=numpy.number)
        numeric_columns = numeric.columns
        data[numeric_columns] = data[numeric_columns].fillna(data.mean())
        boolean_columns = data.select_dtypes(include=numpy.object).columns.tolist()
        data[boolean_columns] = data[boolean_columns].astype('bool')
        data[boolean_columns].fillna(data.mode())
        no_missing = data
        print(f'Replacing {missing.sum()} entries. These make up \
              {missing.sum()/len(data)*100} % of the total data.')
    no_missing_X = no_missing.iloc[:,0:len(no_missing.columns)]
    no_missing_y = no_missing.iloc[:,len(no_missing.columns)-1]
    return no_missing_X, no_missing_y

      

def standardize_split(data):
    scaler = StandardScaler()
    for column in data.columns:
        if data[column].dtype == 'int64':
            scaler.fit(data[column])  
            data[column] = scaler.transform(data[column])
        
    return data
        
    
    
    
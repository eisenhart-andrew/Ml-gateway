import pandas as pd

def analyzer(filename):
    """loads data from filename"""
    
    
    
    if filename.endswith('.xlsx'):
        raw = pd.read_excel(filename,header=None)
    elif filename.endswith('.csv'):
        raw = pd.read_csv(filename,header=None)
    else:
        """ edge cases with weird delimiters taken care of with read_table """
        
        raw = pd.read_table(filename,header=None,delimiter=';')
        if len(raw.columns) != 2:
            raw = pd.read_table(filename,header=None,delimiter=',')
            if len(raw.columns) != 2:
                raw = pd.read_table(filename,header=None,delimiter=':')
                if len(raw.columns) != 2:
                    raw = pd.read_table(filename,header=None,delimiter='/')
                    if len(raw.columns) != 2:
                        print('ERROR: set delimiter to \';\' and rerun')
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    
    
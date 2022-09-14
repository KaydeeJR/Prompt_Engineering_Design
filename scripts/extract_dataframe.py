import pandas as pd
import dvc.api

def excel_to_dataframe(filePath,repository,version):
    """
    Read version of data from remote storage
    The data is in excel format. It is converted to a dataframe
    """
    data = dvc.api.read(filePath,
    repo= repository,
    rev=version,
    mode='rb')
    return pd.read_excel(data)
import pandas as pd
import dvc.api
import json

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

def text_to_dataframe(filePath,repository):
    """
    Read text file which is in json format and convert to dataframe.
    TODO: find out why adding version as an argument leads to:
    - dvc.exceptions.PathMissingError: The path does not exist in the target repository neither as a DVC output nor as a Git-tracked file.
    - dvc.exceptions.FileMissingError: Can't find 
file neither locally nor on remote
    - raise KeyError(key)
KeyError: ('data', 'jobs_desc_training_data.txt')
    """
    data = dvc.api.read(filePath,
    repo= repository)
    return pd.read_json(data)

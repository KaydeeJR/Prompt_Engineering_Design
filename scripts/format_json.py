import dvc.api
import pandas as pd
text_data_path = 'relation_extraction_transformer/relations_dev.txt'
repository_path = 'https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt'

def text_to_DF():
    data = dvc.api.read(text_data_path,
                        repo= repository_path,
                        mode='rb')
    print(len(data))
    return pd.read_json(data)

if __name__ == "__main__":
    text_to_DF()
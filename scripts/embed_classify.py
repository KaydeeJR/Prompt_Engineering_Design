"""
A classifier using Cohere's embeddings
"""
import pandas as pd
import os
import cohere
from tqdm import tqdm
from add_to_SQL_DB import db_execute_fetch

# fetching data
dataframe = db_execute_fetch(dBName='news', tablename='newsarticles')
# text/word embedding
co = cohere.Client(os.getenv('cohere_classification'))
#TODO: INSERT DF FEATURES(SENTENCES)
response = co.embed(
    texts = , model="large", truncate="LEFT").embeddings
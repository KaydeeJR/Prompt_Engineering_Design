"""
Co:here's embedding endpoint
"""
import os
import cohere

def embed_data(data_to_convert):
    """
    perform text/word embedding i.e. convert the data into real-valued vectors
    """
    try:
        co = cohere.Client(os.getenv('cohere_classification'))
        response = co.embed(model='medium',
        texts=data_to_convert)
        return response.embeddings
    
    except cohere.CohereError as e:
        print(e.message)
        print(e.http_status)
        print(e.headers)
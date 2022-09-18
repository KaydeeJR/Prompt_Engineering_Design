# This is a simple placeholder for eccomerce, to make it dynamic we need to use a dictionary for different types of items and use the examples based on the item type
import cohere
import os
co = cohere.Client(os.getenv('cohere_classification'))

def extract_job_desc(description1, description2, extract_desc):
    """
    given examples of job description texts, extract important entities/details
    """
    response = co.generate(
            model='xlarge',
            prompt= description1 + description2 + extract_desc,
            max_tokens=50,
            temperature=0.9,
            k=0,
            p=0.75,
            frequency_penalty=0,
            presence_penalty=0,
            stop_sequences=["--SEPARATOR--"],
            return_likelihoods='NONE'
        )
    return response.generations[0].text
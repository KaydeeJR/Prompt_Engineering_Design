"""
Classification endpoint which classifies the text into one of several classes.
Create a classifier from a generative model.
In the background, it constructs a few-shot classification prompt and uses it classify the input texts you pass to it.
"""
import cohere
import os
from cohere.classify import Example

co = cohere.Client(os.getenv('cohere_classification'))

def create_examples(ex_texts,ex_labels):
    """
    Create examples from training data
    """
    examples = list()
    for txt, lbl in zip(ex_texts,ex_labels):
        examples.append(Example(txt,lbl))
    return examples

def classify_data(text_to_classify, examples):
    """
    classify() returns a list
    """
    classifications = co.classify(
    model='medium',
    inputs=text_to_classify.to_json(),
    examples=examples)
    return classifications.classifications[0].prediction
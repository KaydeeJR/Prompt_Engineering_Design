"""
ENDPOINTS:
/bnewscore - for scoring  breaking news that may lead to public unrest
/jdentities - for extracting entities from job description
"""
from fastapi import FastAPI
fast_api = FastAPI()

@fast_api.get(path="/bnewscore")
@fast_api.get(path="/jdentities")

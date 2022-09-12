# Prompt Engineering Design
This repository contains code that generates prompts for a Generative Large Language Model (LLM). The model classifies news artifacts according to a few examples of human scores. The news artifacts are collected from:
* Web pages
* Tweets
* Facebook posts etc.

Given a news artifact, the model determines how relevant it is to a topic. The relevancy varies between 0 and 1.
0 => news item is totally NOT relevant
1 => news item is very relevant

# REPO Structure
1) Data Folder -> text data files
2) Tests folder -> Test scripts
3) Scripts folder -> Python scripts
4) .dvc -> DVC config files
# Installation guide
git clone https://github.com/KaydeeJR/Prompt_Engineering_Design
pip install -r requirements.txt
# ML workflow diagram

# dj_k_tweets

A NLP processing for tweets and a Quote/Tweet Generator using Markov Chains with [markovify](https://github.com/jsvine/markovify).

We love DJ Khaled! And since we cannot get enough and desire `another one`, our data source is DJ Khaled Tweets and Quotes to use as training data for generating Quotes and Tweets.

## Setup

Create `venv`

    python3 -m venv venv

Activate `venv`
    
    source venv/bin/activate

Install requirements

    pip install -r requirements.txt

Add a `.env` file for the Twitter API. Copy `.env.sample` and replace the `****` with your API tokens


https://huggingface.co/gpt2
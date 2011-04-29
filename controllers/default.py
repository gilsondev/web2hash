# -*- coding: utf-8 -*-

# Importing module
import hashweb2py as hashw2p
import FormatTweets as format

def index():
    """
    Lista all the tweets
    """
    tweets_hash = hashw2p.search_hashs_web2py()
   
    for tweet in tweets_hash:
        tweet_format = format.FormatTweets(tweet['text'])
        tweet['text'] = tweet_format.format_links()
   
    return dict(tweets_hash=tweets_hash)


def teste():
    tweets = hashw2p.search_hashs_web2py()
   
    return dict(tweets=tweets)
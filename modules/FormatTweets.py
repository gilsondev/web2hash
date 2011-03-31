"""
File: FormatTweets.py
Author: Gilson Filho
Date: 30/03/2011
License: GPL 2.0
"""
# -*- encoding: utf-8 -*-

import re

# Patterns of the tweets
PATTERN_URL = re.compile('^(http[s]?://|ftp://)|^www\.')
PATTERN_USERNAME = re.compile('^@')
PATTERN_HASH = re.compile('^#')

class FormatTweets(object):
    """
    This script performs a search in the tweet and 
    renders on links in URLs, usernames and hashs.
    
    >>> tweet = FormatTweet('@web2py This is a test: http://web2py.com #web2py #python')
    >>> tweet.format()
    >>> <a href="http://twitter.com/@web2py">@web2py</a> This is a test: <a href="http://web2py.com">http://web2py.com</a>
    <a href="http://search.twiter.com?q=%23web2py">#web2py</a> <a href="http://search.twiter.com?q=%23python">#python</
    a>
    """

    def __init__(self,text):
		self.text = text

	
    def format_all(self):
        """
        Format the tweets with links
        for the URLs, Hashs and 
        usernames.
        """
        tweet = self.text
        for word in tweet.split():
            # Verifing patterns
            link = re.match(PATTERN_URL,word)
            hashtweet = re.match(PATTERN_HASH,word)
            username = re.match(PATTERN_USERNAME,word)

            if link:
                link = '<a href="%s">%s</a>' %(word,word)	
                tweet = tweet.replace(word,link)
            elif hashtweet:
                hashtweet = '<a href="http://search.twiter.com?q=%23'+'%s">%s</a>'%(word[1:],word)
                tweet = tweet.replace(word,hashtweet)
            elif username:
                username = '<a href="http://twitter.com/%s">%s</a>'%(word[1:],word)
                tweet = tweet.replace(word,username)
        return tweet
    
    def format_links(self):
        """
        Format the tweets with
        links.
        """
        tweet = self.text
        for word in tweet.split():
            # Verifing pattern
            link = re.match(PATTERN_URL,word)
            if link:
                link = '<a href="%s">%s</a>' %(word,word)	
                tweet = tweet.replace(word,link)
        return tweet            

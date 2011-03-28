"""
Searching hash with #web2py in the tweets
Author: Gilson Filho
Date: 27/03/2011
"""
from gluon.tools import fetch
import gluon.contrib.simplejson as json

# URL for searching trend with web2py word    
WEB2PY_HASH_SEARCH = 'http://search.twitter.com/search.json?q=%23web2py'

def search_hashs_web2py():
    page = fetch(WEB2PY_HASH_SEARCH)
    
    return json.loads(page)['results']
    

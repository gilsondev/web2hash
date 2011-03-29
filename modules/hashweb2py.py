"""
Searching hash with #web2py in the tweets
Author: Gilson Filho
Date: 27/03/2011
"""
from gluon.tools import fetch
import gluon.contrib.simplejson as json

# URL for searching trend with web2py word    
WEB2PY_HASH_SEARCH = 'http://search.twitter.com/search.json?q=web2py'

# Twitter web2py
USER_WEB2PY = 'http://twitter.com/web2py?format=json'

def search_hashs_web2py():
    page = fetch(WEB2PY_HASH_SEARCH)
    
    return json.loads(page)['results']
    
def timeline_user_web2py():
    page = fetch(USER_WEB2PY)
    
    return json.loads(page)['#timeline']

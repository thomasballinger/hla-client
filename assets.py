"""Hacky asset retrieval"""

import requests

CACHE = 'assetcache'
if not os.path.exists(CACHE):
    os.mkdir(CACHE)
memory_cache = {}

def get_resource(url):
    fname = url.replace('/','_')

    #TODO make the memory cache fixed size, keep track of requests
    # for it, and swap out better things to cache
    #TODO put this in a decorator or 
    #TODO just use memorize (python memcache client)
    if fname not in memory_cache:
        try:
            result = open(fname)
        except IOError:
            result = requests.get(url.content)
            f = open(fname, 'w')
            f.write(result)
            f.close()
        memory_cache[fname] = result
    return memory_cache[fname]


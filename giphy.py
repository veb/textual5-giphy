#!/usr/bin/env python

import sys
import socket
import urllib2
import json

if __name__ == '__main__':
    if sys.argv[2] != '':
        what = sys.argv[2]
        url = "http://api.giphy.com/v1/gifs/search?q={0}&api_key=dc6zaTOxFJmzC&limit=1".format(what)
        data = urllib2.urlopen(url).read()
        j = json.loads(data)
        result = [d['url'] for d in j['data']]
        print result[0]
    else:
        print('/debug Usage: /giphy <search-term>')

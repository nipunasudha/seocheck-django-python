from urllib import parse
from urllib import robotparser
from pyquery import PyQuery as pq


def get_webpage(url, verify):
    return pq(url=url, method='get', verify=verify)

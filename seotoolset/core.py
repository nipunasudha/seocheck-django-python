from urllib import parse
from urllib import robotparser
from pyquery import PyQuery as pq


def get_webpage(url, verify):
    return pq(url=url, method='get', verify=verify)


# Utilities

def wrap_result(data, status, message):
    return {'data': data, 'status': status, 'message': message}

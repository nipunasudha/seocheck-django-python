import urllib
from urllib import request
from urllib import error
from urllib import parse
from bs4 import BeautifulSoup

from seotoolset import wrap_result

msgFavicon = {
    'ok': 'Your webpage has a favicon!',
    'bad': 'No favicon found',
    'error': 'Error occured while finding favicon'
}


def is_absolute(url):
    return bool(parse.urlparse(url).netloc)


def get_url_root(url):
    parsed_uri = parse.urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    # print(domain)
    return domain


def get_favicon_core(url):
    url = get_url_root(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    icon_tag = soup.find("link", rel="shortcut icon")
    if icon_tag is not None:
        icon_url = icon_tag['href']
    else:
        return False
    if not is_absolute(icon_url):
        icon_url = parse.urljoin(url, icon_url)
    return icon_url


def get_favicon(url):
    status = "ok"
    try:
        result = get_favicon_core(url)
        if not result:
            status = 'bad'
            message = msgFavicon['bad']
        else:
            message = msgFavicon['ok']

    except Exception:
        result = []
        status = "error"
        message = msgFavicon['error']

    return wrap_result(result, status, message)

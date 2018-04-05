import urllib
from urllib import request
from urllib import error
from urllib import parse
from urllib import robotparser

from bs4 import BeautifulSoup


def is_absolute(url):
    return bool(parse.urlparse(url).netloc)


def get_url_root(url):
    parsed_uri = parse.urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    # print(domain)
    return domain


def get_favicon(url):
    url = get_url_root(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    icon_tag = soup.find("link", rel="shortcut icon")
    icon_url = icon_tag['href']
    if not is_absolute(icon_url):
        icon_url = parse.urljoin(url, icon_url)
    return icon_url

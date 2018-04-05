from urllib import request
import certifi
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_clean_text(url):
    html = request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'lxml')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

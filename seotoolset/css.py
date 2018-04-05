from pyquery import PyQuery as pq


def get_css_status(url):
    try:
        page = pq(url=url, method='get', verify=False) #TODO move this to an exception handled util function
        return get_css_status_from_pq(page)
    except Exception:
        return


def get_css_status_from_pq(page):
    css_tags = page("[style]")
    status = {
        'bad': 0
    }
    if not css_tags:
        print("No inline CSS")
        return status
    status['bad'] = len(css_tags)
    return status

# print(get_css_status('http://www.ikman.lk'))

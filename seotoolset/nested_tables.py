from pyquery import PyQuery as pq


def get_table_status(url):
    page = pq(url=url, method='get', verify=False)
    return get_table_status_from_pq(page)


def get_table_status_from_pq(page):
    table_tags = page("table table")
    status = {
        'bad': 0
    }
    if not table_tags:
        print("No nested tables")
        return status
    status['bad'] = len(table_tags)
    return status

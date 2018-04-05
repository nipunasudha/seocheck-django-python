from pyquery import PyQuery as pq


def check_h1_tags(page):
    page = pq(page)
    found_tags = page("h1")
    return len(found_tags)


def check_h2_tags(page):
    page = pq(page)
    found_tags = page("h2")
    return len(found_tags)


def check_h3_tags(page):
    page = pq(page)
    found_tags = page("h3")
    return len(found_tags)


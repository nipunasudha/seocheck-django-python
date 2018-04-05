from pyquery import PyQuery as pq


def get_img_status(url):
    page = pq(url=url, method='get', verify=False)
    return get_img_status_from_pq(page)


def get_img_status_from_pq(page):
    img_tags = page("img")
    print(img_tags)
    status = {
        'good': 0,
        'bad': 0
    }
    if not img_tags:
        print("No img_tags")
        return status
    for tag in img_tags.items():
        img_alt = tag.attr('alt') if tag.attr('alt') else ""
        if not img_alt:
            status['bad'] += 1
        else:
            status['good'] += 1

    return status
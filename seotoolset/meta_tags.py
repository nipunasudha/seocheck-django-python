from pyquery import PyQuery as pq

EMPTY_TAG_CONTENT_TEXT = "<empty>"


def get_meta_tags(url):
    page = pq(url=url, method='get', verify=False)
    return get_meta_tags_from_pq(page)


def get_meta_tags_from_pq(page):
    global EMPTY_TAG_CONTENT_TEXT
    meta_tags = page("meta")
    tags_list = {}
    if not meta_tags:
        print("No meta_tags")
        return tags_list
    empty_name_count = 0
    for tag in meta_tags.items():
        tag_name = tag.attr('name') if tag.attr('name') else tag.attr('property')
        if not tag_name:
            tag_name = "empty-name-" + str(empty_name_count)
            empty_name_count += 1
        tag_content = tag.attr('content')
        tag_content_v = tag_content if tag_content else EMPTY_TAG_CONTENT_TEXT
        tags_list[tag_name] = tag_content_v
    return tags_list


def get_meta_title(meta_tags):
    #More ways to get title TODO
    global EMPTY_TAG_CONTENT_TEXT
    return meta_tags.get('og:title', EMPTY_TAG_CONTENT_TEXT)


def get_meta_description(meta_tags):
    #More ways to get description TODO
    global EMPTY_TAG_CONTENT_TEXT
    return meta_tags.get('og:description', EMPTY_TAG_CONTENT_TEXT)

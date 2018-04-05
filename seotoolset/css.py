from pyquery import PyQuery as pq

from seotoolset import wrap_result

msgCss = {
    'yesCss': 'Your webpage is not using inline CSS styles.',
    'noCss': ['Your webpage is using ', ' inline CSS styles!'],
    'errorCss': 'Error occured while searching inline CSS'
}


def get_css_status(url):
    status = "ok"
    try:
        page = pq(url=url, method='get', verify=False)
        style_tags = page("[style]")
        result = len(style_tags)
        if result:
            status = 'bad'
            message = msgCss['noCss']
        else:
            message = msgCss['yesCss']
    except Exception:
        result = 0
        status = "error"
        message = msgCss['errorCss']

    return wrap_result(result, status, message)

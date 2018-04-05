from reppy.robots import Robots

from seotoolset import wrap_result

MY_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'

msgSitemaps = {
    'yesSitemaps': 'Here are the sitemaps found',
    'noSitemaps': 'No site maps found',
    'errorSitemaps': 'Error occured while searching sitemaps'
}


def get_robot_instance(url):
    txt_location = Robots.robots_url(url)
    return Robots.fetch(txt_location)


def get_sitemap_list(robot_inst):
    status = "ok"
    try:
        result = list(robot_inst.sitemaps)
        message = msgSitemaps['yesSitemaps'] if len(result) else msgSitemaps['noSitemaps']

    except Exception:
        result = []
        status = "error"
        message = msgSitemaps['errorSitemaps']

    return wrap_result(result, status, message)

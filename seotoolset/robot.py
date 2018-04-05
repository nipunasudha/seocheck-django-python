from reppy.robots import Robots

MY_USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'


def get_robot_instance(url):
    txt_location = Robots.robots_url(url)
    return Robots.fetch(txt_location)


def get_sitemap_list(robot_inst):
    return list(robot_inst.sitemaps)

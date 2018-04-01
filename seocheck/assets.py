from django_assets import Bundle, register

js = Bundle('js/app-base.js', filters='jsmin', output='static/packed.js')

register('js_all', js)

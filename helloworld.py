from bottle import route, run, template



@route('/')
def index():
    return template('menu.tpl' )

run(host='0.0.0.0', port=8008)
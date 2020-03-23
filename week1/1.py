from bottle import route, run


@route('/hello')
def index():
    return 'hello world'


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)

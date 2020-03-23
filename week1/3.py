from bottle import route, run, request
import sqlite3


global_data = {}


def create_connection():
    global_data['conn'] = sqlite3.connect(':memory:')
    global_data['conn'].row_factory = sqlite3.Row


def create_table():
    cur = get_cursor()
    sql = '''CREATE TABLE messages (
             msg TEXT NOT NULL)'''
    cur.execute(sql)


def get_cursor():
    return global_data['conn'].cursor()


@route('/show')
def show():
    cur = get_cursor()
    cur.execute('SELECT * FROM messages')

    out = 'Current messages: '
    for i in cur.fetchall():
        out += '<br>{}'.format(i['msg'])

    return out


@route('/add')
def add():
    msg = request.query.get('msg')

    if not msg:
        return 'No message so nothing added.'

    cur = get_cursor()
    params = (msg,)
    cur.execute('INSERT INTO messages (msg) VALUES (?)', params)

    return 'Message added: {}'.format(msg)


if __name__ == '__main__':
    create_connection()
    create_table()
    run(host='0.0.0.0', port=8080)

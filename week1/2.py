"""
Tutorials on sqlite (quickly grabbed off google, there may be better ones):

https://stackabuse.com/a-sqlite-tutorial-with-python/
https://pynative.com/python-sqlite/
"""
import sqlite3


def main():
    print('Connecting')
    conn = sqlite3.connect(':memory:')

    # Configure the connection so we can use the result records as dictionaries.
    conn.row_factory = sqlite3.Row

    # Get a "cursor" for database operations.
    cur = conn.cursor()

    print('Creating table')
    sql = '''CREATE TABLE people (
             id integer PRIMARY KEY,
             first_name text NOT NULL,
             last_name text NOT NULL)'''
    cur.execute(sql)

    print('Selecting all')
    cur.execute('SELECT * FROM people')
    for i in cur.fetchall():
        print(dict(i))

    print('Inserting')
    cur.execute('INSERT INTO people (id, first_name, last_name) VALUES (1, "joe", "aaa")')
    cur.execute('INSERT INTO people (id, first_name, last_name) VALUES (2, "jane", "bbb")')
    cur.execute('INSERT INTO people (id, first_name, last_name) VALUES (3, "marty", "ccc")')

    print('Selecting all')
    cur.execute('SELECT * FROM people')
    for i in cur.fetchall():
        print(dict(i))

    print('Selecting all and printing only specific columns')
    cur.execute('SELECT * FROM people')
    for i in cur.fetchall():
        print('first: {} / last: {}'.format(i['first_name'], i['last_name']))

    print('Selecting id 3')
    cur.execute('SELECT first_name, last_name FROM people WHERE id = 3')
    result = cur.fetchone()
    if result:
        print(dict(result))
    else:
        print('No record found')

    print('Deleting id 3')
    cur.execute('DELETE FROM people WHERE id = 3')

    print('Selecting id 3')
    cur.execute('SELECT first_name, last_name FROM people WHERE id = 3')
    result = cur.fetchone()
    if result:
        print(dict(result))
    else:
        print('No record found')


if __name__ == '__main__':
    main()

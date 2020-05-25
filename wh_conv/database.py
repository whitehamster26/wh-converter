import sqlite3


def init():
    sql = ['''CREATE TABLE IF NOT EXISTS storage
             (id integer primary key,
              pair text,
              last_update integer);''']
    for query in sql:
        push(query)


def db_query(query_type, sql_statement, args=None):
    if sqlite3.complete_statement(sql_statement):
        try:
            conn = sqlite3.connect('wh_conv/database.db')
            c = conn.cursor()
            c.execute(sql_statement) if not args else c.execute(sql_statement,
                                                                args)
        except sqlite3.DatabaseError as e:
            print(f'Database error occured {e}')
            return e
        else:
            if query_type == 'get':
                result = c.fetchall()
            elif query_type == 'push':
                conn.commit()
                result = True
            conn.close()
            return result


def get(sql_statement, *args):
    return db_query('get', sql_statement, args) if args else \
        db_query('get', sql_statement)


def push(sql_statement, *args):
    return db_query('push', sql_statement, args) if args else \
        db_query('push', sql_statement)

import psycopg2


def connect_to_db(db_name, passwd):
    try:
        # setup connection string
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(db_name, passwd)
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

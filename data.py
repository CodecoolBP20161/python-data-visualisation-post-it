import psycopg2


def get_data_from_db(db_name, passwd, option='1'):
    try:
        # setup connection string
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(db_name, passwd)
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()

        if option == '1':
            # run a SELECT statement
            cursor.execute("""SELECT company_name, name, main_color FROM project;""")

        # Fetch and print the result of the last execution
        rows = cursor.fetchall()
        print(rows)
        return rows
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

get_data_from_db('krs', '#3porcI.', '1')
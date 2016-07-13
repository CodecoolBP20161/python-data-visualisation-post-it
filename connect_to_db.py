import psycopg2


def get_pwd():
    try:
        file = open('.secret.txt')
    except Exception as e:
        print("In order to access your database")
        print("first run the following command in your project directory")
        print("substituting the text in quotes with your own details:")
        print('echo "name_of_your_database_or_role, your_password" > .secret.txt')
        print("Then try to run main.py again.")
        print(e)
    else:
        db_password = file.readline().strip().split(',')
        file.close()
        return db_password


def make_connection():
    db_password = get_pwd()
    try:
        # setup connection string
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(db_password[0], db_password[1])
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


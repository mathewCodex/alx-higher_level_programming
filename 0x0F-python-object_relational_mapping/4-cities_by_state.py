#!/usr/bin/python3

"""
Lists all cities from the DataBase hbtn***
taking three args
"""
if __name__ = '__main__':
    from sys import argv
    import MySQLdb as mysql

    if (len(argv) != 4):
        print('Use: username, password, DB name')
        exit(1)

    try:
        connDB = mysql.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])

    except Exception:
        print('Failed to connect to DB')
        exit(0)

    cur = connDB.cursor()

    cur.execute("""SELECT c.id, c.name, s.name FROM cities as c
                    INNER JOIN states as s
                    ON c.states_id = s.id
                    ORDER BY c.id ASC;""")

    query_res = cursor.fetchall()

    for row in query_res:
        print(row)

    cursor.close()
    connDB.close()

#!/usr/bin/python3

"""
Takes in the name of all sattes as args 
and list all fron the db
"""

if __name__ = '__main__':
    from sys import argv
    import MySQLdb as mysql

    import re

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    state_name = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', state_name) is None):
        print('Enter a valid name state (example: California)')
        exit(1)

    try:
        connDB = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = connDB.cursor()

    cuantity = cursor.execute("""SELECT c.name FROM cities as c
                      INNER JOIN states as s
                      ON c.state_id = s.id
                      WHERE s.name = '{:s}'
                      ORDER BY c.id ASC;""".format(state_name))

    result_query = cursor.fetchall()

    final = []

    for i in range(cuantity):
        final.append(result_query[i][0])

    print(', '.join(final))

    cursor.close()
    conndb.close()

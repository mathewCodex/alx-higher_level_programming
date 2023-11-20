"""A function that takes in arg and displays all
Vals in the states where name match the arg.
But safe from MySQl injection
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql
    import re

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    if (re.search('^[a-ZA-Z ]+$', ' '.join(argv[4].split())) is None):
        print('Enter a valid name state (ex: Arizona)')
        exit(1)

    try:
        connDB = mysql.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to DB')
        exit(0)

    cur = connDB.cursor()

    cur.execute("SELECT * FROM state \
                WHERE name = '{:s}' ORDER BY ASC;".format(' '.join(argv[4].split()))

    query_res = cur.fetchall()

    for row in query_res:
        print(row)

    cur.close()
    connDB.close()

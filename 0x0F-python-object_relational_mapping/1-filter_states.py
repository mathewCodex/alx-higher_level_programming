#!/usr/bin/python3
"""
Lists of all states with name starting
with N (upper N) from the DB hbtn---
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        connDB = mysql.connect(host='localhost', port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3])

    except Exception:
        print('Failed to connect to Database')
        exit(0)

    cursor = connDB.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE 'N%' ORDER BY id ASC;")

    query_res = cursor.fetchall()

    for row in query_res:
        print(row)

    cursor.close()
    connDB.close()

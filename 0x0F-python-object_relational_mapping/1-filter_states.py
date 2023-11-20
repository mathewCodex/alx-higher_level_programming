#!/usr/bin/python3

"""
List all states with name starting with
N from the db hbtn_0e_0_usa
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        conndb = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = conndb.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    conndb.close()

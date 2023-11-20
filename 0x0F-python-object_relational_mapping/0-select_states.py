#!/usr/bin/python3
"""List all states from the DB hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MYSQLdb as mysql

    try:
        conndb = mysql.connect(host='localhost', port=3306, user=argv[1],
                passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to DB')
        exit(0)

    cursor = conndb.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
#!/usr/bin/python3
"""
Takes in argument and present all vals in the
states tab where name matches inputs
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        connDB = MySQLdb.connect(host='localhost',port=3306,user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    except Exception:
        print('Failed to connect to the Database')

    cur = connDB.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' \
                ORDER BY id ASC;".format(argv[4]))

    query_res = cur.fetchall()

    for row in query_res:
        print(row)

    cur.close()
    connDB.close()

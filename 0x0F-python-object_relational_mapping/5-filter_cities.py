#!/usr/bin/python3

"""
Takes in the name of all sattes as args 
and list all fron the db
"""

if __name__ == '__main__':
    import MySQLdb as mysql
    from sys import argv

    connDB = mysql.connect(host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")
    cur = connDB.cursor()
    cur.execute(
            "SELECT cities.name FROM cities JOIN states ON \
                    cities.state_id = states.id WHERE states.name = %s",
                    (sys.argv[4]))
    row_query = cur.fetchall()
    all_lists = []
    for row in row_query:
        all_list.append(",".join(str(x) for x in row))
    print(all_lists, sep=", ")
    cur.close()
    connDB.close()

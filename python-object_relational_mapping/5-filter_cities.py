#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def filter_cities_by_state(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    sql_query = "SELECT name FROM cities JOIN states ON cities.state_id = \
        states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(sql_query, (state_name,))
    cities = cursor.fetchall()

    if cities:
        for city in cities:
            print(city[0])
    else:
        print("")

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities_by_state(username, password, database, state_name)

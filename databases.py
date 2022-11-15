import sqlite3 as sql

def execute_query():
    with sql.connect('data.db') as conn:
        c = conn.cursor()
        with open('query.sql', 'r') as f:
            query = f.read()
        result = c.execute(query).fetchall()
        c.close()
        conn.commit()

    return result


########## EXTREME ##########
# Topics: SQL / Databases, Data Science #

# The variable users is required to have that name for the challenge checker !! DO NOT CHANGE !!


# INFORMATION:
# Write queries in the query.sql file and run execute_query() defined above to get the result
# returned in python format so rows are returned as tuples e.g. ('bob', 'smith', 21)
# and can be processed in this file

# THE CHALLENGE - get the username and first name of users with age greater than 27 in ascending order by age and store it in the users array
# FIELDS: id, username, first_name, last_name, age TABLE: users

users: list = execute_query()
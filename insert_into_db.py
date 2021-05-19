from numpy import insert
import psycopg2
from config import config


def insert_property(property):
    print(".")
    sql = 'INSERT INTO property(valuer_general_id, address, suburb, postcode, saleprice, saledate) VALUES(%s, %s, %s, %s, %s, %s)'
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, property)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

'''
insert propert instead: insert property as you read each line
'''

if __name__ == '__main__':
    insert_property()
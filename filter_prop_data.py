# FITLERING ONE .DAT FILE FROM THE FOLDER HOLDING PROPERTY DATA FOR THE WEEK.

import psycopg2
from config import config

def insert_property_list(property_lists):
    print(property_lists)
    sql = 'INSERT INTO property(valuer_general_id, address, saleprice) VALUES(%s, %s, %s)'
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, property_lists)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

value_lists=[] 
with open('property_values/20210412/001_SALES_DATA_NNME_12042021.DAT',"r") as df:
    lines= df.read().split("\n")
    for line in lines[:-1]:
        if line[0] =="B":
            lineSplit = line.split(";")
            property_id = lineSplit[2]
            property_address = " ".join(lineSplit[5:11]).strip()
            #sale_price = lineSplit[15]
            sale_price = lineSplit[15]
            value_list = [property_id, property_address, sale_price]
            # value_lists.append(value_list)
            # value_lists.append(sale_price)
            value_lists.append(value_list)

#print(", ".join(value_lists))

insert_property_list(value_lists)


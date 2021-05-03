import os
import pandas as pd
import psycopg2
from config import config

def insert_property_list(property_lists):
    print(property_lists)
    sql = 'INSERT INTO property(valuer_general_id, address, suburb, postcode, saleprice) VALUES(%s, %s, %s, %s, %s)'
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


directory = '/Users/MichaelHu/Documents/Internship/property_values/20210412'

value_lists=[]

# for filename in os.listdir(directory):
#     if filename.endswith(".DAT"):

def loop_function(filename):
    f = open(filename)
    lines = f.read().split("\n")
    for line in lines[:-1]:
        if line[0] =="B":
            lineSplit = line.split(";")
            property_id = lineSplit[2]
            property_address = " ".join(lineSplit[5:9]).strip()
            property_suburb = lineSplit[9]
            property_postcode = lineSplit[10]
            sale_price = lineSplit[15]
            value_list = [property_id, property_address, property_suburb, property_postcode, sale_price]
            value_lists.append(value_list)

def loop_directory(directory: str):
    '''Loop files in the directory'''

    for filename in os.listdir(directory):
        if filename.endswith(".DAT"):
            file_directory = os.path.join(directory, filename)
            print(file_directory)
            loop_function(file_directory)

if __name__=='__main__':
    loop_directory(directory)

df = pd.DataFrame(value_lists)
print(df.head)

insert_property_list(value_lists)
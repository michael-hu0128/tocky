import psycopg2
from config import config

def create_tables():
    commands = [
        """
        CREATE TABLE property (
            property_id SERIAL PRIMARY KEY,
            valuer_general_id INTEGER NOT NULL,
            address VARCHAR(255) NOT NULL,
            suburb VARCHAR(255) NOT NULL,
            postcode INTEGER NOT NULL,
            saleprice INTEGER NOT NULL
        )
        """]

    conn = None
    try:
        # print(commands)
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
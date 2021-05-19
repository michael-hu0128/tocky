from datetime import datetime
from insert_into_db import insert_property


'''
Going through all .dat files with the 'current' format, splitting and selecting variables
that are relevant to the task. Once the variables are selected, 'insert_property_values'
function will be called so that each property line will be inserted as it is being read,
instead of storing it in to a list. Saves memory and time.

if else none statements are used in lineSplits to ensure that tuples with empty values
can still be inserted into the pg database without failing.
'''


def store_dat_current(file_path):
    value_list = []
    with open(file_path, "r") as df:
        lines = df.read().split("\n")

        for line in lines[:-1]:
            if line.strip() != '' and line[0] == "B":
                line.replace('\\', '/')
                lineSplit = line.split(";")
                property_id = lineSplit[2] if lineSplit[2] else None
                property_address = " ".join(lineSplit[5:9]).strip()
                suburb = lineSplit[9] if lineSplit[9] else None
                postcode = lineSplit[10] if lineSplit[10] else None
                sale_price = lineSplit[15] if lineSplit[15] else None
                sale_date = lineSplit[13] if lineSplit[13] else None
                record = [property_id, property_address,
                          suburb, postcode, sale_price, sale_date]
                value_list.append(record)
        
        insert_property(value_list)


# Same as above, but for .dat files that are in the 'archive' format
def store_dat_archive(file_path):
    value_list = []
    errors = []
    with open(file_path, 'r') as df:
        lines = df.read().split('\n')
        
        for line in lines[:-1]:
            if line[0] == 'B':
                lineSplit = line.split(';')
                property_id = lineSplit[4] if lineSplit[4] else None
                property_address = ' '.join(lineSplit[5:8]).strip()
                suburb = lineSplit[8] if lineSplit[8] else None
                postcode = lineSplit[9] if lineSplit[9] else None
                sale_price = lineSplit[11] if lineSplit[11] else None
                
                sale_date = None
                if lineSplit[10]:
                    date_object = datetime.strptime(lineSplit[10], '%d/%m/%Y')
                    sale_date = date_object.strftime('%Y/%m/%d')
                
                record = [property_id, property_address, suburb, postcode, sale_price, sale_date]
                value_list.append(record)
        
        insert_property(value_list) 


if __name__ == '__main__':
    # store_dat_current(file_path)
    store_dat_archive()
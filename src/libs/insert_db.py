from pg_handler import *
import csv

if __name__=="__main__":
    p = Handler(dbname="postgres", host="localhost", user="postgres", password="*****")
    books = r"C:\Users\Ja\Desktop\IT\PYTHON KURZ\Projects\SDA-Python_interm\Project_library\task\data.csv"

    lib_data=[]

    with open(books, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lib_data.append(row)

    for dic in lib_data:
        p.inserting_db_info('books', dic)
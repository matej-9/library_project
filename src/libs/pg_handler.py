import psycopg2
import psycopg2.extras
from psycopg2 import sql

class Handler:
    def __init__(self,dbname, user, host, password, debug = False):
        self.dbname=dbname
        self.user=user
        self.host=host
        self.password=password
        self.connection = None
        self.debug = debug

    def connect(self):
        self.connection = psycopg2.connect(
           dbname = self.dbname,
           host = self.host,
           user = self.user,
           password=self.password 
        )
        if self.debug:
            print("Connected!")

    def inserting_db_info(self,table_name, dict,):     #dokoncit funkcie na vkladanie, ukazovanie z DB + conection funkcia + cursor funkciu?
        if not self.connection:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                inserting = sql.SQL(
                    """
                    INSERT INTO {} ({})
                    VALUES({})
                    RETURNING *;
                    """
                ).format(
                sql.Identifier(table_name),
                sql.SQL(',').join(map(sql.Identifier,dict.keys())),
                sql.SQL(',').join(map(sql.Literal,dict.values()))
                )
                cur.execute(inserting)
                inserted = cur.fetchone()
            except Exception as e:
                print(f"Error during inserting {e}")
        # self.connection.close()
        return inserted

    def getting_all_db_info(self, table_name, column_name = "*"):
        if not self.connection:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                getting_db_data=sql.SQL(
                    """
                    SELECT {}
                    FROM {};
                    """
                ).format(
                sql.SQL(column_name),
                sql.Identifier(table_name)
                )
                cur.execute(getting_db_data)
                viewed = cur.fetchall()
            except Exception as e:
                print(f"Error during info request {e}")
        # self.connection.close()
        return print(viewed)
    
    def getting_db_info(self, table_name, btype = None, book_type = None):
        if not self.connection:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                getting_db_data=sql.SQL(
                    """
                    SELECT *
                    FROM {}
                    WHERE {} = {};
                    """
                ).format(
                sql.Identifier(table_name),
                sql.SQL(btype),
                sql.Literal(book_type)
                )
                cur.execute(getting_db_data)
                viewed = cur.fetchall()
            except Exception as e:
                print(f"Error during info request {e}")
        # self.connection.close()
        return viewed
    
    def inserting_db_book(self,table_name, column_name, column_name_1, book_id, id2):     #dokoncit funkcie na vkladanie, ukazovanie z DB + conection funkcia + cursor funkciu?
        if not self.connection:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                inserting_book = sql.SQL(
                    """
                    UPDATE {}
                    SET {} = {}
                    wHERE {} = {};
                    """
                ).format(
                sql.Identifier(table_name),
                sql.Identifier(column_name),
                sql.SQL(column_name_1),
                sql.Identifier(book_id),
                sql.Literal(id2)
                )
                cur.execute(inserting_book)
                inserted = cur.rowcount
            except Exception as e:
                print(f"Error during inserting {e}")
        # self.connection.close()
        return inserted
    

    def withdraw_from_db(self, table_name, column_name, quantity, book_id, id1, book_type, btype):
        if not self.connection:
            self.connect()
        with self.connection, self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                withdrawing = sql.SQL(
                    """
                    UPDATE {}
                    SET {} = {}
                    WHERE {} = {} AND {} = {};
                    """
                ).format(
                sql.Identifier(table_name),
                sql.Identifier(column_name),
                sql.SQL (quantity),
                sql.Identifier (book_id),
                sql.Literal (id1),
                sql.Identifier (book_type),
                sql.Literal (btype)
                )
                cur.execute(withdrawing)
            except Exception as e:
                print(f"Error during withdrawal!{e}")
            # self.connection.close()
            return None


    
# if __name__ == "__main__":
#     p = Handler(dbname="postgres", host="localhost", user="postgres", password="****")
    # p.connect()
    # p.inserting_db_info('users', {'name' : 'Matej','surname':'Babiak'})
    # p.getting_all_db_info('books')
    # p.withdraw_from_db('books', 'copies_available', 'copies_available -1','book_id', '2', 'type', 'Audiobook')
import os
import pg_handler
import csv
from abc import ABC, abstractmethod

# db_handler = pg_handler.Handler(dbname="postgres", host="localhost", user="postgres", password="klokanisko1")

TABLE_BOOKS = 'books'
TABLE_USERS = 'users'

class Library:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        

    def showing_books(self):
        all_books = self.db_handler.getting_all_db_info(TABLE_BOOKS)
        return all_books

    def show_book(self,types,book_type):
        book = self.db_handler.getting_db_info(TABLE_BOOKS, types, book_type)        
        return book

    def insert_book(self,book_list):   
        quant = 'copies_available'
        changed_quant = 'copies_available+1'
        id1 = 'book_id'
        id2 = book_list[0][0]
        book_insert = self.db_handler.inserting_db_book(TABLE_BOOKS, quant, changed_quant,id1,id2)
        return book_insert
    
    def withdraw_book(self, book_list):
        quant = 'copies_available'
        changed_quant = 'copies_available-1'
        id1 = 'book_id'
        id2 = book_list[0][0]
        book_type = 'type'
        btype = book_list[0][3]
        book_withdraw = self.db_handler.withdraw_from_db(TABLE_BOOKS, quant, changed_quant,id1,id2, book_type, btype)
        return book_withdraw
        
    def show_all_users(self):
        all_users = self.db_handler.getting_all_db_info(TABLE_USERS)
        return all_users
    
    def show_user(self,column,types,book_type):
        one_user = self.db_handler.getting_db_info(TABLE_USERS,column, types, book_type)        
        return one_user

    def insert_user(self, user_dict):
        insert_user = self.db_handler.inserting_db_info(TABLE_USERS, user_dict)
        return insert_user
    
    def withdraw_users_book(self,user_list):
        book_name_user = user_list[0][4]
        book_type_user = user_list[0][5]
        withdraw_user_book = self.db_handler.withdraw_from_db(TABLE_USERS,'quantity', 'quantity -1', 'book_name', book_name_user, 'book_type', book_type_user)
        return withdraw_user_book
    

# lib = Library(db_handler)
# lib.showing_books()
# users_book=list(lib.show_book('*','book_id', 2))
# print(users_book)
# lib.withdraw_book(users_book)

# one_user = list(lib.show_user('*', 'name', 'Jan'))
# print(one_user)
# lib.insert_user({'name': 'Jan', 'surname':'Skuska', 'book_id': 2, 'book_name': 'Hobit', 'book_type':'Audiobook', 'quantity': 1})
# lib.show_all_users()

# lib.withdraw_users_book(one_user)
## vytvorit class Book a User a definovat metódy na vyberanie a vracanie knih

# if db quantity > 0 -> withdrawdb
# when inserting match id of book / or name with book quantity and pass argument quantity +1 to pg_handler inserting quantity
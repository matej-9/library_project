import os
from library_system import Library
from pg_handler import Handler

handler = Handler(dbname="postgres", host="localhost", user="postgres", password="****")
system = Library(handler)



def starting_lb():
    print("***WELCOME TO LIBRARY SYSTEM***")
    print()
    user_input1 = input("""
                        ***WHAT IS YOUR REQUEST?***
                        PRESS [0] TO SHOW ALL BOOKS IN LIBRARY
                        PRESS [1] TO SHOW SPECIFIC BOOK
                        PRESS [2] TO REGISTER USER
                        PRESS [3] TO SHOW USERS AND BORROWED BOOKS
                        PRESS [4] TO INSERT BOOK
                        PRESS [5] TO WITHDRAW BOOK
                        PRESS [e] TO EXIT 
                        """)
    return user_input1

def show_library():
    user_input = starting_lb()
    if user_input == 'e':
        print("Good Bye!")
    elif user_input == '0':
        system.showing_books()
    elif user_input == '1':
        system.showing_books()
        choosing_title = input("Which book you want to see? : Please select books id :")
        # choosing_type = input("press [1] for Hardcover or press [2] for Audiobook")
        # if choosing_type == 1:
        #     choosing_type = 'Hardcover'
        # elif choosing_type == 2:
        #     choosing_type = 'Audiobook'
        return print(list(system.show_book('book_id', choosing_title)))

show_library()
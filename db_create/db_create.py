import psycopg2
from psycopg2 import sql


if __name__=="__main__":
    conn = psycopg2.connect(
        "dbname=postgres user=postgres host=localhost password=**** port=5432" 
    )
    print("**CONNECTED**")

    with conn, conn.cursor() as cur:
        create_table_books=sql.SQL(
            """
            DROP TABLE IF EXISTS books;
            CREATE TABLE books(
                book_id SERIAL PRIMARY KEY,
                title VARCHAR(256),
                author VARCHAR(256),
                type VARCHAR(256),
                publication_year INT,
                genre VARCHAR(256),
                isbn VARCHAR(256),
                copies_available INT
            );
            """
        )
        cur.execute(create_table_books)
        print("**TABLE BOOKS CREATED**")

        create_table_users=sql.SQL(
            """
            DROP TABLE IF EXISTS users;
            CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(256),
                surname VARCHAR(256),
                book_id INT,
                book_name VARCHAR(256),
                book_type VARCHAR(256),
                quantity INT
            );
            """
        )
        cur.execute(create_table_users)
        print("**TABLE USERS CREATED**")

        create_users_books=sql.SQL(
            """
            DROP TABLE IF EXISTS user_books;

            CREATE TABLE user_books(
                book_id INT NOT NULL,
                user_id INT NOT NULL,
                CONSTRAINT "PK_user_books" PRIMARY KEY (book_id, user_id)
            );
            """ 
        )
        cur.execute(create_users_books)
        print("**TABLE USER_BOOKS CREATED**")
    conn.close()
    
        
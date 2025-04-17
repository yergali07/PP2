import psycopg2
from config import load_config


def insert_phonebook(name, phone):
    """ Insert a new phonebook entry into the phonebook table """

    sql = """INSERT INTO phonebook(name, phone)
             VALUES(%s, %s) RETURNING id;"""
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))

                rows = cur.fetchone()
                if rows:
                    id = rows[0]
                    
                conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return id

if __name__ == '__main__':
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    insert_phonebook(name, phone)
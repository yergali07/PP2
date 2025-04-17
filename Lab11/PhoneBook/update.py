import psycopg2
from config import load_config


def update_phonebook(id, name):
    """ Update a phonebook entry in the phonebook table """

    update_row_count = 0

    sql = """UPDATE phonebook
             SET name = %s
             WHERE id = %s;"""

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, id))
                update_row_count = cur.rowcount
                
            conn.commit()

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return update_row_count

if __name__ == '__main__':
    id = input("Enter id: ")
    name = input("Enter new name: ")
    update_phonebook(id, name)
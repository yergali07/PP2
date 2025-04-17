import psycopg2
from config import load_config

def insert_or_update_user(name, phone):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL insert_or_update_user(%s, %s);', (name, phone))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    insert_or_update_user(name, phone)
    print(f"User {name} with phone {phone} inserted/updated successfully.")
import psycopg2
from config import load_config

def insert_or_update_user(names, phones):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL insert_many_users(%s, %s, %s);', (names, phones, None))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    names = input("Enter the names (comma-separated): ").split(',')
    phones = input("Enter the phones (comma-separated): ").split(',')
    
    if len(names) != len(phones):
        print("The number of names and phones must be the same.")
    else:
        insert_or_update_user(names, phones)
        print(f"Users {names} with phones {phones} inserted/updated successfully.")
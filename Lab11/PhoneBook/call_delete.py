import psycopg2
from config import load_config

def delete_by_name_or_phone(value):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL delete_by_name_or_phone(%s);', (value,))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    value = input("Enter the name or phone number to delete: ")
    delete_by_name_or_phone(value)
    print(f"Deleted user with name or phone {value} successfully.")
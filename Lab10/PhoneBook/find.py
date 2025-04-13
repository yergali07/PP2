import psycopg2
from config import load_config

def find_by_phone_or_name(phone=None, name=None):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if phone:
                    cur.execute("SELECT * FROM phonebook WHERE phone = %s;", (phone,))
                elif name:
                    cur.execute("SELECT * FROM phonebook WHERE name = %s;", (name,))
                else:
                    print("Please provide a phone or name.")
                    return

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    phone = input("Enter phone number to search (or leave blank): ")
    name = input("Enter name to search (or leave blank): ")

    if not phone and not name:
        print("Please provide a phone or name.")
    else:
        find_by_phone_or_name(phone, name)

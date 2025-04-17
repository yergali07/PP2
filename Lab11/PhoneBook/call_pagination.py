import psycopg2
from config import load_config


def get_phonebook_paginated(limit, offset):
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()
                cur.callproc('get_phonebook_paginated', (limit, offset))

                rows = cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows

if __name__ == '__main__':
    limit = int(input("Enter the number of records to fetch: "))
    offset = int(input("Enter the offset: "))
    results = get_phonebook_paginated(limit, offset)
    if results:
        print("Records found:")
        for result in results:
            print(result)
    else:
        print("No records found.")
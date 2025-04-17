import psycopg2
from config import load_config


def search_pattern(pattern):
    matches = []
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur = conn.cursor()
                cur.callproc('search_phonebook', (pattern,))

                row = cur.fetchone()
                while row is not None:
                    matches.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return matches

if __name__ == '__main__':
    pattern = input("Enter the pattern to search: ")
    results = search_pattern(pattern)
    if results:
        print("Matches found:")
        for result in results:
            print(result)
    else:
        print("No matches found.")
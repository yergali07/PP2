import csv
import psycopg2
from config import load_config

def import_from_csv(file_path):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(file_path, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        cur.execute(
                            "INSERT INTO phonebook (name, phone) VALUES (%s, %s);",
                            (row['name'], row['phone'])
                        )
                print("CSV data imported successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    file_path = input("Enter the path to the CSV file: ")
    import_from_csv(file_path)

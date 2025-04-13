import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = [
        """
        CREATE TABLE phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
        );
        """
    ]
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
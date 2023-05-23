import psycopg2
from sqlite_example import connect_to_db, execute_q
from queries import GET_CHARACTERS, CREATE_IAN, CREATE_TEST_TABLE, DROP_CHARACTER_TABLE, CREATE_CHARACTER_TABLE, INSERT_TEST_TABLE, DROP_TEST_TABLE

DBNAME = 'jmdkbuww'
USER = 'jmdkbuww'
PASSWORD = 'FEQi2iE4icjrZLIWmtbhLvmKmltrB_En'
HOST = 'drona.db.elephantsql.com'

def connect_to_pg(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def modify_db(conn, curs, query):
    curs.execute(query)
    conn.commit()

if __name__ == "__main__":
    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, GET_CHARACTERS)

    # Create destination table within PostgreSQL DB
    pg_conn, pg_curs = connect_to_pg()
    # modify_db(pg_conn, pg_curs, DROP_CHARACTER_TABLE)
    modify_db(pg_conn, pg_curs, CREATE_CHARACTER_TABLE)

    # Loop over characters and insert into PostgreSQL w/ correct values
    for character in sl_characters:
        modify_db(pg_conn, pg_curs, 
            f'''
            INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom", 
            VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]});
            '''
        )


import sqlite3


def get_random_row_from_sqlite(table_name, columns="*"):
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = f"SELECT {columns} FROM [{table_name}] ORDER BY RANDOM() LIMIT 1"
        cursor.execute(query)
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_all_const(table_name):
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM [{table_name}]"
        print(query)
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка SQLite: {e}")
        return None
    finally:
        if conn:
            conn.close()
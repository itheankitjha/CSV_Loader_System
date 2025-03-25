import psycopg2


def load_data(data, db_config):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INT PRIMARY KEY, 
                      name VARCHAR(100), 
                      age INT, 
                      city VARCHAR(100));''')

    for row in data:
        cursor.execute("INSERT INTO users (id, name, age, city) VALUES (%s, %s, %s, %s)",
                       (row['id'], row['name'], row['age'], row['city']))

    conn.commit()
    cursor.close()
    conn.close()

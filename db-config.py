#remember to install psycopg2
import psycopg2
host="localhost"
database="ticktack"
user="postgres"
password="password"
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

#open cursor to perform db operations
cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS events(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50),
    from_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    to_time TIMESTAMP WITH TIME ZONE,
    priority INTEGER DEFAULT 0
);
""")
cur.execute(""" CREATE TABLE IF NOT EXISTS timers(
    id SERIAL PRIMARY KEY,
    from_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    to_time TIMESTAMP WITH TIME ZONE
);
""")

# some first record into our table that can be used to test
# cur.execute("INSERT INTO events(name, description,from_time, to_time) VALUES('presentation','I will have a one-to-one presentation',TO_TIMESTAMP('2024 04 11 11:45','YY MM DD HH:MI'),TO_TIMESTAMP('2024 04 11 12:45','YY MM DD HH:MI'))")
# cur.execute("INSERT INTO events(name, description, from_time, to_time) VALUES('meeting','I will have a meeting with my team',TO_TIMESTAMP('2024 04 11 10:00','YY MM DD HH:MI'),TO_TIMESTAMP('2024 04 11 11:30','YY MM DD HH:MI'))")


#make changes to the database persistent
conn.commit()

# close cursor and disconnect from database
cur.close()
conn.close()

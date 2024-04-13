#remember to install psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="ticktack",
    user="postgress",
    password="your_password"
)

#open cursor to perform db operations
cur = conn.cursor()
cur.execute(""" CREATE TABLE events(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(50),
    from TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    to TIMESTAMP WITH TIME ZONE,
    priority INTEGER DEFAULT 0
);
""")

# some first record into our table that can be used to test
cur.execute('INSERT INTO events(name, description, from, to) VALUES("presentation","I will have a one-to-one presentation",TO_TIMESTAMP('2024 04 11 11:45','YY MM DD HH:MI'),TO_TIMESTAMP('2024 04 11 12:45','YY MM DD HH:MI'))');
cur.execute('INSERT INTO events(name, from, to) VALUES("class",TO_TIMESTAMP('2024 05 11 11:45','YY MM DD HH:MI'),TO_TIMESTAMP('2024 05 11 12:45','YY MM DD HH:MI'))');
cur.execute('INSERT INTO events(name, description, from, to) VALUES("meeting","I will have a meeting with my team",TO_TIMESTAMP('2024 04 11 10:00','YY MM DD HH:MI'),TO_TIMESTAMP('2024 04 11 11:30','YY MM DD HH:MI'))');

#make changes to the database persistent
conn.commit()

# close cursor and disconnect from database
cur.close()
conn.close()

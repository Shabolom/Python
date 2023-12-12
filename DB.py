import sql
import logging as log
log.basicConfig(level=log.DEBUG)
sql.db = sql.Db('dbname=postgres user=postgres password=1234 host=127.0.0.1 port=5432')
sql.Table.schema = 'demo'

sql.query('DROP SCHEMA IF EXISTS demo CASCADE')
sql.query('CREATE SCHEMA IF NOT EXISTS demo')

sql.query("""
    CREATE TABLE IF NOT EXISTS demo.groups (
        id SMALLSERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(32)
    )""")

sql.query("""
CREATE TABLE IF NOT EXISTS demo.users (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    username VARCHAR(64) NOT NULL,
    fullname VARCHAR(64) NOT NULL,
    password CHAR(32) NOT NULL,
    status VARCHAR(8) NOT NULL,
    group_id SMALLINT REFERENCES demo.groups(id),
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()
)""")

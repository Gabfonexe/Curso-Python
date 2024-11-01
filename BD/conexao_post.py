import psycopg2

conn = psycopg2.connect(
  database = 'db_games',
  use = 'postgres',
  password = '123456',
  host = 'localhost',
  port = '5432'
)

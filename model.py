import sql

class Users(sql.Table):
    db = sql.Db('host=198.168.0.1 dbname=core')
    schema = 'site'
    name = 'users'
    fields = {}

class Transactions(sql.Table):
    db = sql.Db('host=198.168.0.2 dbname=reporting')
    schema = 'financial'
    name = 'transaction'
    fields = {}
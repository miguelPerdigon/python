from utils.postgress import Postgress

host = 'localhost'
user = 'user_name'
db_name = 'db_name'
password = '***********'

db_postgress = Postgress(host, user, db_name, password)

query = """select * from table_name where field_a = 'abc'"""
result = db_postgress.do_query(query)
db_postgress.close_conn()

for row in result:
    print(row)

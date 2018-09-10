import sqlalchemy
import random

def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('Gene', 'Gene', 'MyCompany')

"""
results = meta.tables['Product']

for row in con.execute(results.select()):
    print(row)
"""
loop_counter = 0

products = meta.tables['product']

#clause = slams.insert().values(name='Wimbledon', country='United Kingdom')

while loop_counter < 50000:
    pt_key = random.randint(1, 5)
    clause = products.insert().values(name='Product_' + str(loop_counter), description='Product_' + str(loop_counter) + ' decription', active=True, deleted=False, product_type_id=pt_key)
    con.execute(clause)
    loop_counter += 1




"""

for table in meta.tables:
    print (table)"""


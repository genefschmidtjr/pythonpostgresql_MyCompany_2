import sqlalchemy
import random


def main():
    seed_data()


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


def seed_data():
    con, meta = connect('Gene', 'Gene', 'MyCompany')

    loop_counter = 0

    products = meta.tables['product']

    while loop_counter < 50000:
        pt_key = random.randint(1, 5)
        clause = products.insert().values(name='Product_' + str(loop_counter), description='Product_' + str(loop_counter) + ' decription', active=True, deleted=False, product_type_id=pt_key)
        con.execute(clause)
        loop_counter += 1

    return


if __name__ == '__main__':
    main()


import sqlalchemy
from sqlalchemy import text


def main():
    process_dimension()
    return


# generic connection
def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta


def flatten_source():
    sourcecon, sourcemeta = connect('Gene', 'Gene', 'MyCompany')

    sql = text('select 			p.id as application_product_id, \
				                pt.id as application_product_type_id, \
				                pt.name as product_type_name, \
				                pt.description as product_type_description, \
				                p.name as product_name, \
				                p.description as product_description \
                from			product p inner join product_type pt on p.product_type_id = pt.id')

    staging_dim_product = sourcecon.engine.execute(sql)

    return staging_dim_product


def process_dimension():
    destcon, destmeta = connect('Gene', 'Gene', 'MyCompanyWarehouse')

    dimproduct = destmeta.tables['dim_product']

    truncateclause = text('TRUNCATE TABLE dim_product')

    destcon.engine.execute(truncateclause)

    source = flatten_source()

    blankinsert = dimproduct.insert().values(application_product_id=0,
                                    application_product_type_id=0,
                                    product_description='not found',
                                    product_name='not found',
                                    product_type_description='not found',
                                    product_type_name='not found')
    destcon.engine.execute(blankinsert)

    for row in source:
        clause = dimproduct.insert().values(application_product_id=row.application_product_id,
                                            application_product_type_id=row.application_product_type_id,
                                            product_description=row.product_description,
                                            product_name=row.product_name,
                                            product_type_description=row.product_type_description,
                                            product_type_name=row.product_type_name)

        destcon.execute(clause)

    return


if __name__ == "__main__":
    main()


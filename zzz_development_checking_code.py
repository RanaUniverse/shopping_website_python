from faker import Faker

from database_code.db_make import create_db_and_engine, engine

from database_code.db_functions import create_one_new_category, create_one_new_product


fake = Faker()


if __name__ == "__main__":
    create_db_and_engine()

    create_one_new_category(
        db_engine=engine,
        cat_name=fake.name(),
        cat_description=fake.sentence(12),
    )

    create_one_new_product(
        db_engine=engine,
        product_name=fake.first_name(),
        product_description=fake.sentence(25),
        price=fake.random_int(100, 10000),
        quantity=fake.random_int(10, 100),
    )

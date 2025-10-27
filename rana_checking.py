from database_code.db_make import create_db_and_engine, engine

from database_code.db_functions import create_one_new_category, create_one_new_product

if __name__ == "__main__":

    # Make sure DB exists
    create_db_and_engine()

    cat_name = "Toys5 is good 2"
    cat_slug = None
    cat_description = "These are made for children."
    create_one_new_category(
        db_engine=engine,
        cat_name=cat_name,
        cat_slug=cat_slug,
        cat_description=cat_description,
    )

    create_one_new_product(
        db_engine=engine,
        product_name="Rana",
        price=99,
        quantity=3,
        is_available=False,
    )

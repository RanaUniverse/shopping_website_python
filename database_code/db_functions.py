from sqlalchemy import Engine

from sqlmodel import Session, select


from database_code.models_table import CategoryModel, ProductModel


def create_one_new_category(
    db_engine: Engine,
    cat_name: str,
    cat_slug: str | None = None,
    cat_description: str | None = None,
):

    # Below it will insert one new category in a session
    with Session(db_engine) as session:
        if not cat_slug:
            cat_slug = cat_name.strip().lower().replace("-", "_").replace(" ", "_")

        statement = select(CategoryModel).where(
            (CategoryModel.name == cat_name) | (CategoryModel.slug == cat_slug)
        )
        existing_cat = session.exec(statement=statement).first()

        if existing_cat:
            # 🧾 Identify which field caused the conflict (optional but nice UX)
            if existing_cat.name == cat_name and existing_cat.slug == cat_slug:
                print(
                    f"⚠️ Category with name '{cat_name}' and "
                    f"slug '{cat_slug}' already exists."
                )
            elif existing_cat.name == cat_name:
                print(f"⚠️ Category's Name '{cat_name}' already exists.")
            elif existing_cat.slug == cat_slug:
                print(f"⚠️ Category's Slug '{cat_slug}' already exists.")
        else:
            category = CategoryModel(
                name=cat_name,
                description=cat_description,
                slug=cat_slug,
            )
            session.add(category)
            session.commit()
            print(f"✅ Added new category: {category}")


def create_one_new_product(
    db_engine: Engine,
    product_name: str,
    price: float,
    product_description: str | None = None,
    product_slug: str | None = None,
    quantity: int | None = None,
    is_available: bool | None = None,
):
    with Session(db_engine) as session:
        product_obj = ProductModel(
            name=product_name,
            description=product_description,
            slug=product_slug,
            price=price,
            stock_qty=quantity,
            is_available=is_available,
        )
        session.add(product_obj)
        session.commit()
        print(f"✔ Product Has Been added")

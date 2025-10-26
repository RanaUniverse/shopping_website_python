from sqlmodel import (
    SQLModel,
    Field,  # type: ignore
    Relationship,
)


class CategoryPart(SQLModel, table=True):
    __tablename__: str = "category_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    name: str

    products: list["ProductPart"] = Relationship(back_populates="category")


class ProductPart(SQLModel, table=True):
    __tablename__: str = "product_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    description: str | None = Field(default=None)
    name: str
    price: float

    category_id:int|None =Field(default=None, foreign_key="category_data.id_")


    category: CategoryPart = Relationship(back_populates="products")

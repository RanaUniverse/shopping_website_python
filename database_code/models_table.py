from datetime import datetime, timezone

from sqlmodel import (
    SQLModel,
    Field,  # type: ignore
    Relationship,
)


class CategoryPart(SQLModel, table=True):
    __tablename__: str = "category_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    description: str | None = Field(default=None)
    name: str
    # 🌐 Optional slug for URLs (e.g., "toy" for "Toy")
    slug: str | None = Field(default=None, index=True, unique=True)

    # ⏰ Auto timestamps (optional, very useful)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    products: list["ProductPart"] = Relationship(back_populates="category")


class ProductPart(SQLModel, table=True):
    __tablename__: str = "product_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    description: str | None = Field(default=None)
    name: str
    slug: str | None = Field(default=None, unique=True)
    price: float | None = Field(default=None)

    category_id: int | None = Field(default=None, foreign_key="category_data.id_")

    # ⏰ Auto timestamps (optional, very useful)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # 🏪 Stock & availability
    stock_qty: int | None = Field(default=None, ge=0)
    is_available: bool | None = Field(default=None)

    category: CategoryPart = Relationship(back_populates="products")

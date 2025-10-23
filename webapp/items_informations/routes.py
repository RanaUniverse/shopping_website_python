from flask import Blueprint, render_template


items_bp = Blueprint(
    name="item_info",
    import_name=__name__,
    template_folder="templates",
)

items: list[dict[str, str | int | float]] = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "A high-performance laptop.",
        "price": 999.99,
        "image_url": "laptop.jpg",
    },
    {
        "id": 2,
        "name": "Smartphone",
        "description": "A powerful smartphone with excellent camera.",
        "price": 799.99,
        "image_url": "smartphone.jpg",
    },
    {
        "id": 3,
        "name": "Headphones",
        "description": "Noise-cancelling over-ear headphones.",
        "price": 199.99,
        "image_url": "headphones.jpg",
    },
]


def get_item_by_id(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


@items_bp.get("/item/<int:item_id>")
def item_details(item_id: int):
    item_info = get_item_by_id(item_id=item_id)
    if item_info is None:
        return "Item Not Found", 404

    return render_template(
        "item_details.html",
        item=item_info,
    )

from typing import Optional
from pathlib import Path
from fastapi import HTTPException
from datetime import datetime

from models.order import Order, OrderCreate, OrderUpdate
from utils.file_io import load_data, save_data

def get_orders_paginated(
    data_path: Path,
    page: int = 1,
    per_page: int = 20,
    customer_name: Optional[str] = None,
    status: Optional[str] = None,
    sort_by: Optional[str] = None  # e.g., "date_asc", "date_desc", "name_asc"
) -> dict:
    orders = load_data(data_path)

    # Filtering by status
    if status:
        orders = [order for order in orders if order.get("status") == status]

    # Filtering by customer name (optional)
    if customer_name:
        orders = [
            order for order in orders
            if customer_name.lower() in order.get("customer", {}).get("name", "").lower()
        ]

    # Sorting
    if sort_by == "date_asc":
        orders.sort(key=lambda x: x["created_at"])
    elif sort_by == "date_desc":
        orders.sort(key=lambda x: x["created_at"], reverse=True)
    elif sort_by == "name_asc":
        orders.sort(key=lambda x: x["customer"]["name"].lower())
    elif sort_by == "name_desc":
        orders.sort(key=lambda x: x["customer"]["name"].lower(), reverse=True)

    # Pagination
    total_items = len(orders)
    total_pages = (total_items + per_page - 1) // per_page

    if page < 1 or (total_pages > 0 and page > total_pages):
        raise HTTPException(status_code=404, detail="Page not found")

    start = (page - 1) * per_page
    end = start + per_page
    paginated_orders = orders[start:end]

    return {
        "page": page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "data": paginated_orders
    }

def get_order(data_path: Path, order_id: int) -> Order:
    orders = load_data(data_path)
    for order in orders:
        if order["id"] == order_id:
            return order
    raise HTTPException(status_code=404, detail="Product not found")

def create_order(data_path: Path, order: OrderCreate) -> dict:
    orders = load_data(data_path)
    new_id = max((o["id"] for o in orders), default=0) + 1

    new_order = {
        "id": new_id,
        **order.model_dump()
    }

    orders.append(new_order)
    save_data(data_path, orders)
    return new_order

def patch_order(data_path: Path, order_id: int, patch_data: OrderUpdate) -> dict:
    updates = patch_data.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    orders = load_data(data_path)

    for i, order in enumerate(orders):
        if order["id"] == order_id:
            updated_order = {**order, **updates}
            orders[i] = updated_order
            save_data(data_path, orders)
            return updated_order

    raise HTTPException(status_code=404, detail="Order not found")
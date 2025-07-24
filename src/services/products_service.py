from fastapi import HTTPException # type: ignore
from pathlib import Path
from typing import List, Optional, Literal
from datetime import datetime

from models.product import Product, ProductCreate, ProductUpdate
from utils.file_io import load_data, save_data

"""This module represents the business logic of the product management"""

def get_products(data_path: Path) -> list[Product]:
    return load_data(data_path)

##def get_products_paginated(data_path: Path, page: int = 1, per_page: int = 20) -> dict:
##    products = load_data(data_path)
##    total_items = len(products)
##    total_pages = (total_items + per_page - 1) // per_page
##
##    if page < 1 or page > total_pages:
##        raise HTTPException(status_code=404, detail="Page not found")
##
##    start = (page - 1) * per_page
##    end = start + per_page
##    paginated_products = products[start:end]
##
##    return {
##        "page": page,
##        "per_page": per_page,
##        "total_items": total_items,
##        "total_pages": total_pages,
##        "has_next": page < total_pages,
##        "data": paginated_products
##    }

def get_product(data_path: Path, product_id: int) -> Product:
    products = load_data(data_path)
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

def get_products_paginated(
    data_path: Path,
    page: int = 1,
    per_page: int = 20,
    name_filter: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_quantity: Optional[int] = None,
    sort_by: Optional[str] = None
) -> dict:
    products = load_data(data_path)

    # Filtering
    if name_filter:
        products = [p for p in products if name_filter.lower() in p["name"].lower()]
    if min_price is not None:
        products = [p for p in products if p["price"] >= min_price]
    if max_price is not None:
        products = [p for p in products if p["price"] <= max_price]
    if min_quantity is not None:
        products = [p for p in products if p["quantity"] >= min_quantity]

    # Sorting
    if sort_by == "price_asc":
        products.sort(key=lambda x: x["price"])
    elif sort_by == "price_desc":
        products.sort(key=lambda x: x["price"], reverse=True)
    elif sort_by == "name_asc":
        products.sort(key=lambda x: x["name"].lower())
    elif sort_by == "name_desc":
        products.sort(key=lambda x: x["name"].lower(), reverse=True)
    elif sort_by == "date_asc":
        products.sort(key=lambda x: x["created_at"].lower())
    elif sort_by == "date_desc":
        products.sort(key=lambda x: x["created_at"].lower(), reverse=True)
    elif sort_by == "quantity_asc":
        products.sort(key=lambda x: x["quantity"])
    elif sort_by == "quantity_desc":
        products.sort(key=lambda x: x["quantity"], reverse=True)

    # Pagination
    total_items = len(products)
    total_pages = (total_items + per_page - 1) // per_page

    if page < 1 or (total_pages > 0 and page > total_pages):
        raise HTTPException(status_code=404, detail="Page not found")

    start = (page - 1) * per_page
    end = start + per_page
    paginated_products = products[start:end]

    return {
        "page": page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "data": paginated_products
    }

def create_product(data_path: Path, product: ProductCreate) -> dict:
    products = load_data(data_path)
    new_id = max((p["id"] for p in products), default=0) + 1
    new_product = {
        "id": new_id,
        **product.model_dump()
    }
    products.append(new_product)
    save_data(data_path, products)
    return new_product

def create_products_batch(data_path: Path, products_in: List[ProductCreate]) -> List[dict]:
    products = load_data(data_path)
    current_max_id = max((p["id"] for p in products), default=0)

    new_products = []
    for idx, product in enumerate(products_in, start=1):
        new_id = current_max_id + idx
        new_product = {
            "id": new_id,
            **product.model_dump()
        }
        new_products.append(new_product)

    products.extend(new_products)
    save_data(data_path, products)
    return new_products

def patch_product(data_path: Path, product_id: int, patch_data: ProductUpdate) -> dict:
    if not patch_data.model_dump(exclude_unset=True):
        raise HTTPException(status_code=400, detail="No fields provided for update")
    
    products = load_data(data_path)

    for i, product in enumerate(products):
        if product["id"] == product_id:
            updated = {**product, **patch_data.model_dump(exclude_unset=True)}
            products[i] = updated
            save_data(data_path, products)
            return updated

    raise HTTPException(status_code=404, detail="Product not found")

def delete_product(data_path: Path, product_id: int) -> None:
    products = load_data(data_path)
    filtered = [p for p in products if p["id"] != product_id]

    if len(filtered) == len(products):
        raise HTTPException(status_code=404, detail="Product not found")

    save_data(data_path, filtered)

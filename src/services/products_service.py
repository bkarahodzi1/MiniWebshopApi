from fastapi import HTTPException
from pathlib import Path
from typing import List

from models.product import Product, ProductCreate, ProductUpdate
from utils.file_io import load_data, save_data

"""This module represents the business logic of the product management"""

def get_products(data_path: Path) -> list[Product]:
    return load_data(data_path)

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

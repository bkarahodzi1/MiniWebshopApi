from typing import Dict, List, Optional, Literal
from fastapi import APIRouter, Query
from pathlib import Path

from models.product import Product, ProductCreate, ProductUpdate
from utils.file_io import load_data, save_data
from services.products_service import (
    get_products,
    get_product,
    create_product,
    create_products_batch,
    patch_product,
    delete_product,
    get_products_paginated
)


"""This module contains routes for managing products(CRUD)."""

router = APIRouter()
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "products.json"

@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):

    return get_product(DATA_PATH, product_id) 

@router.get("/")
def list_products(
    page: int = Query(1, ge=1),
    name: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_quantity: Optional[int] = None,
    sort_by: Optional[str] = None
):
    return get_products_paginated(
        DATA_PATH,
        page=page,
        name_filter=name,
        min_price=min_price,
        max_price=max_price,
        min_quantity=min_quantity,
        sort_by=sort_by
    )

@router.post("/", response_model=Product)
def create_product_endpoint(product: ProductCreate):
    """Endpoint that adds a new produtc."""

    return create_product(DATA_PATH, product)

@router.post("/batch", response_model=List[Product])
def create_products_batch_endpoint(products_in: List[ProductCreate]):
    """Endpoint that adds multiple new products."""

    return create_products_batch(DATA_PATH, products_in)

@router.patch("/{product_id}", response_model=Product)
def patch_product_endpoint(product_id: int, patch_data: ProductUpdate):
    """Partially update a product by ID."""
    
    return patch_product(DATA_PATH, product_id, patch_data)
        
@router.delete("/{product_id}", status_code=204)
def delete_product_endpoint(product_id: int):
    """Delete a product by ID."""

    delete_product(DATA_PATH, product_id)
    return "Deleted"
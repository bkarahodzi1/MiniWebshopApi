from typing import Optional
from fastapi import APIRouter, Query
from pathlib import Path
from datetime import datetime

from models.order import Order, OrderCreate, OrderUpdate
from services.orders_service import (
    get_orders_paginated,
    create_order,
    get_order,
    patch_order
)
from utils.email_utils import send_email

"""This module contains routes for managing products(CRUD)."""

router = APIRouter()
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "orders.json"

@router.get("/{order_id}", response_model=Order)
def get_order_by_id(order_id: int):

    return get_order(DATA_PATH, order_id)

@router.get("/")
def list_orders(
    page: int = Query(1, ge=1),
    customer_name: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    sort_by: Optional[str] = Query(None)
):
    return get_orders_paginated(
        data_path=DATA_PATH,
        page=page,
        customer_name=customer_name,
        status=status,
        sort_by=sort_by
    )

@router.post("/")
def create_order_route(order: OrderCreate):
    return create_order(DATA_PATH, order)

@router.patch("/{order_id}")
def update_order(order_id: int, patch_data: OrderUpdate):
    return patch_order(DATA_PATH, order_id, patch_data)
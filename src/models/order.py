from pydantic import BaseModel, EmailStr, HttpUrl
from datetime import datetime
from typing import List, Optional

"""Order model representing a customer order in the webshop."""

class CustomerInfo(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    phone: str
    address: str
    city: str
    zipCode: str

class Items(BaseModel):
    product_id: int
    quantity: int
    image: HttpUrl
    name: str
    price: float

class OrderCreate(BaseModel):
    items: List[Items]  # list of product IDs
    created_at: datetime
    decision_date: Optional[datetime] = None
    customer: CustomerInfo
    total_price: float
    status: str  # accepted, rejected, completed

class Order(OrderCreate):
    id: int
    items: List[Items]  # list of product IDs
    created_at: datetime
    decision_date: Optional[datetime] = None
    customer: CustomerInfo
    total_price: float
    status: str  # accepted, rejected, completed

class OrderUpdate(BaseModel):
    items: Optional[List[Items]] = None
    created_at: Optional[datetime] = None
    decision_date: Optional[datetime] = None
    customer: Optional[CustomerInfo] = None
    total_price: Optional[float] = None
    status: Optional[str] = None

    class Config:
        extra = 'forbid'

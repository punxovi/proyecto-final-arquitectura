from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


class OrderStatus(str, Enum):
    pending = "PENDIENTE"
    confirmed = "CONFIRMADO"
    preparing = "EN_PREPARACION"
    ready = "LISTO"
    delivered = "ENTREGADO"
    cancelled = "CANCELADO"


class OrderItem(BaseModel):
    product_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class OrderCreate(BaseModel):
    customer_name: str = Field(min_length=2)
    items: List[OrderItem] = Field(min_length=1)


class Order(BaseModel):
    id: str
    customer_name: str
    items: List[OrderItem]
    total: float
    status: OrderStatus
    created_at: str


app = FastAPI(title="PedidoFácil API", version="1.0.0")
orders: Dict[str, Order] = {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "pedidofacil-api"}


@app.post("/api/orders", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(request: OrderCreate) -> Order:
    total = round(sum(item.quantity * item.unit_price for item in request.items), 2)
    order = Order(
        id=str(uuid4()),
        customer_name=request.customer_name,
        items=request.items,
        total=total,
        status=OrderStatus.pending,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
    orders[order.id] = order
    return order


@app.get("/api/orders", response_model=List[Order])
def list_orders() -> List[Order]:
    return list(orders.values())


@app.patch("/api/orders/{order_id}/status", response_model=Order)
def update_order_status(order_id: str, new_status: OrderStatus) -> Order:
    order = orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    order.status = new_status
    return order


# La interfaz web es un cliente local sencillo para demostrar la API.
app.mount("/", StaticFiles(directory="app/static", html=True), name="frontend")

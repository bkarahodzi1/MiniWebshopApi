from fastapi import FastAPI # type: ignore
from routes import products, orders
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  
    "http://localhost:3000",  
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # <- origins allowed to access
    allow_credentials=True,
    allow_methods=["*"],              # <- allow all HTTP methods
    allow_headers=["*"],              # <- allow all headers
)
@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}

app.include_router(products.router, prefix = "/products", tags = ["products"])
app.include_router(orders.router, prefix = "/orders", tags = ["orders"])
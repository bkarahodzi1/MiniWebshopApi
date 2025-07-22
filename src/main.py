from fastapi import FastAPI
from routes import products

app = FastAPI()

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}

app.include_router(products.router, prefix = "/products", tags = ["products"])
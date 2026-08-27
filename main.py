from fastapi import FastAPI

app = FastAPI(title="E-Commerce API")

@app.get("/")
def read_root():
    return {"status": "running", "platform": "Windows Local Dev"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Wireless Mouse", "price": 25.99, "stock": 45},
        {"id": 2, "name": "Mechanical Keyboard", "price": 89.99, "stock": 18},
        {"id": 3, "name": "USB-C Hub", "price": 34.50, "stock": 60}
    ]
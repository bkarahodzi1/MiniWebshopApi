# 🛠️ Mini Webshop Backend (FastAPI)

This is the backend for the Mini Webshop project, built with **FastAPI**. It provides RESTful APIs for managing products and processing customer orders. Data is stored in simple `.json` files to simulate persistent storage.

---

## ⚙️ Tech Stack

- **Framework**: FastAPI (Python)
- **Data Storage**: JSON files
- **CORS**: Configured for frontend communication
- **Deployment**: Local or free hosting (e.g., Render)

---

## 📁 Features

- Retrieve all products
- Retrieve a single product by ID
- Add a new product
- Edit and delete products
- Place a new order
- View all orders
- Update order status (Accepted, Rejected, Completed)

---

## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/webshopapi.git
cd webshopapi
```

### 2. Create and Activate Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Enable CORS

In `main.py`, set allowed frontend origins:

```python
origins = [
    "http://localhost:5173",  # Local frontend
    "https://your-frontend-url.com",  # Deployed frontend
]
```

---

## 🚀 Running the Server Locally

```bash
fastapi dev src/main.py
```

The API will be available at:

```
http://localhost:8000
```

Interactive API docs (Swagger UI) will be available at:

```
http://localhost:8000/docs
```

---

## 📁 Project Structure

```
webshopapi/
├── src/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── data/
│   │   ├── products.json
│   │   └── orders.json
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

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

## 4. Setting Up Gmail for Sending Emails from FastAPI

1. Log in to your Gmail account (the one you'll use to send emails from FastAPI).

2. Go to your Google Account settings:  
   [https://myaccount.google.com/](https://myaccount.google.com/)

3. In the left menu, click **Security**.

4. Enable **2-Step Verification** (if it’s not already enabled):  
   - Scroll to **Signing in to Google** → click **2-Step Verification** → follow the steps to turn it on.

5. Once 2FA is enabled, go back to **Security** and find **App passwords** under the same **Signing in to Google** section.

6. Click **App passwords**. It will ask you to re-enter your password.

7. From the dropdown menus:  
   - Select app: choose **Other (Custom name)**  
   - Enter name: e.g. `FastAPI Webshop`  
   - Click **Generate**

8. Copy the generated 16-character password. It looks like:  
   `abcd efgh ijkl mnop`

You will use this password in your FastAPI email configuration instead of your normal Gmail password.

9. Set the following environment variables:
    ```bash
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=465
    EMAIL_USER=your-email@gmail.com
    EMAIL_PASS=your-app-password-here 
    ```

### 5. Enable CORS

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

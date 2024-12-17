from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

# Initialize FastAPI app
app = FastAPI()

# SQLite Database connection
def get_db_connection():
    conn = sqlite3.connect('E-Market.db')
    conn.row_factory = sqlite3.Row
    return conn

# Pydantic models for user and address
class User(BaseModel):
    username: str
    password: str
    first_name: str
    email: str
    join_date: str
    user_type: str

class UserAddress(BaseModel):
    user_id: int
    address: str
    city: str
    country: str

class UserPayment(BaseModel):
    user_id: int
    payment_type: str

# Initialize the database schema
def init_db():
    schema = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        join_date TEXT NOT NULL,
        user_type TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS user_address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        country TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS user_payment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        payment_type TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    '''
    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

# Run the initialization of the database schema when the server starts
@app.on_event("startup")
def startup():
    init_db()

# API Endpoint to create a new user
@app.post("/users/", response_model=User)
def create_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO users (username, password, first_name, email, join_date, user_type)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', 
        (user.username, user.password, user.first_name, user.email, user.join_date, user.user_type)
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return {**user.dict(), "id": user_id}

# API Endpoint to get a list of all users
@app.get("/users/", response_model=List[User])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return [dict(user) for user in users]

# API Endpoint to get user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user)

# API Endpoint to create a new user address
@app.post("/addresses/", response_model=UserAddress)
def create_address(address: UserAddress):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO user_address (user_id, address, city, country)
        VALUES (?, ?, ?, ?)
        ''', 
        (address.user_id, address.address, address.city, address.country)
    )
    conn.commit()
    address_id = cursor.lastrowid
    conn.close()
    return {**address.dict(), "id": address_id}

# API Endpoint to get all user addresses
@app.get("/addresses/{user_id}", response_model=List[UserAddress])
def get_user_addresses(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_address WHERE user_id = ?", (user_id,))
    addresses = cursor.fetchall()
    conn.close()
    return [dict(address) for address in addresses]

# API Endpoint to create a new user payment method
@app.post("/payments/", response_model=UserPayment)
def create_payment(payment: UserPayment):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO user_payment (user_id, payment_type)
        VALUES (?, ?)
        ''', 
        (payment.user_id, payment.payment_type)
    )
    conn.commit()
    payment_id = cursor.lastrowid
    conn.close()
    return {**payment.dict(), "id": payment_id}

# API Endpoint to get all user payments
@app.get("/payments/{user_id}", response_model=List[UserPayment])
def get_user_payments(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_payment WHERE user_id = ?", (user_id,))
    payments = cursor.fetchall()
    conn.close()
    return [dict(payment) for payment in payments]


if __name__ == "__main__":
    init_db()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
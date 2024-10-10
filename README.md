# Cafe API

This project is a RESTful API for managing a list of cafes. It allows users to perform various CRUD (Create, Read, Update, Delete) operations, such as retrieving all cafes, getting a random cafe, searching for a cafe by location, adding a new cafe, updating the price of a cafe, and deleting a cafe.

## Features

- **SQLite Database**: Stores cafe data, including name, location, facilities, and prices.
- **Flask-SQLAlchemy**: ORM for database operations.
- **RESTful Endpoints**:
  - `GET /random`: Returns a random cafe from the database.
  - `GET /all`: Retrieves all cafes from the database.
  - `GET /search?loc={location}`: Searches cafes by location.
  - `POST /add`: Adds a new cafe to the database.
  - `PATCH /update/{id}?new_price={price}`: Updates the price of a specific cafe.
  - `DELETE /report_deleted/{id}?api_key={api_key}`: Deletes a cafe from the database (requires an API key).

## Prerequisites

- **Python 3.x**
- **Flask** and **Flask-SQLAlchemy**
- **Postman** (to test API requests)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/angelikizoi/FlaskRESTfulProject.git
   cd FlaskRESTfulProject
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**:
   ```bash
   python main.py
   ```

   The app will run on `http://127.0.0.1:5000/` by default.

## Testing API with Postman

To test the API, you'll need **Postman** to send HTTP requests. Below are the API endpoints and how to test them using Postman.

### 1. **Get a Random Cafe**

- **Endpoint**: `/random`
- **Method**: `GET`
- **Description**: Retrieves a random cafe from the database.

**Postman Request**:
- Open **Postman**, select `GET`, and enter `http://127.0.0.1:5000/random` in the URL field.
- Click **Send** to view the random cafe details in the response.

### 2. **Get All Cafes**

- **Endpoint**: `/all`
- **Method**: `GET`
- **Description**: Retrieves all cafes from the database.

**Postman Request**:
- Open **Postman**, select `GET`, and enter `http://127.0.0.1:5000/all` in the URL field.
- Click **Send** to view all cafes in the response.

### 3. **Search Cafes by Location**

- **Endpoint**: `/search?loc={location}`
- **Method**: `GET`
- **Description**: Searches cafes by the given location.

**Postman Request**:
- Open **Postman**, select `GET`, and enter `http://127.0.0.1:5000/search?loc=London` (replace `London` with the location you're searching for).
- Click **Send** to view cafes in that location.

### 4. **Add a New Cafe**

- **Endpoint**: `/add`
- **Method**: `POST`
- **Description**: Adds a new cafe to the database.

**Postman Request**:
- Open **Postman**, select `POST`, and enter `http://127.0.0.1:5000/add` in the URL field.
- Go to the **Body** tab and select **form-data**.
- Add the following key-value pairs:
  ```
  name: New Cafe
  map_url: http://newcafe.com
  img_url: http://image.com
  location: New York
  seats: 20
  has_toilet: true
  has_wifi: true
  has_sockets: true
  can_take_calls: true
  coffee_price: $5.00
  ```
- Click **Send** to add the new cafe.

### 5. **Update Cafe Price**

- **Endpoint**: `/update/{id}?new_price={price}`
- **Method**: `PATCH`
- **Description**: Updates the price of the cafe with the given ID.

**Postman Request**:
- Open **Postman**, select `PATCH`, and enter `http://127.0.0.1:5000/update/1?new_price=$6.00` (replace `1` with the cafe ID and `$6.00` with the new price).
- Click **Send** to update the cafe price.

### 6. **Delete a Cafe**

- **Endpoint**: `/report_deleted/{id}?api_key={api_key}`
- **Method**: `DELETE`
- **Description**: Deletes the cafe with the given ID if the correct API key is provided.

**Postman Request**:
- Open **Postman**, select `DELETE`, and enter `http://127.0.0.1:5000/report_deleted/1?api_key=TopSecretApiKey` (replace `1` with the cafe ID and `TopSecretApiKey` with your API key).
- Click **Send** to delete the cafe.

## Database Configuration

The API uses **SQLite** to store cafe data. The database file is created locally as `cafes.db`. You can modify the database configuration in the `app.config['SQLALCHEMY_DATABASE_URI']` line to point to a different database (e.g., PostgreSQL or MySQL).


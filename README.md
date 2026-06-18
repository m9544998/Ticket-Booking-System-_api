# Ticket-Booking-System_api
# Ticket Booking System API

A professional RESTful API built using Flask and SQLite for managing ticket bookings.  
Users can book tickets, view all bookings, and cancel booked tickets.

---

##  Features

- Book Ticket
- View All Tickets
- Cancel Ticket
- SQLite Database Integration
- Input Validation
- Error Handling
- Structured JSON Responses
- REST API Design

---

## Technologies Used

- Python 3
- Flask
- SQLite3
- REST API
- JSON

---

##  Project Structure

```text
ticket-booking-system-api/
│
├── app.py
├── tickets.db
├── README.md
└── requirements.txt
```

---


---

### 1. Install Dependencies

```bash
pip install flask
```

---

### 2. Run Application

```bash
python app.py
```

Server will start at:

```text
http://127.0.0.1:5000
```

---


## Book Ticket

Request:

```http
POST /tickets
```

Request Body:

```json
{
    "customer_name": "Maheen",
    "movie_name": "Python Movie"
}
```

Response:

```json
{
    "message": "Ticket booked",
    "ticket_id": 1
}
```

Status:

```text
201 Created
```

---

## View Tickets

Request:

```http
GET /tickets
```

Response:

```json
[
    {
        "id": 1,
        "customer_name": "Maheen",
        "movie_name": "Python Movie"
    }
]
```

---

##  Cancel Ticket

Request:

```http
DELETE /tickets/1
```

Response:

```json
{
    "message": "Ticket cancelled"
}
```

Status:

```text
200 OK

##  Author

**Maheen Asad**

Flask • SQLite • REST API

---

 If you found this project useful, give it a star on GitHub.

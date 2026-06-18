from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DATABASE = "tickets.db"
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():

    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS tickets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        movie_name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()

@app.route("/tickets", methods=["POST"])
def book_ticket():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Data required"
        }), 400

    customer = data.get("customer_name")
    movie = data.get("movie_name")

    if not customer or not movie:
        return jsonify({
            "error": "customer_name and movie_name required"
        }), 400

    try:

        conn = get_db()

        cursor = conn.execute(
            """
            INSERT INTO tickets(
            customer_name,
            movie_name
            )
            VALUES(?,?)
            """,
            (customer, movie)
        )

        conn.commit()

        ticket_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message": "Ticket booked",
            "ticket_id": ticket_id
        }), 201

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500
@app.route("/tickets", methods=["GET"])
def get_tickets():

    try:

        conn = get_db()

        tickets = conn.execute(
            "SELECT * FROM tickets"
        ).fetchall()

        conn.close()

        return jsonify([
            dict(row)
            for row in tickets
        ])

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500
@app.route("/tickets/<int:id>", methods=["DELETE"])
def delete_ticket(id):

    try:
        conn = get_db()

        ticket = conn.execute(
            "SELECT * FROM tickets WHERE id=?",
            (id,)
        ).fetchone()

        if ticket is None:

            conn.close()

            return jsonify({
                "error": "Ticket not found"
            }), 404

        conn.execute(
            "DELETE FROM tickets WHERE id=?",
            (id,)
        )

        conn.commit()
        conn.close()

        return jsonify({
            "message": "Ticket cancelled"
        })

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500
if __name__ == "__main__":
    app.run(debug=True)
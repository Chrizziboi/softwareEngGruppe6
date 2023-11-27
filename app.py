import sqlite3

from flask import Flask, render_template, redirect, url_for, request

from backend.shopping_cart.shoppingCart import shoppingCart
from backend.users.user import user
from backend.users.admin import admin
from backend.database.db import *

app = Flask(__name__)

DATABASE = 'chinook.db'

user1 = user(userID=int(1), username="user")

admin1 = admin(adminID=int(1), adminname="admin")

shopcart = shoppingCart(user1)

db_startup()

@app.route('/user-page')
def get_storage():
    try:
        with get_db() as conn:
            peristorage = conn.execute('SELECT * FROM peristorage').fetchall()
            return render_template('user-page.html', user=user1, peristorage=peristorage)
    except Exception as e:
        print(f"Det har forekommet en feil: {e}")
        return "Det forekom en feil ved henting av brukerdata"

'''@app.route('/user-page')
def get_storage():
    conn = get_db()
    peristorage = conn.execute('SELECT * FROM peristorage').fetchall()
    return render_template('user-page.html', user=user1, peristorage=peristorage)
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-page')
def userpage():
    user1 = user(userID=1, username="user")
    return render_template('user-page.html', user=user1)

@app.route("/user-info")
def user_info():
    return render_template('user-info.html', user=user1)

def admin_info():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-info.html', admin=admin1)

@app.route('/admin-page')
def adminpage():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-page.html', admin=admin1)

@app.route("/add_tour", methods=["POST"])
def add_tour():
    name = request.form["name"]
    if name:
        conn = get_db()
        #conn.execute("INSERT INTO tours (id, name, price) VALUES (?, ?, ?)")
        conn.commit()
        conn.close()
    return redirect(url_for("list_items"))

@app.route("/search-results")
def search():
    query = request.args.get('query')
    if query:
        try:
            with get_db() as conn:
                search_results = conn.execute("SELECT name, price FROM tours WHERE name LIKE (?)",
                                              ('%' + query + '%',)).fetchall()
                for row in search_results:
                    tour_name = row[0]
                    tour_price = row[1]
                sql_translate = f"{tour_name} - Pris: {tour_price}"
                print(sql_translate)
                return render_template("search-results.html", query=query, results=sql_translate)
        except Exception as e:
            print(f"Feil ved henting av tabell {e}")
            return redirect("/user-page")
    else:
        return render_template('user-page.html', user=user1)

def login():
    pass

if __name__ == '__main__':
    app.run(debug=True)



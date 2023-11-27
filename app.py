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

user1_shoppingCart = shoppingCart(user1)

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

@app.route('/user-trips')
def usertrips():
    user1 = user(userID=1, username="user")

    return render_template('user-trips.html', user=user1)

@app.route('/user-edit')
def useredit():
    user1 = user(userID=1, username="user")

    return render_template('user-edit.html', user=user1)

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


@app.route('/admin-edit')
def adminedit():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-edit.html', admin=admin1)

@app.route('/admin-trips')
def admintrips():
    admin1 = admin(adminID=1, adminname="admin")
    return render_template('admin-trips.html', admin=admin1)

'''@app.route("/add_item", methods=["POST"])
def add_item():
    name = request.form["name"]'''

@app.route("/add_tour", methods=["POST"])
def add_tour():
    tour_name = request.form["navn"]
    tour_price = request.form["pris"]
    try:
        with get_db() as conn:

            conn.execute(
                "INSERT INTO tours (name, price) VALUES (?, ?)",
                (tour_name, tour_price)
            )
            conn.commit()
    finally:
        conn.close()
        return redirect("/admin-page")


'''    if name:
        shoppingCart.add_tour(user1_shoppingCart, name, price)'''

@app.route("/delete_tour", methods=["POST"])
def delete_tour():
    tour_id = request.form["id"]
    try:
        with get_db() as conn:
            conn.execute("DELETE FROM tours WHERE id = (?)",
                (tour_id,)
            )
            conn.commit()
    finally:
        with get_db() as conn:
            search_results = conn.execute("SELECT * FROM tours").fetchall()
            return render_template("search-results.html", results=search_results)


'''    if name:
        shoppingCart.add_tour(user1_shoppingCart, name, price)'''


@app.route("/search-results")
def search():
    query = request.args.get('query')
    if query:
        try:
            with get_db() as conn:
                search_results = conn.execute("SELECT name, price FROM tours WHERE name LIKE (?)",
                                              ('%' + query + '%',)).fetchall()
                for row in search_results:
                    tour_id = row[0]
                    tour_name = row[1]
                    tour_price = row[2]
                sql_translate = f"ID: {tour_id} - Navn: {tour_name} - Pris: {tour_price}"
                print(sql_translate)
                return render_template("search-results.html", results=search_results, query=query)
        except Exception as e:
            print(f"Feil ved henting av tabell {e}")
            return redirect("/user-page")
    else:
        with get_db() as conn:
            search_results = conn.execute("SELECT * FROM tours").fetchall()
            return render_template("search-results.html",results=search_results)

#render_template('user-page.html', user=user1)

@app.route("/admin-search-results")
def admin_search():
    query = request.args.get('query')
    if query:
        try:
            with get_db() as conn:
                search_results = conn.execute("SELECT id, name, price FROM tours WHERE name LIKE (?)",
                                              ('%' + query + '%',)).fetchall()
                for row in search_results:
                    tour_id = row[0]
                    tour_name = row[1]
                    tour_price = row[2]
                sql_translate = f"ID: {tour_id} - Navn: {tour_name} - Pris: {tour_price}"
                print(sql_translate)
                return render_template("admin-search-results.html", results=search_results, query=query)
        except Exception as e:
                print(f"Feil ved henting av tabell {e}")
                return redirect("/admin-page")
    else:
        with get_db() as conn:
            search_results = conn.execute("SELECT * FROM tours").fetchall()
            return render_template("admin-search-results.html", results=search_results)

@app.route('/shoppingcart')
def shoppingcart():
    user1 = user(userID=1, username="user")
    return render_template('shoppingcart.html', user=user1)

def login():
    pass

if __name__ == '__main__':
    app.run(debug=True)



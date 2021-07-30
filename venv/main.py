from flask import Flask
from flask import render_template, request, g
import sqlite3
import random

from werkzeug.utils import redirect

DATABASE = "C:\\python\\cs50Project\\venv\\shortenurl.db"
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_db(query, args=()):
    con = sqlite3.connect("C:\\python\\cs50Project\\venv\\shortenurl.db")
     # Getting cursor
    c =  con.cursor() 
    # Adding data
    c.execute(query, args)
    # Applying changes
    con.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        long_url = request.form['longurl']
        short_url = generate_random()
        insert_db("INSERT INTO urls (long_url, short_url) VALUES (?, ?)", (long_url,short_url,))
        short_url = "http://127.0.0.1:5000/" + short_url
        return render_template("index.html", shorturl = short_url, longurl = long_url)


@app.route("/<shorturl>")
def redirecttolongurl(shorturl):
    short_exists = query_db("SELECT * FROM urls WHERE short_url = ?", [shorturl], one = True)
    print(short_exists)
    if not short_exists:
        return render_template("error.html")
    else:
        return redirect(short_exists[1])


def generate_random():
    while True:
        short_url = "s"
        shortCharacters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random_digits = [random.randint(0, 51) for i in range(0, 8)]
        for value in random_digits:
            short_url += shortCharacters[value]
        print(short_url)
        short_exists = query_db("SELECT * FROM urls WHERE short_url = ?", [short_url])
        if not short_exists:
            break
    return short_url

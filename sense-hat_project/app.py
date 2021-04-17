from flask import Flask, render_template, request, current_app as app
from sense_hat import SenseHat 
from time import sleep
import sys
import sqlite3


sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods= ['GET', 'POST'])
def success():
    message = request.form['message']
    sense.show_message(str(message))

    return render_template("success.html", message = message)

@app.route('/send', methods=['POST'])
def sent():
    message = request.form['message']
    name = request.form['name']

    conn = sqlite3.connect('/.static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO messages VALUES((?),(?)", (name, message))
    conn.commit()

    conn.closet()
    return render_template("sent.html", message = message, name = name)

@app.route('/all')
def all():
    #Connect to database and insert name and message
    conn = sqlite3.connect('/.static/data/senseDisplay.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message':row[1]}
        messages.append(message)
    conn.close()
    return render_template('all.html', messages = messages)


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
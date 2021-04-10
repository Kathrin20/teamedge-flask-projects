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

    #Connect to database and insert name and message
    conn = sqlite3.connect('/.static/data/senseDisplay.db');
    curs = conn.cursor()
    curs.execute("INSERT INTO messages VALUES((?),(?)", (name, message))
    conn.commit()

    #Close database
    conn.close()

    return render_template("success.html", message = message)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
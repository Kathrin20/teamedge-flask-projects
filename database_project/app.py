from flask import Flask, render_template, request, current_app as app
from sense_hat import SenseHat
from flask_apscheduler import APScheduler 
from time import sleep
import sys
import sqlite3

sense = SenseHat()

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

#scheduler.add_job(id ='1', func = 'show_reminder', trigger='date', 
#run_date = '2021-04-26T8:15', args=['Do your Micro hw :/'])
#def show_reminder(remider)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/done', methods=['POST'])
def done():
    reminder = request.form['reminder']
    date = request.form['date']

    display = reminder + " due " + date

    sense.show_message(display)

    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO (reminder, date) VALUES((?),(?))", (reminder, date))
    conn.commit()

    conn.close()
    return render_template("done.html", reminder = reminder, date=date)

@app.route('/response', methods=['GET', 'POST'])
def response():



    return render_template("response.html")

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
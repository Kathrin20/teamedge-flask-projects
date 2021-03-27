from flask import Flask, render_template, request, current_app as app
from sense_hat import SenseHat 
from time import sleep


sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods= ['GET', 'POST'])
def success():
    message = request.form['message']
    sense.show_message(str(message))
    sense.show_message("Nice to see you there!", text_colour=[128,0,128] )
    return render_template("success.html", message = message)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
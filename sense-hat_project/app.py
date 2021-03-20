from flask import Flask, render_template, request, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods= ['GET', 'POST'])
def success():
    message = request.form['message']
    
    return render_template("success.html", message = message)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
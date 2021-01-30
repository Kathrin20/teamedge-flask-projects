from flask import Flask, render_template, current_app as app

app = Flask(__name__)


@app.route('/')
def index():
	return 'Welcome to Kathrin\'s Rainbow Project'

@app.route('/red')
def red_html():
    color = 'red'
    return render_template('colorful.html', color = color)

@app.route('/orange')
def orange_html():
    color = 'orange'
    return render_template('colorful.html', color = color)

@app.route('/yellow')
def yellow_html():
    color = 'yellow'
    return render_template('colorful.html', color = color)

@app.route('/green')
def green_html():
    color = 'greem'
    return render_template('colorful.html', color = color)

@app.route('/blue')
def blue_html():
    color = 'blue'
    return render_template('colorful.html', color = color)

@app.route('/indigo')
def indigo_html():
    color = 'indigo'
    return render_template('colorful.html', color = color)

@app.route('/violet')
def violet_html():
    color = 'violet'
    return render_template('colorful.html', color = color)

@app.route('/rainbow')
def rainbow_html():
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet' ]
    return render_template('colorful.html', color = color)

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')

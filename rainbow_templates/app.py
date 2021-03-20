from flask import Flask, render_template, current_app as app

app = Flask(__name__)


@app.route('/')
def index():
	return 'Welcome to Kathrin\'s Rainbow Project'

@app.route('/red')
def red_html():
    return render_template('colorful.html', color = 'red')

@app.route('/orange')
def orange_html():
    return render_template('colorful.html', color = 'orange')

@app.route('/yellow')
def yellow_html():
    return render_template('colorful.html', color = 'yellow')

@app.route('/green')
def green_html():
    return render_template('colorful.html', color = 'green')

@app.route('/blue')
def blue_html():
    return render_template('colorful.html', color = 'blue')

@app.route('/indigo')
def indigo_html():
    return render_template('colorful.html', color = 'indigo')

@app.route('/violet')
def violet_html():
    return render_template('colorful.html', color = 'violet')

@app.route('/rainbow')
def rainbow_html():
    color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    return render_template('other.html', color = color)

if __name__ == '__main__':
    app.run(debug=True, host ='0.0.0.0')

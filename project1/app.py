from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/bulletin')
def bulletin():
    return render_template('bulletin.html')

@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

@app.route('/join_us')
def join_us():
    return render_template('join_us.html')

@app.route('/message_center')
def message_center():
    return render_template('message_center.html')

if __name__ == '__main__':
    app.run(debug=True)
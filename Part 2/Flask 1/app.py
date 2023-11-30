from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index(data=df):
    data = data.sample(30)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()

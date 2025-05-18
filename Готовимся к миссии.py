from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index/<title>')
def index(title='заготовка'):
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
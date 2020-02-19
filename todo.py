from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    text = db.Column(db.String(200))


@app.route('/')
@app.route('/home')
def index():
    todos = Todo.query.all()
    return render_template('index.html', title="Home", todos=todos)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task = Todo(title=request.form['title'], text=request.form['text'])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
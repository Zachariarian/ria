from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////path/to/database.db'
db = SQLAlchemy(app)

print(app.config['SQLALCHEMY_DATABASE_URI'])

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    amount = db.Column(db.Integer)
    date = db.Column(db.DateTime)

@app.route('/')
def index():
    return redirect(url_for('new_loan'))

@app.route('/new_loan', methods=['GET', 'POST'])
def new_loan():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        amount = request.form['amount']
        loan = Loan(name=name, email=email, amount=amount)
        db.session.add(loan)
        db.session.commit()
        return redirect(url_for('loan_submitted'))
    return render_template('new_loan.html')

@app.route('/loan_submitted')
def loan_submitted():
    return render_template('loan_submitted.html')

@app.route('/past_loans')
def past_loans():
    loans = Loan.query.all()
    return render_template('past_loans.html', loans=loans)

if __name__ == '__main__':
    app.run() 

from flask import Flask

app = Flask(__name__)

@app.route('/')


class Loan:
    def __init__(self, amount, interest_rate, term):
        self.amount = amount
        self.interest_rate = interest_rate
        self.term = term
        self.payments = []

def monthly_payment(self):
    r = self.interest_rate / 100 / 12
    n = self.term * 12
    return self.amount * r * (1 + r) ** n / ((1 + r) ** n - 1)

def payment_schedule(self):
    payment = self.monthly_payment()
    balance = self.amount
    for i in range(self.term * 12):
        interest = balance * self.interest_rate / 100 / 12
        principal = payment - interest
        balance -= principal
        self.payments.append((i+1, payment, principal, interest, balance))

def print_schedule(self):
    print("Payment schedule:")
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Month", "Payment", "Principal", "Interest", "Balance"))
    for payment in self.payments:
        print("{:<10} {:<15.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(*payment))

loan = Loan(10000, 5, 5)
loan.payment_schedule()


def index():

    return '''

        <form method="post" action="/loan">

            <label for="amount">Loan amount:</label>

            <input type="text" name="amount"><br>

            <label for="interest_rate">Interest rate:</label>

            <input type="text" name="interest_rate"><br>

            <label for="term">Term in years:</label>

            <input type="text" name="term"><br>

            <input type="submit" value="Submit">

        </form>

    '''
    
from loan import Loan

@app.route('/loan', methods=['POST'])

def loan():

    amount = float(request.form['amount'])

    interest_rate = float(request.form['interest_rate'])

    term = int(request.form['term'])

    loan = Loan(amount, interest_rate, term)

    loan.payment_schedule()

    return '''

        <h1>Payment schedule:</h1>

        <table>

            <thead>

                <tr>

                    <th>Month</th>

                    <th>Payment</th>

                    <th>Principal</th>

                    <th>Interest</th>

                    <th>Balance</th>

                </tr>

            </thead>

            <tbody>

                {% for payment in loan.payments %}

                    <tr>

                        <td>{{ payment[0] }}</td>

                        <td>{{ payment[1] }}</td>

                        <td>{{ payment[2] }}</td>

                        <td>{{ payment[3] }}</td>

                        <td>{{ payment[4] }}</td>

                    </tr>

                {% endfor %}

            </tbody>

        </table>

    '''
 
loan.print_schedule()
   
if __name__ == '__main__':

    app.run()
    

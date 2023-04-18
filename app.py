from flask import Flask

app = Flask(__name__)

@app.route('/')

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
    
    if __name__ == '__main__':

    app.run()




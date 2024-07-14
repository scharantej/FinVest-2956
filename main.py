
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for processing the user's input and generating a financial plan
@app.route('/results', methods=['POST'])
def results():
    # Get the user's input from the form
    income = float(request.form['income'])
    expenses = float(request.form['expenses'])
    savings_goal = float(request.form['savings_goal'])

    # Calculate the user's surplus or deficit
    surplus = income - expenses

    # Generate a financial plan based on the user's input
    plan = generate_plan(income, expenses, savings_goal, surplus)

    # Render the results page, passing in the generated plan
    return render_template('results.html', plan=plan)

# A sample function to generate a financial plan. In a real-world scenario, this
# function would perform more complex calculations and provide personalized recommendations.
def generate_plan(income, expenses, savings_goal, surplus):
    plan = {
        "savings_rate": surplus / income,
        "investment_return": 0.05,
        "years_to_goal": savings_goal / (surplus * (1 + 0.05)),
        "recommendations": [
            "Increase your income by negotiating a raise or finding a side hustle.",
            "Reduce your expenses by cutting back on unnecessary spending.",
            "Invest your savings in a diversified portfolio to grow your wealth."
        ]
    }

    return plan

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

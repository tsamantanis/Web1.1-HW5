from flask import Flask, request

from unit_tests.string_functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/color_form')
def show_color_form():
    return """
    <form action="/color_results" method="GET">
        <label>
            What's your favorite color?
            <input type="text" name="color">
        </label>
        <input type="submit" name="Submit!">
    </form>
    """

@app.route('/color_results')
def process_color_results():
    users_favorite_color = request.args.get('color')
    if users_favorite_color == '':
        return "You did\'t specify a color!"
    return f"Wow, {users_favorite_color} is my favorite color, too!"


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/><br/>
        What toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    toppings = request.args.get('toppings')
    if users_froyo_flavor == '' and  toppings == '':
        return "You didn\'t specify a flavor or any toppings!"
    elif users_froyo_flavor == '':
        return "You didn\'t specify a flavor!"
    elif toppings == '':
        return "You didn\'t specify any toppings!"
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {toppings}!'


@app.route('/reverse_message')
def reverse_message_form():
    return """
    <form action="/message_results" method="POST">
        What's your message?
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    message = request.form.get('message')
    if message == '':
        return "You didn\'t add a message to reverse!"
    reversed_message = reverse(message)
    return f'Here\'s your reversed message: {reversed_message}'


@app.route('/calculator')
def calculator():
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    if request.args.get('operand1') == '':
        return "You didn\'t specify operand1!"
    if request.args.get('operand2') == '':
        return "You didn\'t specify operand2!"
    if (not request.args.get('operand1').startswith('-') and not request.args.get('operand1').isdigit()) or (not request.args.get('operand2').startswith('-') and not request.args.get('operand2').isdigit()):
        return 'Operands cannot be strings!'
    operand1 = int(request.args.get('operand1'))
    operand2 = int(request.args.get('operand2'))
    operation = request.args.get('operation')
    if operation == 'divide' and operand2 == 0:
        return "You cannot divide by zero!"
    if operation == 'add':
        result = operand1 + operand2
    elif operation == 'subtract':
        result = operand1 - operand2
    elif operation == 'multiply':
        result = operand1 * operand2
    else:
        result = operand1 / operand2
    return f'You chose to {operation} {operand1} and {operand2}. Your result is: {result}'


if __name__ == '__main__':
    app.run(debug=True)

import os
import signal
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify

import sympy

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))
history_file = os.path.join(base_dir, 'data', 'calculation_history.txt')

@app.route("/")
def calculator():
    print("Serving home page 'calculator.html'")
    return render_template('calculator.html', provided_expression=None, result=None)

@app.route("/calculate", methods=['POST'])
def calculate():
    expression = request.form['expression']
    print(f"Evaluating the expression '{expression}' with route 'calculate'")
    try:
        print(expression)
        result = sympy.sympify(expression)
        save_to_history(expression, result)
        return render_template('calculator.html', provided_expression=expression, result=result)
    except (sympy.SympifyError, TypeError):
        return render_template('calculator.html', provided_expression=expression, result="Invalid expression. Please enter a valid expression.")

@app.route("/history")
def history():
    print("Serving 'history.html' page to show history")
    calculations = load_history()
    return render_template('history.html', calculations=calculations)

@app.route("/api/history")
def api_history():
    print("Generating History in api in JSON")
    history = load_history()
    calculations_dict = {"history": history}
    return jsonify(calculations_dict)

def save_to_history(expression, result):
    try:
        sympy.sympify(expression)
        with open(history_file, 'a') as file:
            file.write(f"{expression} = {result}\n")
    except (sympy.SympifyError, TypeError):
        pass

def load_history():
    history = []
    try:
        with open(history_file, 'r') as file:
            history = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return history

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

def signal_handler(sig, frame):
    print('Server stopped.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    app.run(host='localhost', port=60002, debug=True)
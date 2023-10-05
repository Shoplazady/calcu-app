from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"})
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Students! Kubernetes CI/CD is working!"

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    
    if not data or 'operation' not in data or 'num1' not in data or 'num2' not in data:
        return jsonify(error="Missing required parameters: operation, num1, num2"), 400
        
    operation = data['operation'].lower()
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify(error="Inputs num1 and num2 must be numerical values"), 400

    # Push 1: Addition and Subtraction
    if operation == "addition" or operation == "add":
        result = num1 + num2
    elif operation == "subtraction" or operation == "subtract":
        result = num1 - num2
        
    # Push 2: Multiplication and Division
    elif operation == "multiplication" or operation == "multiply":
        result = num1 * num2
    elif operation == "division" or operation == "divide":
        if num2 == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        result = num1 / num2
    else:
        return jsonify(error="Invalid operation. Choose add, subtract, multiply, or divide"), 400

    return jsonify(operation=operation, num1=num1, num2=num2, result=result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

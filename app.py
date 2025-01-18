from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        except ValueError:
            result = "Invalid input"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the port Render provides
    app.run(host="0.0.0.0", port=port, debug=True)

from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = None
    gst = 0
    total = 0

    if request.method == "POST":
        try:
            # Get form inputs
            hall_rent = float(request.form.get("hall_rent", 0))
            food = float(request.form.get("food", 0))
            miscellaneous = float(request.form.get("miscellaneous", 0))
            gst_option = request.form.get("gst_option", "no")  # Default to "no"

            # Calculate GST only if "Yes" is selected
            if gst_option == "yes":
                gst = 0.18 * hall_rent

            # Total calculation
            total = hall_rent + gst + food + miscellaneous

            # Result summary
            result = {
                "hall_rent": hall_rent,
                "food": food,
                "miscellaneous": miscellaneous,
                "gst": round(gst, 2),
                "total": round(total, 2)
            }
        except ValueError:
            result = "Invalid input! Please enter numeric values."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

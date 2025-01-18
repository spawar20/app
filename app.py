from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    result = {}
    gst = 0
    total = 0

    if request.method == "POST":
        try:
            # Get form inputs
            hall_rent = float(request.form.get("hall_rent", 0))
            food = float(request.form.get("food", 0))
            miscellaneous = float(request.form.get("miscellaneous", 30000))  # Default value
            guruji = float(request.form.get("guruji", 0))
            saman = float(request.form.get("saman", 0))
            photo = float(request.form.get("photo", 0))
            decoration = float(request.form.get("decoration", 45000))  # Default value
            haldi = float(request.form.get("haldi", 0))  # New field for Haldi
            evening_tea = float(request.form.get("evening_tea", 0))
            dinner = float(request.form.get("dinner", 0))
            morning_breakfast = float(request.form.get("morning_breakfast", 0))
            pedhe = float(request.form.get("pedhe", 0))
            gst_option = request.form.get("gst_option", "no")  # Default to "no"

            # Calculate GST only if "Yes" is selected
            if gst_option == "yes":
                gst = 0.18 * hall_rent

            # Total calculation
            total = (
                hall_rent + gst + food + miscellaneous + guruji + saman +
                photo + decoration + haldi + evening_tea + dinner +
                morning_breakfast + pedhe
            )

            # Result summary
            result = {
                "hall_rent": hall_rent,
                "food": food,
                "miscellaneous": miscellaneous,
                "guruji": guruji,
                "saman": saman,
                "photo": photo,
                "decoration": decoration,
                "haldi": haldi,  # Include Haldi in the result
                "evening_tea": evening_tea,
                "dinner": dinner,
                "morning_breakfast": morning_breakfast,
                "pedhe": pedhe,
                "gst": round(gst, 2),
                "total": round(total, 2),
                "gst_option": gst_option  # Persist GST option
            }
        except ValueError:
            result = {"error": "Invalid input! Please enter numeric values."}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

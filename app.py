from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        customer = request.form["customer"]
        items = request.form.getlist("item[]")
        qtys = request.form.getlist("qty[]")
        prices = request.form.getlist("price[]")

        products = []
        subtotal = 0

        for i in range(len(items)):
            total = int(qtys[i]) * float(prices[i])
            products.append({
                "name": items[i],
                "qty": qtys[i],
                "price": prices[i],
                "total": total
            })
            subtotal += total

        gst = round(subtotal * 0.18, 2)
        grand_total = round(subtotal + gst, 2)

        return render_template(
            "invoice.html",
            customer=customer,
            products=products,
            subtotal=subtotal,
            gst=gst,
            grand_total=grand_total,
            invoice_no=random.randint(1000,9999),
            date=datetime.now().strftime("%d-%m-%Y")
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

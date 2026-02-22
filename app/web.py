from flask import Flask, request, jsonify, render_template_string
from app.services.pricing import calculate_final_price

app = Flask(__name__)

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pricing Calculator</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: system-ui, sans-serif; background: #f5f5f5; display: flex; justify-content: center; padding: 60px 20px; }
        .card { background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.1); padding: 40px; width: 100%; max-width: 420px; }
        h1 { font-size: 1.5rem; margin-bottom: 24px; color: #333; }
        label { display: block; font-size: 0.85rem; font-weight: 600; color: #555; margin-bottom: 6px; }
        input, select { width: 100%; padding: 10px 12px; border: 1px solid #ddd; border-radius: 8px; font-size: 1rem; margin-bottom: 16px; }
        input:focus, select:focus { outline: none; border-color: #4f46e5; box-shadow: 0 0 0 3px rgba(79,70,229,0.1); }
        button { width: 100%; padding: 12px; background: #4f46e5; color: #fff; border: none; border-radius: 8px; font-size: 1rem; cursor: pointer; }
        button:hover { background: #4338ca; }
        .result { margin-top: 20px; padding: 16px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; display: none; }
        .result .label { font-size: 0.85rem; color: #666; }
        .result .price { font-size: 2rem; font-weight: 700; color: #16a34a; }
        .breakdown { font-size: 0.85rem; color: #888; margin-top: 8px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Pricing Calculator</h1>
        <form id="priceForm">
            <label for="base">Base Price ($)</label>
            <input type="number" id="base" value="100" min="0" step="0.01">
            <label for="customer">Customer Type</label>
            <select id="customer">
                <option value="premium">Premium (20% off)</option>
                <option value="standard" selected>Standard (10% off)</option>
                <option value="new">New (no discount)</option>
            </select>
            <button type="submit">Calculate Price</button>
        </form>
        <div class="result" id="result">
            <div class="label">Final Price</div>
            <div class="price" id="finalPrice"></div>
            <div class="breakdown" id="breakdown"></div>
        </div>
    </div>
    <script>
        document.getElementById('priceForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const base = document.getElementById('base').value;
            const customer = document.getElementById('customer').value;
            const res = await fetch(`/price?base=${base}&customer=${customer}`);
            const data = await res.json();
            document.getElementById('finalPrice').textContent = '$' + data.final_price.toFixed(2);
            document.getElementById('breakdown').textContent =
                `Base: $${data.base_price} | Type: ${data.customer_type} | Tax: 5%`;
            document.getElementById('result').style.display = 'block';
        });
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_PAGE)


@app.route("/price")
def price():
    base_price = request.args.get("base", 100, type=float)
    customer_type = request.args.get("customer", "standard", type=str)

    final_price = calculate_final_price(base_price, customer_type)

    return jsonify({
        "base_price": base_price,
        "customer_type": customer_type,
        "final_price": final_price
    })


if __name__ == "__main__":
    app.run(debug=True)

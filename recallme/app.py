from flask import Flask, render_template_string
from .main import load_recalls, load_purchases, check_recalls

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>RecallMe</title>
<h1>Produits rappelés</h1>
{% if alerts %}
<ul>
{% for item in alerts %}
<li>{{ item['name'] }} ({{ item['brand'] }})</li>
{% endfor %}
</ul>
{% else %}
<p>Aucun produit rappelé parmi vos achats.</p>
{% endif %}
"""

@app.route("/")
def index():
    recalls = load_recalls()
    purchases = load_purchases()
    alerts = check_recalls(recalls, purchases)
    return render_template_string(TEMPLATE, alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8058105739:AAGYQ2goMQqS1KOTaHQ9e6zTIfcTDJv1MiA"
CHAT_ID = "-1002137579033"  # Ton groupe privé

@app.route("/send_order", methods=["POST"])
def send_order():
    data = request.get_json()

    produit_id = data.get("produit_id")
    produit_nom = data.get("produit_nom")
    quantite = data.get("quantite")
    telegram_user = data.get("telegram_user", "Inconnu")

    message = f"""🧪 <b>Nouvelle commande MeltLabz</b>\n
🆔 <b>ID Produit :</b> {produit_id}
📦 <b>Nom :</b> {produit_nom}
📏 <b>Quantité :</b> {quantite}
👤 <b>Client :</b> {telegram_user}"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)
    return jsonify({"status": "ok", "telegram_response": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # autoriser toutes les origines

# Config Telegram
BOT_TOKEN = "8058105739:AAGYQ2goMQqS1KOTaHQ9e6zTIfcTDJv1MiA"
GROUP_CHAT_ID = "-1002647230701"  # ton groupe


@app.route('/send_order', methods=['POST'])
def send_order():
    try:
        data = request.get_json()

        produit_id = data.get("produit_id")
        produit_nom = data.get("produit_nom")
        quantite = data.get("quantite")
        telegram = data.get("telegram", "@Inconnu")
        paiement = data.get("paiement", "Non précisé")
        nom = data.get("nom", "")
        prenom = data.get("prenom", "")
        adresse = data.get("adresse", "")
        cp = data.get("cp", "")
        tel = data.get("tel", "")
        infos = data.get("infos", "")

        message = f"""🧪 Nouvelle Commande

📦 Produit : {produit_nom}
📏 Quantité : {quantite}

👤 Client :
• {telegram}
• Prénom : {prenom}
• Nom : {nom}
• Téléphone : {tel}

🏠 Livraison :
• Adresse : {adresse}
• Code Postal : {cp}
• Infos supplémentaires : {infos}

💰 Paiement : {paiement}
"""


        # Envoyer vers Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": GROUP_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        r = requests.post(url, json=payload)
        if r.status_code == 200:
            return jsonify({"ok": True})
        else:
            return jsonify({"ok": False, "error": f"Télégram error: {r.text}"})

    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

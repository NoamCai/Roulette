from flask import Flask, request, jsonify

app = Flask(__name__)

def initialiser_cagnotte(montant, devise):
    montant = int(montant)

    symboles = {
        "euro": "€",
        "dollar": "$"
    }

    if devise.lower() not in symboles:
        return {"succes": False, "erreur": "Devise invalide"}

    symbole = symboles[devise.lower()]

    if 1 <= montant <= 1000:
        return {
            "succes": True,
            "cagnotte": montant,
            "devise": symbole,
            "message": f"Cagnotte creee : {montant} {symbole}"
        }

    return {"succes": False, "erreur": "Montant invalide"}


# 🔥 API (reçoit les données du site)
@app.route("/api/cagnotte")
def cagnotte():
    montant = request.args.get("montant")
    devise = request.args.get("devise")

    return jsonify(initialiser_cagnotte(montant, devise))


# 🔥 page web (HTML affiché)
@app.route("/")
def home():
    return """
    <h1>Roulette</h1>

    <form action="/api/cagnotte" method="GET">
        <input type="number" name="montant" placeholder="Montant">
        <input type="text" name="devise" placeholder="euro ou dollar">
        <button type="submit">Créer cagnotte</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
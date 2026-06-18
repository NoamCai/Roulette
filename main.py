from flask import Flask, redirect, render_template, request, jsonify, url_for
from fonctions.cagnotte import initialiser_cagnotte
from flask import Flask, jsonify
import random

app = Flask(__name__)

cagnotte = 0

@app.route("/api/cagnotte")
def cagnotter():
    global cagnotte

    montant = request.args.get("montant", default=0, type=int)
    devise = request.args.get("devise")

    result = initialiser_cagnotte(cagnotte, montant, devise)
    if result.get("success") is True:
        cagnotte = result.get("cagnotte")

    return jsonify(result)

@app.route("/api/cagnotter2")
def cagnotter2():
    global cagnotte

    montant = request.args.get("montant", default=0, type=int)
    devise = request.args.get("devise")

    result = initialiser_cagnotte(cagnotte, montant, devise)
    if result.get("success") is True:
        cagnotte = result.get("cagnotte")

    return f"{cagnotte} €"

@app.route("/", methods=['GET', 'POST'])
def home():   
    global cagnotte

    if request.method == 'POST':
        # Si l'utilisateur a cliqué sur le bouton, on incrémente
        cagnotte += 1
        # On redirige vers la fonction 'home' pour rafraîchir proprement
        return redirect(url_for('home')) # <--- C'est ici qu'on corrige !
    
    return render_template('index.html', cagnotteHtml=cagnotte)

if __name__ == '__main__':
    app.run(debug=True)

<<<<<<< HEAD


=======
    from flask import Flask, jsonify
import random

app = Flask(__name__)
>>>>>>> b91d1c0c6ae11cb66649bae8383360c109f2af90

@app.route("/api/tirage")
def tirage():
    chiffre = random.randint(1, 36)

    return jsonify({
        "resultat": chiffre
    })

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True, host="127.0.0.1")


=======
    app.run(debug=True, host="0.0.0.0")
>>>>>>> b91d1c0c6ae11cb66649bae8383360c109f2af90

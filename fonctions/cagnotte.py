def initialiser_cagnotte(cagnotteActuelle, montant, devise):
    cagnotteActuelle = int(cagnotteActuelle)
    montant = int(montant)

    symboles = {
        "euro": "€",
        "dollar": "$"
    }

    if devise.lower() not in symboles:
        return {"success": False, "erreur": "Devise invalide"}

    symbole = symboles[devise.lower()]

    if 1 <= montant <= 1000:
        cagnotteActuelle = cagnotteActuelle + montant;
        return {
            "success": True,
            "cagnotte": cagnotteActuelle,
            "devise": symbole,
            "message": f"Cagnotte creee : {montant} {symbole}"
        }

    return {"success": False, "erreur": "Montant invalide"}
def initialiser_cagnotte(montant, devise):
    montant = int(montant)

    symboles = {
        "euro": "€",
        "dollar": "$"
    }

    if devise.lower() not in symboles:
        return {
            "succes": False,
            "erreur": "Devise non supportée"
        }

    symbole = symboles[devise.lower()]

    if 1 <= montant <= 1000:
        return {
            "succes": True,
            "message": f"Super ! Votre cagnotte est de {montant} {symbole}",
            "cagnotte": montant,
            "devise": symbole
        }

    return {
        "succes": False,
        "erreur": "Montant doit être entre 1 et 1000"
    }
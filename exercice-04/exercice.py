ventes = [
{"produit": "café", "prix": 2.5, "quantite": 120},
{"produit": "thé", "prix": 2.0, "quantite": 80},
{"produit": "jus", "prix": 3.5, "quantite": 45},
]
ca_par_produit = {}
plus_grand_ca = 0

for vente in ventes:
    total_vente = vente["prix"] * vente["quantite"]
    nom_produit = vente["produit"]
    ca_par_produit[nom_produit] = total_vente
    if total_vente > plus_grand_ca:
        plus_grand_ca = total_vente
        produit_max = nom_produit
print(ca_par_produit)

ca_total = sum(ca_par_produit.values())
print("total :", ca_total)

print("meilleur produit :", produit_max)
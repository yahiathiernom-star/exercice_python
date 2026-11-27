produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)

print(f"{quantite} x {produit} : {total_ttc:.2f} euros TTC")

prix_texte = "19.90"
prix_converti = float(prix_texte)
total_ttc_depuis_texte = prix_converti * quantite * (1 + taux_tva)
print(f"Avec le prix converti : {total_ttc_depuis_texte:.2f} euros TTC")

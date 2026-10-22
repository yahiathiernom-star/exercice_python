produit = "clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.2

total_ht = prix_ht * quantite
total_ttc = total_ht + (total_ht * taux_tva)

print("Le prix total HT est de : ", round(total_ht, 2))
print(quantite, "x", produit, "-", round(total_ttc, 2))

prix_texte = "19.90"
prix_conv = (float(prix_texte))

print(prix_conv)

total_ht = prix_ht * quantite
total_ttc = total_ht + (total_ht * taux_tva)

print("Le prix total HT est de : ", round(total_ht, 2))

from outils import conv_to_int, mention
notes_brutes = ["12,5", "15", "abc", "9", "18.25"]
notes_nettoyees = []
for n in notes_brutes:
    note_propre = conv_to_int(n)
    if note_propre is not None:  
        notes_nettoyees.append(note_propre)
print(f"les notes ignorées : {len(notes_brutes) - len(notes_nettoyees)}")
print(f"moyenne : {round(sum(notes_nettoyees)/len(notes_nettoyees), 2)}") 
print(f"mention : {mention(sum(notes_nettoyees)/len(notes_nettoyees))}")       




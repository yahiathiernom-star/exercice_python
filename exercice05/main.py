from outils import conv_to_int, mention
notes_brutes = ["12.5", "15", "abc", "9", "18.25"]
notes_nettoyees = []
for n in notes_brutes:
    note_propre = conv_to_int(n)
    if note_propre is not None:  
        notes_nettoyees.append(note_propre)
print(f"les notes ignorées : {len(notes_brutes) - len(notes_nettoyees)}")
print(f"moyenne : {round(sum(notes_nettoyees)/len(notes_nettoyees), 2)}") 
print(f"mention : {mention(sum(notes_nettoyees)/len(notes_nettoyees))}")       




"""for note in notes_brutes:
    conv_note = conv_to_int(note)
    if conv_note is not None:
        print(f"moyenne : {sum([conv_note])/len([conv_note])}")
        print(f"mention : {mention(conv_note)}")
    else:
        print(f"les notes ignorées : {len(notes_brutes) - sum(1 for n in notes_brutes if conv_to_int(n) is not None)}")"""
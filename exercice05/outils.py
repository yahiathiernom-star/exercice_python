def conv_to_int (texte):
    try:
        return float(texte)
    except ValueError:
       return None

def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Insuffisant"

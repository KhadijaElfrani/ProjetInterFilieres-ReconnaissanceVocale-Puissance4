from Reconnaissance import reconnaissance

while True:
    ordre = reconnaissance()
    if ordre == "première colonne" or ordre == "1e colonne" or ordre == "2e colonne" or ordre == "deuxième colonne" or ordre == "troisième colonne" or ordre == "3e colonne" or ordre == "4e colonne" or ordre == "cinquième colonne" or ordre == "5e colonne":

        print("Je met la balle dans la", ordre)
        continue
    elif ordre == "quitter":
        print("Au revoir!")
        break

    else:
        print("j'ai pas compris, veuillez réessayer...")
        print()




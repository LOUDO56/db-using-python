import sqlite3 as sql



def liste_maladie():
    """Cette fonction permet d'afficher la page web de la liste des maladies."""
    co = sql.connect('plantes_medicinales.db') # On se connecte à la base de données
    liste_maladie = [] # Définition de la table sur les informations de chaque maladies
    for row in co.execute("SELECT * FROM maladie"): # On récupère les informations de la table Maladie en faisant une requète à la base de données
        liste_maladie.append(list(row))
    if len(liste_maladie) != 0: # Si la table n'est pas vide
        for i in range(len(liste_maladie)): # On boucle la table
            nom_plante = co.execute(f"SELECT nom_commun FROM plante WHERE id = {liste_maladie[i][2]};").fetchone() # On fait de requète pour récuperer le nom des plantes assigné à leur ID
            nom_plante = str(nom_plante).replace("('","")
            nom_plante = str(nom_plante).replace("',)","")
            if nom_plante != "None": # Si l'id existe, on le remplace, sinon on affiche une erreur.
                liste_maladie[i][2] = nom_plante 
            else:
                liste_maladie[i][2] = f"L'ID que vous avez indiquée ({liste_maladie[i][2]}) n'existe pas, veuillez le créer"
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Liste Maladie</title>
        </head>
        <body>
            <header>
                <nav class="navbar">
                    <ul class="navlinks">
                        <li class="navlink"><a href="http://localhost/liste_plante.py">Liste des plantes</a></li>
                        <li class="navlink"><a href="http://localhost/liste_maladie.py">Liste des maladies</a></li>
                        <li class="navlink"><a href="http://localhost/liste_patient.py">Liste des patients</a></li>
                        <li class="navlink"><a href="http://localhost/liste_rdv.py">Liste des rdv</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <h1>Liste des maladies</h1>
                <a class="add" href="http://localhost/ajouter_maladie.py">Ajouter une maladie</a>""")
    if len(liste_maladie) != 0:  # Si la table est vide, la box pour supprimer un élément ne sera pas disponible
        print("""

        <div class="form_suppr">
            <p>Supprimer une maladie</p>
            <form action = "/compl_supprimer.py" method = "post">
                <input type="hidden" name="type_base" value="maladie">
                <label for="id_db">REF</label>
                <input type="number" id="id_db" name="id_db" required>
                <button type="submit">Supprimer</button>
        </div>

""")
      

                
    for i in range(len(liste_maladie)):
        print("""
        <table class="liste" cellspacing="0" style="width:30%;">
            <thead>
                <tr class="categorie">
                    <th>REF</th>
                    <th>Nom</th>
                    <th>Guéri par</th>
                </tr>
            </thead>       
            <tbody>
        """)
        print("""<tr class="information">""")
        for j in range(len(liste_maladie[i])):
            print("<td>", str(liste_maladie[i][j]), "</td>")
        print("""</tr>
                </tobdy>
                </table>""")
    print("</main> </body> </html>")
    co.close()
        

liste_maladie()






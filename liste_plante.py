import sqlite3 as sql



def liste_plante():
    """Cette fonction permet d'afficher la page web de la liste des plantes."""
    co = sql.connect('plantes_medicinales.db')  # On se connecte à la base de données
    liste_plante = [] # Définition de la table sur les informations de chaque plantes
    for row in co.execute("SELECT * FROM plante"): # On récupère les informations de la table Maladie en faisant une requète à la base de données
        liste_plante.append(list(row))
    if len(liste_plante) != 0: # Si la table n'est pas vide
        for i in range(len(liste_plante)): # On boucle la table
            nom_maladie = co.execute(f"SELECT nom FROM maladie WHERE id = {liste_plante[i][5]};").fetchone() # On fait de requète pour récuperer le nom des maladies assigné à leur ID
            nom_maladie = str(nom_maladie).replace("('","")
            nom_maladie = str(nom_maladie).replace("',)","")
            if nom_maladie != "None": # Si l'id existe, on le remplace, sinon on affiche une erreur.
                liste_plante[i][5] = nom_maladie
            else:
                liste_plante[i][5] = f"L'ID que vous avez indiquée {liste_plante[i][5]} n'existe pas, veuillez le créer"
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <title>Liste plante</title>
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
                <h1>Liste des plantes</h1>
                <a class="add" href="http://localhost/ajouter_plante.py">Ajouter une plante</a>""")
    
    if len(liste_plante) != 0: # Si la table est vide, la box pour supprimer un élément ne sera pas disponible
        print("""

        <div class="form_suppr">
            <p>Supprimer une plante</p>
            <form action = "/compl_supprimer.py" method = "post">
                <input type="hidden" name="type_base" value="plante">
                <label for="id_db">REF</label>
                <input type="number" id="id_db" name="id_db" required>
                <button type="submit">Supprimer</button>
        </div>
        """)
    
     
    for i in range(len(liste_plante)):
        print("""
        <table class="liste" cellspacing="0" style="width: 75%;">
            <thead>
                <tr class="categorie">
                    <th>REF</th>
                    <th>Nom Commun</th>
                    <th>Nom Scientifique</th>
                    <th>Descriptif</th>
                    <th>Famille</th>
                    <th>Maladie traité</th>
                    <th>Posolopie</th>
                    <th>Illustration</th>
                    <th>Stock</th>
                </tr>
            </thead>       
            <tbody>
        """)
        print("""<tr class="information">""")
        for j in range(len(liste_plante[i])):
            if j == 3:
                print('<td class="no-text-center">', str(liste_plante[i][j]), "</td>")
            else:
                print("<td>", str(liste_plante[i][j]), "</td>")
        print("""</tr>
                </tobdy>
                </table>""")
    print("</main> </body> </html>")
    co.close()
        

liste_plante()






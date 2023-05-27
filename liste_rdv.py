import sqlite3 as sql

def liste_rdv():
    """Cette fonction permet d'afficher la page web de la liste des rendez-vous."""
    co = sql.connect('plantes_medicinales.db') # On se connecte à la base de données
    liste_rdv = [] #Définition de la table sur les informations de chaque rendew-vous
    for row in co.execute("SELECT * FROM rdv"): # On récupère les informations de la table Rdv en faisant une requète à la base de données
        liste_rdv.append(list(row))
    if len(liste_rdv) != 0: # Si la table n'est pas vide
        for i in range(len(liste_rdv)): # On boucle la table
            nom_maladie = co.execute(f"SELECT nom FROM maladie WHERE id = {liste_rdv[i][4]};").fetchone() # On fait de requète pour récuperer le nom des maladies assigné à leur ID
            nom_maladie = str(nom_maladie).replace("('","")
            nom_maladie = str(nom_maladie).replace("',)","")
            if nom_maladie != "None": # Si l'id existe, on le remplace, sinon on affiche une erreur.
                liste_rdv[i][4] = nom_maladie
            else:
                liste_rdv[i][4] = f"L'ID que vous avez indiquée {liste_rdv[i][4]} n'existe pas, veuillez le créer"
           
            nom_plante = co.execute(f"SELECT nom_commun FROM plante WHERE id = {liste_rdv[i][5]};").fetchone() # On fait de requète pour récuperer le nom des plantes assigné à leur ID
            nom_plante = str(nom_plante).replace("('","")
            nom_plante = str(nom_plante).replace("',)","")
            if nom_plante != "None": # Si l'id existe, on le remplace, sinon on affiche une erreur.
                liste_rdv[i][5] = nom_plante
            else:
                liste_rdv[i][5] = f"L'ID que vous avez indiquée {liste_rdv[i][3]} n'existe pas, veuillez le créer"

    
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Liste des rendez-vous</title>
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
                <h1>Liste des rendez-vous</h1>
                <a class="add" href="http://localhost/ajouter_rdv.py">Ajouter un rendez-vous</a>""")
    if len(liste_rdv) != 0: # Si la table est vide, la box pour supprimer un élément ne sera pas disponible
        print("""     
            <div class="form_suppr">
                <p>Supprimer un rendez-vous</p>
                <form action = "/compl_supprimer.py" method = "post">
                    <input type="hidden" name="type_base" value="rdv">
                    <label for="id_db">REF</label>
                    <input type="number" id="id_db" name="id_db" required>
                    <button type="submit">Supprimer</button>
            </div>""")
                
    
    for i in range(len(liste_rdv)):
        print("""
        <table class="liste" cellspacing="0" style="width:35%;">
            <thead>
                <tr class="categorie">
                    <th>REF</th>
                    <th>Date</th>
                    <th>Nom</th>
                    <th>ID patient</th>
                    <th>Maladie a traiter</th>
                    <th>Plante a utiliser</th>
                    
                </tr>
            </thead>       
            <tbody>
        """)
        print("""<tr class="information">""")
        for j in range(len(liste_rdv[i])):
            print("<td>", str(liste_rdv[i][j]), "</td>")
        print("""</tr>
                </tobdy>
                </table>""")
    print("</main> </body> </html>")
    co.close()
    
def broad_id(id):
    print(id)
    
liste_rdv()

import sqlite3 as sql

def liste_patient():
    """Cette fonction permet d'afficher la page web de la liste des patients."""
    co = sql.connect('plantes_medicinales.db') # On se connecte à la base de données
    liste_patient = [] # Définition de la table sur les informations de chaque patients
    for row in co.execute("SELECT * FROM patient"): # On récupère les informations de la table Patient en faisant une requète à la base de données
        liste_patient.append(list(row))
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Liste Patients</title>
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
                <h1>Liste des patients</h1>
                <a class="add" href="http://localhost/ajouter_patient.py">Ajouter un patient</a>""")
    if len(liste_patient) != 0:  # Si la table est vide, la box pour supprimer un élément ne sera pas disponible
        print("""  
        <div class="form_suppr">
            <p>Supprimer un patient</p>
            <form action = "/compl_supprimer.py" method = "post">
                <input type="hidden" name="type_base" value="patient">
                <label for="id_db">REF</label>
                <input type="number" id="id_db" name="id_db" required>
                <button type="submit">Supprimer</button>
        </div>""")
    
    for i in range(len(liste_patient)):
        print("""
        <table class="liste" cellspacing="0" style="width:30%;">
            <thead>
                <tr class="categorie">
                    <th>REF</th>
                    <th>Prenom</th>
                    <th>Nom</th>
                    <th>Adresse</th>
                    <th>Téléphone</th>
                </tr>
            </thead>       
            <tbody>
        """)
        print("""<tr class="information">""")
        for j in range(len(liste_patient[i])):
            print("<td>", str(liste_patient[i][j]), "</td>")
        print("""</tr>
                </tobdy>
                </table>""")
    print("</main> </body> </html>")
    co.close()
    
    
liste_patient()


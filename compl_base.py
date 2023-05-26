import cgi
import sqlite3


def added_success():
    """Cette fonction permet d'afficher la page web pour dire que notre ajout de nos élément à la base de donnée a
        marché avec succès."""
    action = formulaire.getvalue("type_base")
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ajout avec succès</title>
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
                <h2>Vous avez ajouté votre élément avec succès !</h2>""")
    
    print(f"""
    
        <h2><a href="http://localhost:80/liste_{action}.py">Actualiser votre table</a></h2>



    """)

def ajouter_base(table, formulaire):
    if table == "maladie":
        # récupération des données du formulaire
        nom = formulaire.getvalue("nom")
        id_plante = formulaire.getvalue("id_plante")

        # insertion des données du formulaire dans la base
        connexion = sqlite3.connect('plantes_medicinales.db')
        curseur = connexion.cursor()
        donnees = (nom, id_plante)
        curseur.execute("""INSERT INTO maladie(nom, id_plante) VALUES(?, ?)""", donnees)
    
    elif table == "plante":
        # récupération des données du formulaire
        nom_commun = formulaire.getvalue("nom_commun")
        nom_scientifique = formulaire.getvalue("nom_scientifique")
        descriptif = formulaire.getvalue("descriptif")
        famille = formulaire.getvalue("famille")
        id_maladie = formulaire.getvalue("id_maladie")
        posologie = formulaire.getvalue("posologie")
        image = formulaire.getvalue("image")
        stock = formulaire.getvalue("stock")


        # insertion des données du formulaire dans la base
        connexion = sqlite3.connect('plantes_medicinales.db')
        curseur = connexion.cursor()
        donnees = (nom_commun, nom_scientifique, descriptif, famille, id_maladie, posologie, image, stock)
        curseur.execute("""INSERT INTO plante(nom_commun, nom_scientifique, descriptif, famille, id_maladie, posologie, image, stock) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", donnees)
        
    elif table == "patient":
        prenom = formulaire.getvalue("prenom")
        nom = formulaire.getvalue("nom")
        adresse = formulaire.getvalue("adresse")
        telephone = formulaire.getvalue("telephone")


        # insertion des données du formulaire dans la base
        connexion = sqlite3.connect('plantes_medicinales.db')
        curseur = connexion.cursor()
        donnees = (prenom, nom, adresse, telephone)
        curseur.execute("""INSERT INTO patient(prenom, nom, adresse, telephone) VALUES(?, ?, ?, ?)""", donnees)
    

    elif table == "rdv":
        date = formulaire.getvalue("date")
        nom = formulaire.getvalue("nom")
        id_patient = formulaire.getvalue("id_patient")
        id_maladie = formulaire.getvalue("id_maladie")
        id_plante = formulaire.getvalue("id_plante")


        # insertion des données du formulaire dans la base
        connexion = sqlite3.connect('plantes_medicinales.db')
        curseur = connexion.cursor()
        donnees = (date, nom, id_patient, id_maladie, id_plante)
        curseur.execute("""INSERT INTO rdv(date, nom, id_patient, id_maladie, id_plante) VALUES(?, ?, ?, ?, ?)""", donnees)

        
    connexion.commit()
    curseur.close()
    connexion.close()

formulaire = cgi.FieldStorage()
ajouter_base(formulaire.getvalue('type_base'), formulaire)
added_success()
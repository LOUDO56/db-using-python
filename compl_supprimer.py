import cgi
import sqlite3

def deleted_success():
    """Cette fonction permet d'afficher la page web pour montrer que l'on a supprimé notre élément avec succès."""
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Supprimer avec succès</title>
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
                <h2>Vous avez supprimé votre élément avec succès !</h2>""")
    
    print(f"""
    
        <h2><a href="http://localhost:80/liste_{action}.py">Actualiser votre table</a></h2>



    """)

# récupération des données du formulaire
formulaire = cgi.FieldStorage()
id_db = formulaire.getvalue("id_db")
table = formulaire.getvalue("type_base")
print(table)

# insertion des données du formulaire dans la base
connexion = sqlite3.connect('plantes_medicinales.db')
curseur = connexion.cursor()
curseur.execute(f"""DELETE FROM {table} WHERE ID = ?;""", (id_db,))
connexion.commit()
curseur.close()
connexion.close()

deleted_success()
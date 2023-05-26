import sqlite3 as sql


def ajouter_maladie():
    """Cette fonction permet d'afficher la page web pour ajouter une maladie"""
    print("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" href="outils_web/style.css">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ajouter Plante</title>
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
                <h1>Ajouter une maladie</h1>
                <form action = "/compl_base.py" method = "post" class="form_ajouter">
                    <input type="hidden" name="type_base" value="maladie">
                    <label for="nom">Nom</label>
                    <input type="text" id="nom" name="nom" required>
                    
                    <label for="id_plante">ID Plante</label>
                    <input type="number" id="id_plante" name="id_plante" required>
                    
                    
                    <button type="submit">Ajouter la maladie</button>
                </form>
            """)
    
ajouter_maladie()

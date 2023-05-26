import sqlite3 as sql


def ajouter_plante():
    """Cette fonction permet d'afficher la page web pour ajouter une plante"""
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
                <h1>Ajouter une plante</h1>
                <form action = "compl_base.py" method = "post" class="form_ajouter">
                    <input type="hidden" name="type_base" value="plante">
                    <label for="nom_commun">Nom Commun</label>
                    <input type="text" id="nom_commun" name="nom_commun" required>
                    
                    <label for="nom_scientifique">Nom Scientifique</label>
                    <input type="text" id="nom_scientifique" name="nom_scientifique" required>
                    
                    <label for="descriptif">Descriptif</label>
                    <textarea id="descriptif" name="descriptif"></textarea>
                    
                    <label for="famille">Famille</label>
                    <input type="text" id="famille" name="famille" required>
                    
                    <label for="id_maladie">ID Maladie</label>
                    <input type="number" id="id_maladie" name="id_maladie" required>
                    
                    <label for="posologie">Posologie</label>
                    <input type="text" id="posologie" name="posologie" required>
                    
                    <label for="image">Image</label>
                    <input type="text" id="image" name="image" required>
                    
                    <label for="stock">Stock</label>
                    <input type="number" id="stock" name="stock" required>
                    
                    <button type="submit">Ajouter la plante</button>
                </form>
            """)
    
ajouter_plante()
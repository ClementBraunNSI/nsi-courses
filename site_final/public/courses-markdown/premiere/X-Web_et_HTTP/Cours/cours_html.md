# HTML : le langage du Web

**HTML** (HyperText Markup Language) est le langage de balisage standard utilisé pour créer et structurer le contenu des pages web. Créé par Tim Berners-Lee en 1991, HTML utilise un système de balises pour définir la structure et le contenu d'une page web.

## Structure d'un document HTML

Voici la structure de base d'un document HTML :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titre de la page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Titre principal</h1>
        <nav>
            <ul>
                <li><a href="#">Accueil</a></li>
                <li><a href="#">À propos</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>Section 1</h2>
            <p>Contenu de la section 1.</p>
        </section>
        
        <section>
            <h2>Section 2</h2>
            <p>Contenu de la section 2.</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Mon Site Web</p>
    </footer>
</body>
</html>
```

## Les principales balises HTML

- **Balises de structure** :
  - `<!DOCTYPE html>` : Déclare le type de document (HTML5)
  - `<html>` : Élément racine du document
  - `<head>` : Contient les métadonnées
  - `<body>` : Contient le contenu visible
  - `<header>`, `<main>`, `<footer>`, `<section>`, `<article>`, `<nav>` : Balises sémantiques pour structurer le contenu

- **Balises de texte** :
  - `<h1>` à `<h6>` : Titres de différents niveaux
  - `<p>` : Paragraphe
  - `<strong>` : Texte important (généralement en gras)
  - `<em>` : Texte mis en emphase (généralement en italique)

- **Balises de lien et média** :
  - `<a href="url">` : Lien hypertexte
  - `<img src="image.jpg" alt="description">` : Image
  - `<video>`, `<audio>` : Éléments multimédias

- **Balises de liste** :
  - `<ul>` : Liste non ordonnée (à puces)
  - `<ol>` : Liste ordonnée (numérotée)
  - `<li>` : Élément de liste

- **Balises de tableau** :
  - `<table>` : Définit un tableau
  - `<tr>` : Ligne de tableau
  - `<th>` : Cellule d'en-tête
  - `<td>` : Cellule de données

- **Balises de formulaire** :
  - `<form>` : Définit un formulaire
  - `<input>` : Champ de saisie
  - `<textarea>` : Zone de texte multiligne
  - `<button>` : Bouton
  - `<select>` et `<option>` : Liste déroulante

## Formulaires et transmission de données

Les formulaires HTML permettent aux utilisateurs d'envoyer des données au serveur. Ils sont définis par la balise `<form>` et contiennent divers éléments interactifs comme des champs de texte, des cases à cocher, des boutons radio, etc.

### Structure d'un formulaire

```html
<form action="/traitement.php" method="post">
    <label for="nom">Nom :</label>
    <input type="text" id="nom" name="nom" required>
    
    <label for="email">Email :</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message :</label>
    <textarea id="message" name="message"></textarea>
    
    <button type="submit">Envoyer</button>
</form>
```

Attributs importants de la balise `<form>` :
- **action** : URL où les données du formulaire seront envoyées
- **method** : Méthode HTTP utilisée pour envoyer les données (GET ou POST)

# Projet Tableaux de Maîtres Revisités avec des Renards

Ce dossier contient les ressources pour le projet "Tableaux de Maîtres Revisités avec des Renards" pour le cours de NSI Première.

## Contenu du dossier

- `Projet.md` : Description complète du projet et des consignes
- `exemple_index.html` : Exemple de page HTML pour présenter un tableau revisité
- `exemple_style.css` : Exemple de feuille de style CSS à adapter
- `exemple_script.js` : Exemple de script JavaScript avec les fonctionnalités interactives

## Comment utiliser ces ressources

### 1. Comprendre le projet

Commencez par lire attentivement le fichier `Projet.md` qui explique l'objectif du projet, les consignes et les critères d'évaluation.

### 2. Explorer les exemples

Les fichiers d'exemple vous montrent comment structurer votre page web et implémenter les fonctionnalités interactives. Vous pouvez les utiliser comme point de départ pour votre propre projet.

### 3. Créer votre projet

Pour commencer votre projet :

1. Créez un nouveau dossier pour votre projet avec la structure suivante :
   ```
   projet-tableau-renard/
   ├── index.html
   ├── images/
   ├── styles/
   │   └── style.css
   └── scripts/
       └── script.js
   ```

2. Adaptez les exemples fournis à votre tableau choisi :
   - Modifiez le contenu HTML pour présenter votre tableau et raconter votre histoire
   - Personnalisez le CSS pour créer un style qui correspond à l'ambiance de votre tableau
   - Adaptez le JavaScript pour implémenter au moins deux fonctionnalités interactives

### 4. Conseils pour les débutants en JavaScript

Si vous n'avez jamais utilisé JavaScript auparavant, voici quelques conseils :

- **Comprendre avant de modifier** : Prenez le temps de comprendre comment fonctionne chaque partie du code avant de le modifier
- **Modifications progressives** : Faites des petites modifications une par une et testez régulièrement
- **Utiliser la console** : Si quelque chose ne fonctionne pas, ouvrez la console du navigateur (F12) pour voir les erreurs
- **Commentaires** : Les exemples contiennent des commentaires qui expliquent ce que fait chaque partie du code

### 5. Ressources supplémentaires

Si vous avez besoin d'aide ou d'inspiration supplémentaire :

- [MDN Web Docs - JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [W3Schools - JavaScript Tutorial](https://www.w3schools.com/js/)
- [CSS-Tricks](https://css-tricks.com/)

## Adaptation des fonctionnalités JavaScript

Voici comment adapter les différentes fonctionnalités à votre projet :

### 1. Effet de survol sur le tableau

Dans votre fichier HTML, assurez-vous d'avoir une image avec l'ID `tableau-image` :
```html
<img id="tableau-image" src="images/votre-tableau-renard.jpg" alt="Votre Tableau Revisité">
```

Dans votre fichier JavaScript, modifiez les chemins des images :
```javascript
const tableauOriginal = 'images/votre-tableau-original.jpg';
const tableauRenard = 'images/votre-tableau-renard.jpg';
```

### 2. Galerie de détails

Dans votre HTML, créez des miniatures avec la classe `detail-miniature` et l'attribut `data-image` :
```html
<img class="detail-miniature" src="images/detail1-petit.jpg" data-image="images/detail1-grand.jpg" alt="Description du détail">
```

### 3. Quiz

Modifiez les questions et les réponses dans votre HTML pour qu'elles correspondent à votre tableau :
```html
<div class="question">
    <p>Votre question ici ?</p>
    <label><input type="radio" name="question1" value="incorrect"> Réponse incorrecte</label><br>
    <label><input type="radio" name="question1" value="correct"> Réponse correcte</label><br>
    <label><input type="radio" name="question1" value="incorrect"> Autre réponse incorrecte</label><br>
</div>
```

### 4. Mode jour/nuit

Cette fonctionnalité devrait fonctionner sans modification, assurez-vous simplement d'avoir un bouton avec l'ID `bouton-mode` dans votre HTML.

## Bon projet !

N'hésitez pas à être créatif et à personnaliser votre page au-delà des exemples fournis. L'objectif est de créer une page web unique qui met en valeur votre tableau revisité et raconte une histoire intéressante !
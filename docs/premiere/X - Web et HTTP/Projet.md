# Création de pages WEB dynamiques : Tableaux de maîtres revisités avec des renards

Le but de ce projet est de créer une page web présentant un tableau de maître revisité avec des renards. Chaque élève travaillera sur un tableau différent, qu'il choisira ou tirera au sort parmi une sélection de 18 tableaux.

## La page Web et son style

Vous devrez créer une page web présentant le tableau revisité qui vous a été attribué. Votre page devra inclure :

- Une présentation du tableau original (titre, auteur, date, contexte historique)
- Une présentation du tableau revisité avec des renards
- Une histoire inventée autour de ce tableau et de ses personnages renards
- Des éléments visuels et textuels mettant en valeur votre créativité

Vous réaliserez une arborescence correcte avec :

- Les images dans le dossier **images**
- Les feuilles de style dans un dossier **styles**
- Les scripts JavaScript dans un dossier **scripts**
- La page web nommée **index.html** à la racine de l'arborescence

### Organisation des fichiers

```
projet-tableau-renard/
├── index.html
├── images/
│   ├── tableau-original.jpg
│   └── tableau-renard.jpg
├── styles/
│   └── style.css
└── scripts/
    └── script.js
```

## 2 - Dynamiser la page

Pour rendre votre page plus interactive, vous allez implémenter quelques fonctionnalités JavaScript simples. Vous n'avez pas besoin d'avoir des connaissances avancées en JavaScript, des modèles de code vous seront fournis que vous pourrez adapter à votre projet.

Voici les fonctionnalités que vous devrez implémenter  :

### Effet de survol sur le tableau

Lorsque l'utilisateur passe la souris sur l'image du tableau, vous pouvez :

- Afficher le tableau original à la place du tableau revisité
- Afficher une légende ou une information supplémentaire
- Zoomer légèrement sur l'image

```javascript

const tableauImage = document.getElementById('tableau-image');
const tableauOriginal = 'images/tableau-original.jpg';
const tableauRenard = 'images/tableau-renard.jpg';


tableauImage.addEventListener('mouseover', function() {
  tableauImage.src = tableauOriginal;
});


tableauImage.addEventListener('mouseout', function() {
  tableauImage.src = tableauRenard;
});
```

### Pour aller plus loin : Quiz sur le tableau original

Créez un petit quiz avec quelques questions sur le tableau original :

```javascript

const quizForm = document.getElementById('quiz-form');
const resultatQuiz = document.getElementById('resultat-quiz');

quizForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Empêche l'envoi du formulaire
  
  
  const reponse1 = document.querySelector('input[name="question1"]:checked');
  const reponse2 = document.querySelector('input[name="question2"]:checked');
  
  
  let score = 0;
  if (reponse1 && reponse1.value === 'correct') {
    score++;
  }
  if (reponse2 && reponse2.value === 'correct') {
    score++;
  }
  
  // Afficher le résultat
  resultatQuiz.textContent = `Vous avez obtenu ${score} point(s) sur 2 !`;
  resultatQuiz.style.display = 'block';
});
```

## Ressources

- [MDN Web Docs - JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript)
- [W3Schools - JavaScript Tutorial](https://www.w3schools.com/js/)
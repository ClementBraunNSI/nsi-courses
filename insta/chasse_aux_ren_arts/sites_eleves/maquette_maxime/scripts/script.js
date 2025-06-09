
// Changement d’image au survol
const imgRenard = document.getElementById("image-renard");
if (imgRenard) {
  imgRenard.addEventListener("mouseover", () => {
    imgRenard.src = "images/tableau-original.jpg";
  });
  imgRenard.addEventListener("mouseout", () => {
    imgRenard.src = "images/tableau-renard.jpg";
  });
}

// Changement de texte au survol
const sectionHistoire = document.querySelector(".histoire");
const originalHistoire = sectionHistoire?.innerHTML;
const newHistoire = `
  <h3>Le Fils de l'homme</h3>
  <p>Le tableau original de René Magritte montre un homme en costume avec une pomme verte cachant son visage. C'est une image célèbre du surréalisme.</p>
  <p>Il évoque les limites de ce que l’on peut percevoir et l’idée que ce qui est le plus important est souvent dissimulé.</p>
`;

if (sectionHistoire) {
  sectionHistoire.addEventListener("mouseover", () => {
    sectionHistoire.innerHTML = newHistoire;
  });
  sectionHistoire.addEventListener("mouseout", () => {
    sectionHistoire.innerHTML = originalHistoire;
  });
}

// Quiz à étapes
const questions = [
  {
    question: "Qui est l'auteur du tableau 'Le Fils de l'homme' ?",
    options: ["Salvador Dalí", "René Magritte", "Pablo Picasso"],
    answer: 1
  },
  {
    question: "Quel fruit cache le visage de l’homme dans le tableau ?",
    options: ["Une poire", "Une orange", "Une pomme"],
    answer: 2
  },
  {
    question: "Quel est le style artistique de ce tableau ?",
    options: ["Cubisme", "Surréalisme", "Expressionnisme"],
    answer: 1
  },
  {
    question: "Quelle est la signification de l’objet masquant le visage ?",
    options: ["L'interdiction", "La dissimulation", "La rébellion"],
    answer: 1
  }
];

let currentQuestion = 0;
let score = 0;

const quizQuestion = document.getElementById("quiz-question");
const quizOptions = document.getElementById("quiz-options");
const quizResult = document.getElementById("quiz-result");
const nextButton = document.getElementById("next-question");

function loadQuestion() {
  const q = questions[currentQuestion];
  quizQuestion.textContent = q.question;
  quizOptions.innerHTML = "";

  q.options.forEach((option, index) => {
    const btn = document.createElement("button");
    btn.textContent = option;
    btn.onclick = () => {
      if (index === q.answer) {
        score++;
        quizResult.textContent = "Bonne réponse !";
        quizResult.style.color = "green";
      } else {
        quizResult.textContent = "Mauvaise réponse.";
        quizResult.style.color = "red";
      }
      nextButton.style.display = "inline-block";
    };
    quizOptions.appendChild(btn);
  });
}

nextButton.onclick = () => {
  currentQuestion++;
  quizResult.textContent = "";
  nextButton.style.display = "none";
  if (currentQuestion < questions.length) {
    loadQuestion();
  } else {
    quizQuestion.textContent = "Quiz terminé !";
    quizOptions.innerHTML = "";
    quizResult.textContent = `Score final : ${score}/${questions.length}`;
    quizResult.style.color = "blue";
  }
};

loadQuestion();
const toggleBtn = document.getElementById("toggle-theme");

if (toggleBtn) {
  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("dark");
  });
}
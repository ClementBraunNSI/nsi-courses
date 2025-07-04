<style>
/* Styles pour les cours avec système de cartes */

.course-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 1rem 0;
    max-width: 100%;
}

.course-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-left: 4px solid;
    width: 100%;
    max-width: 100%;
    margin: 1rem 0;
}

.course-card.definition {
    border-left-color: #4CAF50;
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.05) 0%, rgba(76, 175, 80, 0.02) 100%);
}

.course-card.definition:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
}

.course-card.example {
    border-left-color: #2196F3;
    background: linear-gradient(135deg, rgba(33, 150, 243, 0.05) 0%, rgba(33, 150, 243, 0.02) 100%);
}

.course-card.example:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(33, 150, 243, 0.3);
}

.course-card.warning {
    border-left-color: #F44336;
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.05) 0%, rgba(244, 67, 54, 0.02) 100%);
}

.course-card.warning:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(244, 67, 54, 0.3);
}

.course-card.tip {
    border-left-color: #FF9800;
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.05) 0%, rgba(255, 152, 0, 0.02) 100%);
}

.course-card.tip:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(255, 152, 0, 0.3);
}

.course-card.highlight {
    border-left-color: #9C27B0;
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.05) 0%, rgba(156, 39, 176, 0.02) 100%);
}

.course-card.highlight:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(156, 39, 176, 0.3);
}

.course-title {
    margin: 0 0 1rem 0;
    color: var(--md-primary-fg-color);
    font-size: 1.3rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.course-content {
    margin-bottom: 1rem;
    line-height: 1.7;
    font-size: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.badge.definition {
    background: rgba(76, 175, 80, 0.15);
    color: #4CAF50;
}

.badge.example {
    background: rgba(33, 150, 243, 0.15);
    color: #2196F3;
}

.badge.warning {
    background: rgba(244, 67, 54, 0.15);
    color: #F44336;
}

.badge.tip {
    background: rgba(255, 152, 0, 0.15);
    color: #FF9800;
}

.badge.highlight {
    background: rgba(156, 39, 176, 0.15);
    color: #9C27B0;
}

.btn {
    background: white;
    color: #4169E1;
    border: 2px solid #4169E1;
    padding: 0.8rem 1.5rem;
    border-radius: 10px;
    cursor: pointer;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 1rem;
    text-decoration: none;
}

.btn:hover {
    background: rgba(65, 105, 225, 0.1);
    border-color: #1E90FF;
    color: #1E90FF;
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(65, 105, 225, 0.4);
}

.exercise-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.math-container {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    text-align: center;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.table tr:hover {
    background: #f8f9fa;
}

code {
    background: #f1f3f4;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem;
    color: #d63384;
}

pre {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    padding: 1.5rem;
    overflow-x: auto;
    margin: 1.5rem 0;
}

pre code {
    background: none;
    padding: 0;
    color: #495057;
}

.highlight {
    background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-weight: 600;
}
</style>

# 📚 Les réseaux sociaux : Définitions et Principes

<div class="course-container">
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Définition</h3>
        <div class="course-content">
            Un réseau social correspond à un groupe de personnes qui sont liées par des points communs qui peuvent être :  <br><br>* des amitiés<br>* des goûts partagés<br>* des passions partagées<br>* des intérêts communs.<br><br>De manière plus globale, on définit aussi un réseau social comme étant un site internet qui permet aux internautes de communiquer, de se créer des pages et de partager tous types d'informations.<br><br>Ces réseaux sociaux sont basés sur le WEB qui est une application d'Internet.<br><br>Il existe bons nombres de réseaux sociaux qui sont tous de formes ou d'utilisations différentes. Certains permettent de relier les gens et de les faire communiquer, d'autres servent à partager des actualités ou encore certains partager des vidéos, des photos etc...<br><br><strong>Activité :</strong><br><strong>Choisissez un réseau social que vous connaissez et définissez le.</strong><br><strong>Expliquez en quoi il est différent des autres? comment fonctionne-t-il? Qui l'a fondé? Quand? Pour quel but?</strong>
        </div>
    </div>
    
    <div class="course-card highlight">
        <div class="badge highlight">📚 Historique</div>
        <h3 class="course-title">Histoire des réseaux sociaux</h3>
        <div class="course-content">
            Les réseaux sociaux ont vu le jour au début des années 2000, en plein dans l'expansion du numérique dans les foyers.<br>Certains n'avaient pas forcément comme but d'être ceux qu'ils sont actuellement (comme Facebook qui initialement servait à relier les étudiants de Harvard).
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Financement d'un réseau social</h3>
        <div class="course-content">
            Un réseau social est associé à un modèle économique. De grandes sociétés financent des réseaux sociaux à des fins lucratives (pour créer des bénéfices).<br>Il existe un bon nombre de coûts liés à l'utilisation pour les particuliers de réseaux sociaux.<br><br><strong>Lister quels coûts peuvent être associés au fonctionneemnt d'un réseau social</strong><br><br>_______________________________________________________________________________________<br>______________________________________________________________________________________________________________________________________________________________________________<br><br>Ces entreprises doivent donc rémunérer ou financer toutes les fonctionnalités de leurs réseaux sociaux et cela avec diverses méthodes.<br><br><strong>Lister des méthodes de financement des réseaux sociaux</strong><br><br>_______________________________________________________________________________________<br>______________________________________________________________________________________________________________________________________________________________________________
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Contenus disponibles sur un réseau social</h3>
        <div class="course-content">
            Sur un réseau social, il existe bons nombre de contenus différents qui sont publiés pour des utilisateurs par des utilisateurs.<br><br><strong>Lister quels contenus peuvent être présents sur un réseau social</strong><br><br>______________________________________________________________________________________________________________________________________________________________________________<br><br>Les contenus sont soumis à un réglement spécifique au réseau social et même à la loi.<br>En effet,chaque utilisateur est pénalement responsable de ce qu'il poste sur un réseau social.<br>Les contenus publiés sur un réseau social sont considérés publics et à visée de tous.  <br>*Par exemple : il est strictement interdit de publier des contenus à caractères discriminatoires, diffamant et à visée de harcèlement envers autrui.*<br><br>Ces contenus peuvent être produits par des créateurs qui souhaitent partager leurs passions, des entreprises ou des magasins qui veulent étendre leur clientèle ou par des influenceurs payés par des marques pour réaliser des publicités.<br><br>### Réputation de l'utilisateur en ligne<br><br>Ces contenus (prises de parole, opinions, photos, vidéo, placements de produits) peuvent notamment affecter la réputation de l'utilisateur en ligne : on l'appelle <strong>e-reputation</strong>.<br>Elle renvoie directement à tous les utilisateurs l'image de celui qui publie du contenu en ligne.<br><br>Une bonne e-reputation permet de créer un sentiment de confiance à l'égard de l'utilisateur qui poste des contenus en ligne.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Utilisation d'un réseau social</h3>
        <div class="course-content">
            Après avoir défini ce qu'était un réseau social, comment ils fonctionnent ou comment les contenus sont régis, il faut savoir comment utiliser un réseau social.<br><br>### Pré-requis : enfants et réseaux sociaux<br><br>Avant toute chose : <strong>Un réseau social est uniquement réservé à tout individu ayant plus de 15 ans. On parle de Majorité numérique</strong>.<br><br>Avant cet âge, les réseaux sociaux sont autorisés à :  <br><br>* Refuser l'inscription des utilisateurs.<br>* Informer les enfants qui tentent une inscription et leurs parents des risques de leurs usages.<br>* Activer un dispositif de contrôle de temps.<br><br>Cela est décrit par l'article de loi du <strong>7 juillet 2023</strong> sur l'accès des réseaux sociaux par les enfants.<br><br>### Un profil pour utiliser un réseau social<br><br>Pour utiliser un réseau social, la majorité du temps il est nécessaire de se créer un <strong>profil</strong> et un <strong>compte</strong>. On parle d'<strong>inscription</strong>.<br><br>Pour créer un profil en ligne, l'utilisateur doit partager à l'entreprise qui gère le réseau social par exemple :<br><br>* Une adresse mail<br>* Un mot de passe<br>* Son identité : nom, prénom, âge, genre, voir même l'adresse<br>* Son numéro de téléphone<br>* Un pseudonyme qui permettra d'identifier l'utilisateur en ligne<br><br>![inscription](inscription.png)<br>Par exemple, voici les données nécessaires pour s'inscrire sur 𝕏 (anciennement Twitter) et Facebook.<br><br>Ces informations peuvent aussi être intéressantes pour les publicitaires pour cibler les annonces publicitaires aux utilisateurs.<br>Ces informations ne sont pas gratuites pour ces annonceurs, elles sont en général revendues par les entreprises qui gèrent les réseaux sociaux pour un certain montant d'argent.<br><br>### Sécurité de son profil en ligne<br><br>Les informations transmises à un réseau social sont confidentielles et permettent d'identifier un individu même dans le monde hors numérique.<br>Pour les sécuriser, il faut pouvoir rendre l'accès aux pirates informatiques impossible ou très complexes car elles peuvent fuiter lors de grands piratages des bases de données.<br><br>Pour se faire, on ne peut pas forcément sécuriser son adresse-mail, on va donc jouer sur le mot de passe.<br><br>On dit qu'un mot de passe est <strong>robuste</strong> s'il est compliqué à retrouver lors d'une recherche exhaustive. Une <strong>recherche exhaustive</strong> correspond à une recherche où l'on teste toutes les combinaisons possibles de caractères.<br><br>En général, il est conseillé pour rendre robuste un mot de passe qu'il réponde à ces critères :<br><br>* Au moins 10 caractères<br>* Contient des minuscules et des majuscules<br>* Contient des chiffres<br>* Contient des caractères spéciaux (! ? ; @ # & etc...)<br><br>Certains sites internet permettent d'observer la robustesse d'un mot de passe : [testeur de mots de passe](https://www.passwordmonster.com)<br><br><strong>Activité :</strong><br><strong>Tester les mots de passe suivant sur le site internet de test de mots de passe.</strong><br><br>* <strong>JeSuisUnRenardQuiCourtDanslaForet</strong><br>* <strong>Ren4rDFor3|</strong>  <br><br><strong>Que peut-on en déduire?</strong><br><br>_______________________________________________________________________________________<br>______________________________________________________________________________________________________________________________________________________________________________<br><br>À l'issue de la création de compte, l'utilisateur doit se connecter.<br>Pour se faire, il doit renseigner à minima son adresse mail et son mot de passe dans des champs qui sont spécialement choisis.<br>On nomme cette étape <strong>l'authentification</strong>.
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Les fils d'actualité et les messages privés</h3>
        <div class="course-content">
            Dans tous les réseaux sociaux, tous les utilisateurs peuvent discuter par divers moyens : fils d'actualités, messages privés, groupes privés ou publics.<br>Comme énoncé au début de ce cours, tous les utilisateurs sont responsables de leurs mots et de leurs contenus sur les divers réseaux sociaux.<br><br>Le fait de harceler sur internet nommé <strong>cyber-harcèlement</strong> est répréhensible par la loi. On parle de l'article 222-33-2-2 du code pénal.<br><br>!!! Danger<br>    Le fait de harceler une personne par des propos ou comportements répétés ayant pour objet ou pour effet une dégradation de ses conditions de vie se traduisant par une altération de sa santé physique ou mentale est puni d'un an d'emprisonnement et de 15 000 € d'amende lorsque ces faits ont causé une incapacité totale de travail inférieure ou égale à huit jours ou n'ont entraîné aucune incapacité de travail.<br>    <strong>...</strong><br>    4° Lorsqu'ils ont été commis par l'utilisation d'un service de communication au public en ligne ou par le biais d'un support numérique ou électronique ;<br><br>Il existe différentes formes de <strong>cyberviolence</strong>.<br><br><strong>Définir ces différentes formes de cyberviolences :</strong><br><br>* Harcèlement en ligne<br>* Discrimination en ligne<br>* Usurpation d'identité<br>* Diffamation<br>* Cyberintimidation<br><br>Il existe diverses ressources disponibles pour lutter contre les cyber-violences comme la plateforme <strong>Pharos</strong>. Elle permet de réaliser des signalements pour des contenus illicites ou illégaux publiés sur les réseaux sociaux.<br>Si vous êtes vous même victime de cyber-harcèlement, vous pouvez contacter le <strong>3018</strong> qui est le numéro national contre le harcèlement en ligne.<br><br>La cyberviolence est un des plus grands enjeux de notre société car celle-ci est omniprésente. Il est important de savoir l'identifier et de savoir comment lutter contre celle-ci.<br><br><strong>Activité : activité Pix sur les réseaux sociaux</strong>
        </div>
    </div>
    
    <div class="course-card definition">
        <div class="badge definition">📖 Définition</div>
        <h3 class="course-title">Proximité des utilisateurs : Notion de Graphe et expérience de Milgram</h3>
        <div class="course-content">
            Précédemment, on parlait d'un réseau social comme étant une manière de relier les personnes dans le monde.<br><br>### Les Graphes<br><br>Il existe un modèle mathématique pour représenter ce genre de situation, on appelle cela des <strong>graphes</strong>.<br><br>Un graphe correspond à un ensemble de noeuds que l'on relie pour simuler ou représenter graphiquement des liens entre des individus ou des machines par exemple.<br><br>Il existe plusieurs types de graphes qui correspondent à des situations particulières :<br><br>- Les graphes dits <strong>non orientés</strong> sont des graphes dans lesquels des noeuds appelés <strong>sommets</strong> sont reliés par des arêtes. Ce genre de graphe représente notamment les amitiés sur Facebook car celles-ci sont dites <strong>réflexives</strong> (si A est ami avec B, alors B est ami avec A).<br>- Les graphes dit <strong>orientés</strong> sont des graphes dans lesquels des <strong>sommets</strong> sont reliés par des <strong>arcs</strong> qui représentent une direction. Ce genre de graphe représente notamment les liens de *follow* sur Twitter.<br><br><strong>Indiquer sur le dessin ci-dessous, quel graphe est orienté et lequel est non orienté.</strong><br>![rs](rs.png)<br><br><strong>Vous avez un groupe de 6 amis : Alice, Bob, Charlie, David, Emma et Frank. Vous devez modéliser leurs amitiés en utilisant un graphe. Un graphe est constitué de sommets (les personnes) et d’arêtes (les relations d’amitié). Voici les informations sur leurs amitiés :</strong><br><br>- Alice est amie avec Bob, Charlie et Emma.<br>- Bob est ami avec Alice, David et Frank.<br>- Charlie est ami avec Alice et Emma.<br>- David est ami avec Bob et Frank.<br>- Emma est amie avec Alice et Charlie.<br>- Frank est ami avec Bob et David.<br><br>#### Définitions sur les Graphes<br><br>On a vu précédement que ces graphes pouvaient modéliser des situations de la vie réelle.<br>Pour ce faire, on dispose de quelques propriétés sur les graphes.<br><br><strong>Le centre d'un graphe</strong> est le sommet (ou le groupe de sommets) étant relié à tous les autres par une distance minimale.<br><br><strong>Le rayon d'un graphe</strong> correspond à la plus petite distance entre un sommet qui est le centre et les sommets les plus excentrés.<br><br><strong>Le diamètre d'un graphe</strong> correspond à la plus petite distance reliant deux sommets excentrés (comme pour un cercle).<br><br>Dans notre situation des réseaux sociaux, le centre d'un graphe correspondant est la personne qui est amie avec le plus de personnes par exemple.<br><br><strong>Activité</strong><br><br>* À l'aide du graphe de l'exercice précédent, donner le centre du graphe (c'est à dire la personne qui a le plus d'amis).<br><br>* Donner un rayon de ce graphe, donner sa longueur.<br><br>* En déduire un diamètre de ce graphe, donner sa longueur.<br><br><br>### Petit monde de Milgram<br><br>Quel est le lien entre les graphes et les réseaux sociaux hormis la représentation mathématiques?<br>On a vu précédement qu'il existe des chemins entre les utilisateurs qui représentent le nombre de personnes dont un utilisateur A a besoin pour contacter un utilisateur B.<br><br>Cela a été étudié en 1963 par Stanley Milgram. En effet, il a déterminé qu'il fallait au maximum 6 poignées de mains pour connaître n'importe qui dans le monde.<br><br>Par exemple, comment pourriez-vous contacter de manière directe notre président de la République ?<br><br>Vous aurez besoin de plusieurs intermédiaires :<br><br>![milgram](g_milgram.png)<br><br><strong>Activité : Trouvez un chemin entre vous et Bill Gates, le directeur de Microsoft.</strong>
        </div>
    </div>
    
</div>
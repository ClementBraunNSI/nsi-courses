<style>
/* Styles modernes B1 – alignés avec Chemin Critique, Gestion de Projet, Gestion des Risques, ITIL */
.course-header {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(52, 152, 219, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.concept-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 1.5rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05));
    border-left: 5px solid #3498db;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #3498db;
    margin-bottom: 0.8rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.05rem;
    line-height: 1.6;
}

.content-text {
    color: var(--md-default-fg-color);
    line-height: 1.7;
    margin: 1.2rem 0;
    font-size: 1.05rem;
}

.highlight-fact {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.warning-fact {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f1c40f;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.scenario-box {
    background: rgba(241, 196, 15, 0.1);
    border-left: 4px solid #f39c12;
    border-radius: 8px;
    padding: 1.2rem;
    margin: 1rem 0;
}

.exercise-container {
    background: white;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border-left: 5px solid #3498db;
}

.exercise-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2980b9;
    margin-bottom: 1rem;
}

/* Titres H3 stylisés (pour sous-sections) */
h3.subsection-title {
    font-size: 1.6rem;
    font-weight: 600;
    color: #3498db;
    margin: 1.5rem 0 0.8rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid rgba(52, 152, 219, 0.25);
}

/* Titres H4 stylisés (pour sous-sous-sections) */
h4.subsubsection-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 1.2rem 0 0.6rem 0;
    padding-bottom: 0.3rem;
    border-bottom: 1px dashed rgba(44, 62, 80, 0.3);
}

.exercise-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.85);
    border-radius: 8px;
    overflow: hidden;
}
.exercise-table th, .exercise-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(52, 152, 219, 0.2);
}
.exercise-table th {
    background: rgba(52, 152, 219, 0.2);
    font-weight: 600;
    color: #2c3e50;
}
</style>

<div class="course-header">
  <h1 class="course-title">⚖️ RGPD & CNIL</h1>
  <p class="course-subtitle">Politique de collecte et protection des données personnelles</p>
</div>

<div class="concept-section">
  <h2 class="section-title">1. Comprendre le cadre légal</h2>

  <h3 class="subsection-title">1.1 Qu'est-ce que le RGPD ?</h3>
  <div class="definition-box">
    <div class="definition-title">RGPD (Règlement Général sur la Protection des Données)</div>
    <div class="definition-content">
      Texte réglementaire européen entré en vigueur le <strong>25 mai 2018</strong>. Il encadre le traitement des données personnelles sur tout le territoire de l'Union Européenne.
      <br><br>
      <strong>Objectifs :</strong>
      <ul>
        <li>Redonner aux citoyens le contrôle de leurs données personnelles.</li>
        <li>Responsabiliser les acteurs (entreprises, associations, administration).</li>
        <li>Unifier la réglementation à travers l'Europe (marché unique numérique).</li>
      </ul>
    </div>
  </div>

  <h4 class="subsubsection-title">Notions clés</h4>
  <div class="definition-box">
    <div class="definition-title">Donnée Personnelle</div>
    <div class="definition-content">
      Toute information se rapportant à une personne physique identifiée ou identifiable :
      <ul>
        <li><strong>Directement</strong> : Nom, Prénom, Email nominatif.</li>
        <li><strong>Indirectement</strong> : Numéro de téléphone, Plaque d'immatriculation, Numéro Sécurité Sociale, Identifiant client.</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Traitement de données</div>
    <div class="definition-content">
      Toute opération effectuée sur des données personnelles, quel que soit le procédé utilisé (automatisé ou papier) : collecte, enregistrement, organisation, conservation, modification, extraction, consultation, utilisation, communication, diffusion, effacement ou destruction.
      <br><em>Exemple : Un simple fichier Excel avec des noms de clients EST un traitement.</em>
    </div>
  </div>

  <div class="warning-fact">
    🌍 <strong>Portée territoriale (Extraterritorialité)</strong> : Le RGPD s'applique à toute organisation établie dans l'UE, mais aussi aux organisations <strong>hors UE</strong> si elles ciblent des résidents européens (offre de biens/services ou suivi de comportement).
  </div>

  <div class="warning-fact">
    ⚠️ <strong>Données Sensibles</strong> : Le traitement de certaines données est par principe <strong>INTERDIT</strong> (sauf exceptions strictes) : origine ethnique, opinions politiques, convictions religieuses, appartenance syndicale, données génétiques, biométriques, de santé ou concernant la vie sexuelle.
  </div>

  <h3 class="subsection-title">1.2 La CNIL : Le régulateur français</h3>
  <div class="definition-box">
    <div class="definition-title">Qu'est-ce que la CNIL ?</div>
    <div class="definition-content">
      La <strong>Commission Nationale de l'Informatique et des Libertés</strong> est une <strong>Autorité Administrative Indépendante (AAI)</strong> créée par la loi Informatique et Libertés du 6 janvier 1978. Elle est le régulateur des données personnelles en France. Elle agit au nom de l'État mais sans être soumise à l'autorité du gouvernement.
    </div>
  </div>

  <h4 class="subsubsection-title">Les 4 missions principales</h4>
  <div class="content-text">
    La CNIL remplit 4 missions essentielles pour la protection des données :
    <ul>
      <li><strong>1. Informer et protéger les droits :</strong> Elle répond aux demandes des particuliers, reçoit les plaintes (plus de 14 000 par an) et aide les citoyens à exercer leurs droits.</li>
      <li><strong>2. Accompagner la conformité :</strong> Elle aide les entreprises et organismes publics à se mettre en conformité via des boîtes à outils, des référentiels sectoriels, des guides pratiques et des labels.</li>
      <li><strong>3. Anticiper et innover :</strong> Elle mène une veille technologique (via le <em>LINC</em>, son laboratoire d'innovation) pour évaluer les conséquences des nouvelles technologies (IA, smartphones, objets connectés) sur la vie privée.</li>
      <li><strong>4. Contrôler et sanctionner :</strong> Elle vérifie le respect de la loi sur le terrain ou en ligne et peut punir les infractions constatées.</li>
    </ul>
  </div>

  <h4 class="subsubsection-title">Les pouvoirs de contrôle</h4>
  <div class="content-text">
    La CNIL effectue plusieurs centaines de contrôles par an pour vérifier la conformité des organismes.
  </div>
  <div class="definition-box">
    <div class="definition-title">Types de contrôles</div>
    <div class="definition-content">
      <ul>
        <li><strong>Contrôle en ligne :</strong> Vérification à distance depuis les locaux de la CNIL (cookies, mentions légales, formulaires web).</li>
        <li><strong>Contrôle sur pièces :</strong> Échanges de courriers et demandes de documents (registres, contrats de sous-traitance).</li>
        <li><strong>Contrôle sur place :</strong> Visite inopinée ou programmée dans les locaux de l'entreprise (accès aux serveurs, audition du personnel).</li>
        <li><strong>Audition :</strong> Convocation des responsables à la CNIL.</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">1.3 Les acteurs clés</h3>
  
  <div class="definition-box">
    <div class="definition-title">Responsable de Traitement (RT)</div>
    <div class="definition-content">
      C'est la personne (morale ou physique), l'autorité publique ou l'organisme qui <strong>détermine les finalités et les moyens</strong> du traitement.
      <br><strong>Missions principales :</strong>
      <ul>
        <li>Assurer la conformité globale au RGPD.</li>
        <li>Mettre en œuvre les mesures de sécurité appropriées.</li>
        <li>Répondre aux demandes d'exercice de droits.</li>
        <li>Notifier les violations de données à la CNIL.</li>
      </ul>
      <br><em>Exemple : Une entreprise qui gère la paie de ses salariés est RT.</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Sous-traitant (ST)</div>
    <div class="definition-content">
      C'est la personne ou l'organisme qui traite des données <strong>pour le compte et sur instruction</strong> du responsable de traitement.
      <br><strong>Missions principales :</strong>
      <ul>
        <li>Ne traiter les données que sur instruction documentée du RT.</li>
        <li>Garantir la confidentialité et la sécurité des données.</li>
        <li>Aider le RT à respecter ses obligations (sécurité, AIPD, droits des personnes).</li>
        <li>Supprimer ou renvoyer les données à la fin du contrat.</li>
      </ul>
      <br><em>Exemple : Un hébergeur web, un service cloud, un cabinet comptable externe.</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">Délégué à la Protection des Données (DPO)</div>
    <div class="definition-content">
      Le "pilote" de la conformité. Sa désignation est <strong>obligatoire</strong> pour les organismes publics et ceux traitant des données sensibles ou faisant du suivi régulier à grande échelle.
      <br><strong>Missions principales :</strong>
      <ul>
        <li><strong>Informer et conseiller</strong> le RT et les employés.</li>
        <li><strong>Contrôler</strong> le respect du RGPD (audits internes).</li>
        <li>Être le <strong>point de contact</strong> avec la CNIL et les personnes concernées.</li>
        <li>Il doit être indépendant et ne pas avoir de conflit d'intérêts (ex: le DSI ne peut pas être DPO car il définit les moyens techniques).</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">2. Les Principes Fondamentaux</h2>
  <div class="content-text">Pour être conforme, tout traitement de données doit respecter 6 grands principes (plus le principe de responsabilité).</div>

  <div class="definition-box">
    <div class="definition-title">1. Licéité, Loyauté, Transparence</div>
    <div class="definition-content">
      Le traitement doit avoir une base légale, ne pas tromper les personnes et être expliqué clairement.
      <br><em>Exemple : Ne pas collecter d'emails sous prétexte d'un jeu-concours pour les revendre ensuite sans le dire.</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">2. Limitation des finalités</div>
    <div class="definition-content">
      Les données sont collectées pour un but précis, légitime et déterminé. Pas de réutilisation incompatible ("détournement de finalité").
      <br><em>Exemple : Les caméras de vidéosurveillance d'un magasin sont là pour la sécurité, pas pour surveiller la productivité des employés.</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">3. Minimisation des données</div>
    <div class="definition-content">
      Ne collecter que les données <strong>strictement nécessaires</strong> à l'objectif visé.
      <br><em>Exemple : Ne pas demander le numéro de Sécurité Sociale pour une carte de fidélité de supermarché.</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">4. Exactitude</div>
    <div class="definition-content">
      Les données doivent être exactes et tenues à jour. Les données incorrectes doivent être corrigées ou effacées.
      <br><em>Exemple : Si un client déménage et signale sa nouvelle adresse, l'entreprise doit mettre à jour sa base et ne plus envoyer de courrier à l'ancienne.</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">5. Limitation de la conservation</div>
    <div class="definition-content">
      Les données ne peuvent pas être conservées indéfiniment. Une <strong>durée de conservation</strong> doit être définie (ex: durée du contrat + prescription légale).
      <br><em>Exemple : Les CV des candidats non retenus doivent être supprimés après 2 ans (sauf accord contraire).</em>
    </div>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">6. Intégrité et Confidentialité</div>
    <div class="definition-content">
      Le responsable doit garantir la sécurité des données (protection contre le vol, la perte, l'accès non autorisé).
      <br><em>Exemple : Les dossiers médicaux à l'hôpital ne doivent être accessibles qu'aux soignants, pas à l'administration ou aux visiteurs.</em>
    </div>
  </div>

  <div class="warning-fact">
    🚨 <strong>Accountability</strong> (Responsabilité) : L'entreprise doit être capable de <strong>prouver</strong> à tout moment sa conformité (documentation, registres, procédures). On passe d'une logique de formalités préalables à une logique de responsabilité continue.
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">3. Les Bases Légales</h2>
  <div class="content-text">
    Pour qu'un traitement soit licite, il doit <strong>obligatoirement</strong> se fonder sur l'une des 6 bases légales prévues par l'article 6 du RGPD. C'est la première question à se poser : "De quel droit je traite ces données ?"
  </div>
  
  <div class="definition-box">
    <div class="definition-title">1. Le Consentement (Art. 6.1.a)</div>
    <div class="definition-content">
      La personne a donné son accord clair pour une finalité spécifique.
      <br><strong>Exemple :</strong> S'abonner à une newsletter, accepter les cookies de publicité ciblée.
      <br><em>Nota : Le consentement doit pouvoir être retiré aussi facilement qu'il a été donné.</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">2. Le Contrat (Art. 6.1.b)</div>
    <div class="definition-content">
      Le traitement est nécessaire à l'exécution ou à la préparation d'un contrat avec la personne.
      <br><strong>Exemple :</strong> Un site e-commerce a besoin de l'adresse pour livrer un colis. Une banque a besoin des revenus pour accorder un prêt.
      <br><em>Pas besoin de demander le consentement ici, car sans données, pas de service !</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">3. L'Obligation Légale (Art. 6.1.c)</div>
    <div class="definition-content">
      Le traitement est imposé par la loi (française ou européenne).
      <br><strong>Exemple :</strong> Un employeur doit déclarer les salaires à l'URSSAF. Une banque doit vérifier l'identité pour lutter contre le blanchiment.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">4. La Sauvegarde des Intérêts Vitaux (Art. 6.1.d)</div>
    <div class="definition-content">
      Nécessaire pour protéger la vie de la personne concernée ou d'une autre personne physique.
      <br><strong>Exemple :</strong> Un hôpital accède au dossier médical d'un patient inconscient arrivé aux urgences après un accident.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">5. La Mission d'Intérêt Public (Art. 6.1.e)</div>
    <div class="definition-content">
      Nécessaire à l'exécution d'une mission d'intérêt public ou relevant de l'autorité publique.
      <br><strong>Exemple :</strong> La gestion des impôts par la DGFIP, la gestion des étudiants par une université publique.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">6. L'Intérêt Légitime (Art. 6.1.f)</div>
    <div class="definition-content">
      Nécessaire aux intérêts de l'organisme, à condition de ne pas déséquilibrer les droits fondamentaux des personnes.
      <br><strong>Exemple :</strong> Une entreprise installe des caméras pour sécuriser ses locaux (son intérêt) sans filmer les postes de travail (droits des employés). La lutte contre la fraude à la carte bancaire.
      <br><em>Attention : C'est la base la plus complexe, elle nécessite souvent une "mise en balance" des intérêts.</em>
    </div>
  </div>

  <h3 class="subsection-title">Le Consentement valide</h3>
  <div class="content-text">Pour être valide, le consentement doit être :</div>
  <ul>
    <li><strong>Libre</strong> : Pas de contrainte ni de conséquence négative en cas de refus.</li>
    <li><strong>Spécifique</strong> : Un consentement par finalité.</li>
    <li><strong>Éclairé</strong> : La personne sait à quoi elle consent.</li>
    <li><strong>Univoque</strong> : Acte positif clair (case à cocher, clic). Pas de case pré-cochée !</li>
  </ul>
</div>

<div class="concept-section">
  <h2 class="section-title">4. Les Droits des Personnes</h2>
  <div class="content-text">
    Le RGPD renforce les droits des citoyens sur leurs données. Chaque personne (salarié, client, usager) dispose de droits qu'elle peut exercer à tout moment auprès du responsable de traitement.
  </div>
  
  <div class="definition-box">
    <div class="definition-title">1. Droit d'accès (Art. 15)</div>
    <div class="definition-content">
      Toute personne peut demander à un organisme s'il détient des données sur elle et, si oui, en obtenir une copie lisible.
      <br><em>Cela permet de vérifier l'exactitude des données.</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">2. Droit de rectification (Art. 16)</div>
    <div class="definition-content">
      Permet de corriger des données inexactes ou de compléter des données incomplètes.
      <br><em>Exemple : Corriger une erreur dans l'orthographe d'un nom ou mettre à jour une adresse.</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">3. Droit à l'effacement ("Droit à l'oubli" - Art. 17)</div>
    <div class="definition-content">
      Permet de demander la suppression de ses données.
      <br><strong>Attention, ce n'est pas un droit absolu !</strong> On ne peut pas demander l'effacement si le traitement est nécessaire (ex: pour payer des impôts, pour exécuter un contrat en cours).
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">4. Droit à la limitation du traitement (Art. 18)</div>
    <div class="definition-content">
      Permet de "geler" l'utilisation des données temporairement (par exemple, le temps de vérifier leur exactitude suite à une contestation).
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">5. Droit à la portabilité (Art. 20)</div>
    <div class="definition-content">
      Permet de récupérer ses données dans un format structuré et lisible par machine (ex: CSV, XML) pour les transmettre à un autre organisme.
      <br><em>Exemple : Changer d'opérateur téléphonique ou de plateforme de streaming musical en gardant son historique.</em>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">6. Droit d'opposition (Art. 21)</div>
    <div class="definition-content">
      Permet de refuser qu'un organisme utilise ses données pour un objectif précis.
      <br><strong>Absolu pour la prospection commerciale :</strong> On peut toujours s'opposer à recevoir de la pub, sans justification.
      <br><strong>Sous conditions pour les autres cas :</strong> Il faut un motif légitime (sauf si le traitement est d'intérêt public).
    </div>
  </div>
  
  <div class="highlight-fact">
    ⏱️ <strong>Délais et Modalités</strong> :
    <ul>
      <li>Le responsable doit répondre dans un délai de <strong>1 mois</strong> (prolongeable de 2 mois si complexe).</li>
      <li>L'exercice des droits doit être <strong>gratuit</strong> pour le demandeur.</li>
      <li>En cas de refus, le responsable doit motiver sa décision et informer des voies de recours (CNIL).</li>
    </ul>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">5. Obligations et Conformité</h2>
  
  <h3 class="subsection-title">5.1 Le Registre des activités de traitement</h3>
  <div class="content-text">
    C'est le document central de la conformité. Il recense tous les traitements effectués par l'organisme (Qui ? Quoi ? Pourquoi ? Combien de temps ? Sécurité ?). Il est obligatoire pour la plupart des entreprises.
  </div>

  <h3 class="subsection-title">5.2 L'Analyse d'Impact (AIPD / DPIA)</h3>
  <div class="content-text">
    Obligatoire pour les traitements à <strong>risque élevé</strong> pour les droits et libertés (ex: données de santé, surveillance systématique, profilage). C'est une étude qui vise à identifier les risques et les mesures pour les atténuer.
  </div>

  <h3 class="subsection-title">5.3 Notification des violations</h3>
  <div class="warning-fact">
    En cas de fuite de données (vol, perte, accès non autorisé), le responsable doit notifier la CNIL dans les <strong>72 heures</strong>. Si le risque est élevé pour les personnes, il faut aussi les informer individuellement.
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">6. Sécurité et Concepts Avancés</h2>

  <h3 class="subsection-title">Privacy by Design & by Default</h3>
  <div class="definition-box">
    <div class="definition-title">Privacy by Design (Protection dès la conception)</div>
    <div class="definition-content">La protection des données doit être intégrée dès le début du projet informatique, et non ajoutée à la fin comme une "verrue".</div>
  </div>
  <div class="definition-box">
    <div class="definition-title">Privacy by Default (Protection par défaut)</div>
    <div class="definition-content">Par défaut, le système doit offrir le plus haut niveau de protection (ex: case non cochée, profil privé par défaut sur un réseau social).</div>
  </div>

  <h3 class="subsection-title">Sécurité des données</h3>
  <div class="content-text">
    Le RGPD impose des mesures techniques et organisationnelles appropriées :
    <ul>
      <li><strong>Pseudonymisation</strong> : Remplacer les identifiants par des codes.</li>
      <li><strong>Chiffrement</strong> : Rendre les données illisibles sans clé.</li>
      <li><strong>Sauvegardes</strong> : Garantir la disponibilité.</li>
      <li><strong>Tests réguliers</strong> de vulnérabilité.</li>
      <li><strong>Contrôle d'accès</strong> : Authentification forte et gestion des droits.</li>
    </ul>
  </div>

  <h3 class="subsection-title">Mesures organisationnelles</h3>
  <div class="definition-box">
    <div class="definition-title">Politique et Humain</div>
    <div class="definition-content">
      La sécurité n'est pas que technique, elle est aussi humaine :
      <ul>
        <li><strong>Charte informatique</strong> : Règles d'utilisation des outils.</li>
        <li><strong>Sensibilisation</strong> : Formation régulière du personnel (phishing, mots de passe).</li>
        <li><strong>Gestion des départs</strong> : Suppression immédiate des accès.</li>
        <li><strong>Clauses de confidentialité</strong> dans les contrats de travail.</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">7. Transferts de données hors UE</h2>
  <div class="content-text">
    Le transfert de données personnelles en dehors de l'Union Européenne est par principe interdit, sauf exceptions encadrées.
  </div>

  <h3 class="subsection-title">7.1 Encadrement des transferts</h3>
  <div class="definition-box">
    <div class="definition-title">Pays à niveau de protection adéquat</div>
    <div class="definition-content">
      La Commission Européenne reconnaît que certains pays offrent un niveau de protection équivalent à celui de l'UE (ex: Suisse, Japon, Canada - secteur commercial). Les transferts vers ces pays sont libres.
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Garanties appropriées</div>
    <div class="definition-content">
      Pour les autres pays, il faut mettre en place des outils juridiques :
      <ul>
        <li><strong>BCR (Binding Corporate Rules)</strong> : Règles internes d'entreprise pour les groupes multinationaux.</li>
        <li><strong>Clauses Contractuelles Types (CCT)</strong> : Modèles de contrats rédigés par la Commission Européenne.</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">7.2 Cas particuliers</h3>
  <div class="content-text">
    <ul>
      <li><strong>États-Unis</strong> : Le "Data Privacy Framework" facilite les échanges avec les entreprises américaines certifiées.</li>
      <li><strong>Cloud Computing</strong> : Attention à la localisation des serveurs (AWS, Azure, Google Cloud). Héberger des données sensibles hors UE nécessite une vigilance accrue.</li>
    </ul>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">8. Sanctions</h2>
  <div class="content-text">
    La CNIL dispose d'un pouvoir de sanction dissuasif. Les amendes peuvent aller jusqu'à :
  </div>
  <div class="warning-fact">
    💰 <strong>10 millions d'euros</strong> ou <strong>2% du CA mondial</strong> (manquements administratifs).<br>
    💰 <strong>20 millions d'euros</strong> ou <strong>4% du CA mondial</strong> (violation des droits, principes fondamentaux).
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">9. Cas pratiques et applications</h2>

  <h3 class="subsection-title">9.1 Politique de confidentialité</h3>
  <div class="content-text">
    Document obligatoire sur tout site web collectant des données. Elle doit être :
    <ul>
      <li><strong>Accessible</strong> depuis toutes les pages (footer).</li>
      <li><strong>Compréhensible</strong> (langage clair, pas de jargon juridique).</li>
      <li><strong>Complète</strong> (finalités, destinataires, durée, droits).</li>
    </ul>
  </div>

  <h3 class="subsection-title">9.2 Gestion des cookies</h3>
  <div class="definition-box">
    <div class="definition-title">Bandeau Cookies</div>
    <div class="definition-content">
      <ul>
        <li>Le dépôt de cookies non essentiels (pub, réseaux sociaux) nécessite un <strong>consentement préalable</strong>.</li>
        <li>Boutons obligatoires : "Tout accepter", "Tout refuser", "Personnaliser".</li>
        <li>Il doit être aussi facile de refuser que d'accepter.</li>
        <li>Durée de validité du choix : 6 mois recommandé.</li>
      </ul>
    </div>
  </div>
</div>

<div class="exercise-container">
  <div class="exercise-title">📝 Cas Pratique : Le formulaire de contact</div>
  <div class="content-text">
    Vous développez un formulaire de contact pour un site vitrine. Analysez les éléments suivants :
  </div>
  
  <table class="exercise-table">
    <tr>
      <th>Élément</th>
      <th>Conforme RGPD ?</th>
      <th>Correction / Explication</th>
    </tr>
    <tr>
      <td>Champ "Nom" (Obligatoire)</td>
      <td>✅ OUI</td>
      <td>Nécessaire pour répondre (Minimisation).</td>
    </tr>
    <tr>
      <td>Champ "Date de naissance" (Obligatoire)</td>
      <td>❌ NON</td>
      <td>Inutile pour une simple prise de contact (Minimisation).</td>
    </tr>
    <tr>
      <td>Case pré-cochée : "Je veux recevoir la newsletter"</td>
      <td>❌ NON</td>
      <td>Le consentement doit être un acte positif. La case doit être vide par défaut.</td>
    </tr>
    <tr>
      <td>Mention : "Vos données sont conservées 3 ans après le dernier contact"</td>
      <td>✅ OUI</td>
      <td>Durée de conservation définie et transparente.</td>
    </tr>
    <tr>
      <td>Lien vers la "Politique de confidentialité"</td>
      <td>✅ OUI</td>
      <td>Obligation de transparence (Information).</td>
    </tr>
  </table>
</div>

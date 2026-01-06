<style>
.course-header { background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 3rem; margin: 2rem 0; border: 1px solid rgba(52, 152, 219, 0.2); text-align: center; }
.course-title { font-size: 3rem; font-weight: 700; background: linear-gradient(135deg, #3498db 0%, #9b59b6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
.course-subtitle { color: #7f8c8d; font-size: 1.2rem; font-weight: 300; margin-bottom: 2rem; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 2rem; margin: 2rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }
.section-title { font-size: 2.2rem; font-weight: 600; color: #3498db; margin-bottom: 1.5rem; text-align: center; }
.definition-box { background: linear-gradient(135deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.05)); border-left: 5px solid #3498db; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; backdrop-filter: blur(10px); }
.definition-title { font-size: 1.2rem; font-weight: 600; color: #3498db; margin-bottom: 0.8rem; }
.definition-content { color: var(--md-default-fg-color); font-size: 1.05rem; line-height: 1.6; }
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1.2rem 0; font-size: 1.05rem; }
.highlight-fact { background: rgba(46, 204, 113, 0.1); border-left: 4px solid #2ecc71; padding: 1rem; margin: 1rem 0; border-radius: 8px; font-weight: 500; }
.exercise-container { background: white; border-radius: 15px; padding: 1.5rem; margin: 1.5rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border-left: 5px solid #3498db; }
.exercise-title { font-size: 1.4rem; font-weight: 600; color: #2980b9; margin-bottom: 1rem; }
.exercise-table { width: 100%; border-collapse: collapse; margin: 1rem 0; background: rgba(255, 255, 255, 0.85); border-radius: 8px; overflow: hidden; }
.exercise-table th, .exercise-table td { padding: 0.8rem; text-align: left; border: 1px solid rgba(52, 152, 219, 0.2); }
.exercise-table th { background: rgba(52, 152, 219, 0.2); font-weight: 600; color: #2c3e50; }
@media (max-width: 768px) { .course-title { font-size: 2rem; } .course-header { padding: 2rem; } }
</style>

<div class="course-header">
  <h1 class="course-title">📑 Activité pratique : RGPD et Mentions Légales</h1>
  <p class="course-subtitle">BTS SIO 1 • B3 Cybersécurité • Durée : 2 heures</p>
</div>

<div class="concept-section">
  <h2 class="section-title">📦 Contexte</h2>
  <div class="definition-box">
    <div class="definition-title">Projet client</div>
    <div class="definition-content">
      Vous travailez en tant que consultants en conformité numérique. Votre client, l'association <strong>Le Refuge des Renards Polaires</strong>, souhaite lancer un site e-commerce pour vendre des produits dérivés (mugs, t-shirts, peluches, stickers) afin de financer ses activités de protection des renards.
      <br/><br/>
      Le site doit être conforme au RGPD et aux obligations légales françaises avant sa mise en ligne.
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🧾 Informations sur le client</h2>
  <div class="definition-box">
    <div class="definition-title">Identité et hébergeur</div>
    <div class="definition-content content-text">
      <ul>
        <li><strong>Nom :</strong> Le Refuge des Renards Polaires</li>
        <li><strong>Statut juridique :</strong> Association loi 1901</li>
        <li><strong>Siège social :</strong> Port-aux-Français, 98417 Îles Kerguelen, TAAF, France</li>
        <li><strong>Email :</strong> contact@refugedesrenards.fr</li>
        <li><strong>Téléphone :</strong> +262 984 00 01 23</li>
        <li><strong>N° SIRET :</strong> 123 456 789 00012</li>
        <li><strong>Directeur de publication :</strong> Marie Dubois (Présidente de l'association)</li>
        <li><strong>Hébergeur :</strong> OVH — 2 rue Kellermann, 59100 Roubaix</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Données collectées</div>
    <div class="definition-content content-text">
      <ul>
        <li>Nom et prénom</li>
        <li>Adresse email</li>
        <li>Adresse postale (livraison et facturation)</li>
        <li>Numéro de téléphone (optionnel)</li>
        <li>Données de paiement (traitées par Stripe, prestataire externe)</li>
        <li>Consentement pour la newsletter (optionnel)</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Finalités des traitements</div>
    <div class="definition-content content-text">
      <ul>
        <li>Gestion des commandes et livraisons</li>
        <li>Facturation</li>
        <li>Service client</li>
        <li>Newsletter (si consentement)</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Durées de conservation</div>
    <div class="definition-content content-text">
      <ul>
        <li>Données de commande : 3 ans après la dernière commande</li>
        <li>Newsletter : jusqu'à désinscription</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">🎯 Mission</h2>
  <div class="definition-box">
    <div class="definition-title">Phase 1 — Recherche et documentation</div>
    <div class="definition-content content-text">
      Travail en binôme. Effectuez des recherches pour identifier et documenter :
      <ul>
        <li>Les éléments obligatoires dans des mentions légales pour un site e-commerce d'une association</li>
        <li>Les éléments obligatoires dans une politique de confidentialité conforme au RGPD</li>
        <li>Qu'est-ce que la CNIL ? Amendes et peines.</li>
      </ul>
    </div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Phase 2 — Analyse comparative de sites web</div>
    <div class="definition-content content-text">
      Travail en binôme. Analysez les mentions légales et politiques de confidentialité des sites suivants (ou équivalents) :
      <ul>
        <li>Un site e-commerce : <a href="https://www.fnac.com" target="_blank">fnac.com</a> (ou Amazon.fr, Cdiscount.com, Boulanger.com)</li>
        <li>Une landing page d'artiste : <a href="https://www.bmthofficial.com" target="_blank">Bring Me The Horizon</a> (ou Orelsan, Stromae)</li>
        <li>Un site d'association : <a href="https://www.croix-rouge.fr" target="_blank">croix-rouge.fr</a> (ou Secours Populaire, WWF France)</li>
      </ul>
    </div>
  </div>

  <div class="exercise-container">
    <div class="exercise-title">Tableau d'analyse comparatif</div>
    <table class="exercise-table">
      <thead>
        <tr>
          <th>Critères</th>
          <th>Site e-commerce</th>
          <th>Landing page artiste</th>
          <th>Site association</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Nom du site analysé</td><td></td><td></td><td></td></tr>
        <tr><td>Mentions légales présentes ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Identité éditeur complète ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Hébergeur mentionné ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Directeur de publication ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Politique de confidentialité ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Finalités des traitements ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Droits des utilisateurs RGPD ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Durée de conservation ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Gestion des cookies</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Bandeau cookies présent ?</td><td>Oui / Non</td><td>Oui / Non</td><td>Oui / Non</td></tr>
        <tr><td>Conformité globale</td><td>Conforme / Non conforme / Partiellement</td><td>Conforme / Non conforme / Partiellement</td><td>Conforme / Non conforme / Partiellement</td></tr>
        <tr><td>Points forts</td><td></td><td></td><td></td></tr>
        <tr><td>Points faibles ou manquants</td><td></td><td></td><td></td></tr>
      </tbody>
    </table>
    <div class="highlight-fact">Livrable de la Phase 2 : Tableau comparatif complété avec vos observations.</div>
  </div>

  <div class="definition-box">
    <div class="definition-title">Phase 3 — Création des documents de conformité</div>
    <div class="definition-content content-text">
      Travail en binôme. En vous appuyant sur vos recherches et analyses, rédigez :
      <ul>
        <li>Les mentions légales complètes</li>
        <li>La politique de confidentialité (RGPD)</li>
      </ul>
      Bonus si le temps le permet :
      <ul>
        <li>Texte du bandeau cookies</li>
        <li>Registre simplifié des traitements</li>
      </ul>
      <div class="highlight-fact">Livrable de la Phase 3 : Document Word ou PDF professionnel, prêt à être intégré sur le site.</div>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">📄 Livrables finaux à rendre</h2>
  <div class="definition-box">
    <div class="definition-title">Checklist</div>
    <div class="definition-content content-text">
      <ol>
        <li>Document de synthèse / checklist (Phase 1)</li>
        <li>Tableau d'analyse comparative des 3 sites (Phase 2)</li>
        <li>Mentions légales et Politique de confidentialité pour Le Refuge des Renards Polaires (Phase 3)</li>
      </ol>
    </div>
  </div>
</div>

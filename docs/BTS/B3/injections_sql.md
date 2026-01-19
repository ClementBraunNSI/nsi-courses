<style>
.course-tabs { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 2rem 0; padding: 0; }
.course-tab { background: #f5f5f5; color: #333; border: none; padding: 1rem 1.5rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; flex: 1; min-width: 150px; text-align: center; }
.course-tab:hover { background: #e0e0e0; transform: translateY(-2px); }
.course-tab.active { background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; box-shadow: 0 4px 12px rgba(231, 76, 60, 0.4); }
.course-content { display: none; margin-top: 2rem; padding: 2rem; background: #fafafa; border-radius: 12px; border: 1px solid #e0e0e0; }
.course-content.active { display: block; }
.course-header { background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05)); backdrop-filter: blur(20px); border-radius: 24px; padding: 2rem; margin: 2rem 0; border: 1px solid rgba(231, 76, 60, 0.2); text-align: center; }
.section-title { font-size: 2rem; font-weight: 700; background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; }
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1rem 0; font-size: 1.02rem; }
.concept-section { background: var(--md-default-bg-color); border-radius: 20px; padding: 1.5rem; margin: 1.5rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); }
h3.subsection-title { font-size: 1.6rem; font-weight: 600; color: #e74c3c; margin: 0 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 2px solid rgba(231, 76, 60, 0.25); }
.definition-box { background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(192, 57, 43, 0.05)); border-left: 5px solid #e74c3c; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; backdrop-filter: blur(10px); }
.definition-title { font-size: 1.2rem; font-weight: 600; color: #e74c3c; margin-bottom: 0.8rem; }
.exercise-card { background: var(--md-default-bg-color); border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border-left: 4px solid #c0392b; }
.exercise-title { margin: 0 0 1rem 0; color: #c0392b; font-size: 1.2rem; font-weight: 600; }
/* Table Styles */
table { width: 100%; border-collapse: collapse; margin: 1rem 0; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
th { background: #f8f9fa; color: #2c3e50; font-weight: 600; padding: 12px 15px; text-align: left; border-bottom: 2px solid #e9ecef; }
td { padding: 12px 15px; border-bottom: 1px solid #e9ecef; color: #495057; vertical-align: top; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #f8f9fa; }
</style>

<script>
function showCourseSection(sectionId, button) {
  const allContents = document.querySelectorAll('.course-content');
  const allTabs = document.querySelectorAll('.course-tab');
  allContents.forEach(c => c.classList.remove('active'));
  allTabs.forEach(t => { t.classList.remove('active'); t.setAttribute('aria-selected', 'false'); });
  const target = document.getElementById(sectionId);
  if (target) target.classList.add('active');
  if (button) { button.classList.add('active'); button.setAttribute('aria-selected', 'true'); }
  try { const url = new URL(window.location); url.hash = sectionId; history.replaceState(null, '', url); } catch (e) {}
  if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
document.addEventListener('DOMContentLoaded', function() {
  const firstTab = document.querySelector('.course-tab');
  if (firstTab) firstTab.click();
});
</script>

<div class="course-header">
  <h2 class="section-title">TP - Sécurité Web : Injections SQL</h2>
  <p class="course-subtitle">BTS SISR 2ème année · Bloc 2 : Supervision et protection des services réseaux</p>
  <p><strong>Durée : 2 heures</strong> · <strong>Objectif : Comprendre pour mieux protéger</strong></p>
</div>

<div class="concept-section">
  <h3 class="subsection-title">Contexte</h3>
  <div class="content-text">
    Les injections SQL restent l'une des vulnérabilités les plus critiques du web (Top 10 OWASP). Ce TP vous place dans la peau d'un attaquant éthique pour comprendre les mécanismes, puis dans celle d'un administrateur système pour analyser les traces et sécuriser l'infrastructure.
  </div>
</div>

<div class="course-tabs" role="tablist" aria-label="Parties du TP">
  <button id="tab-part1" class="course-tab" role="tab" onclick="showCourseSection('part1', this)">1. Découverte (25')</button>
  <button id="tab-part2" class="course-tab" role="tab" onclick="showCourseSection('part2', this)">2. Analyse Logs (40')</button>
  <button id="tab-part3" class="course-tab" role="tab" onclick="showCourseSection('part3', this)">3. Protection (40')</button>
  <button id="tab-part4" class="course-tab" role="tab" onclick="showCourseSection('part4', this)">4. Rapport (15')</button>
  <button id="tab-livrables" class="course-tab" role="tab" onclick="showCourseSection('livrables', this)">Livrables & Barème</button>
</div>

<!-- PARTIE 1 -->
<div id="part1" class="course-content">
  <div class="concept-section">
    <h3 class="subsection-title">Partie 1 : Découverte de l'injection SQL</h3>
    <p>Objectif : Manipuler une base de données via un formulaire web vulnérable.</p>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 1.1 : Tutoriel interactif (15 min)</h3>
    <div class="exercise-content">
      <p><strong>Se connecter au site d'entraînement :</strong></p>
      <ul>
        <li>URL : <a href="https://www.hacksplaining.com/exercises/sql-injection" target="_blank">https://www.hacksplaining.com/exercises/sql-injection</a></li>
        <li>Cliquer sur "Start lesson"</li>
        <li>Suivre le tutoriel interactif</li>
      </ul>
      
      <div class="definition-box">
        <div class="definition-title">À noter dans le compte rendu</div>
        <ol>
          <li><strong>Quel payload est utilisé dans l'exemple ?</strong></li>
          <li><strong>Quel est l'impact démontré ?</strong></li>
          <li><strong>Capture d'écran :</strong> Insérer la page finale "Lesson Complete"</li>
        </ol>
      </div>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 1.2 : Tester sur un environnement sécurisé</h3>
    <div class="exercise-content">
      <p><strong>Site à utiliser :</strong> <a href="https://portswigger.net/web-security/sql-injection" target="_blank">https://portswigger.net/web-security/sql-injection</a></p>
      
      <p><strong>Mission :</strong></p>
      <ol>
        <li>Cliquer sur "Access the lab" pour le premier exercice</li>
        <li>Lire les instructions (traduction possible avec clic droit)</li>
        <li>Essayer de résoudre le premier lab (niveau apprentice)</li>
      </ol>

      <div class="definition-box">
        <div class="definition-title">Aide</div>
        <ul>
          <li>L'objectif est de modifier l'URL pour voir tous les produits</li>
        </ul>
      </div>

      <div class="definition-box">
        <div class="definition-title">À noter dans le compte rendu</div>
        <ol>
          <li><strong>Quelle URL a été modifiée ?</strong></li>
          <li><strong>Combien de produits s'affichent maintenant ?</strong></li>
          <li><strong>Expliquer le fonctionnement (avec vos mots) :</strong> Pourquoi l'ajout de caractères spéciaux modifie le comportement de la requête SQL ?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- PARTIE 2 -->
<div id="part2" class="course-content">
  <div class="concept-section">
    <h3 class="subsection-title">Partie 2 : Analyse de logs d'attaque</h3>
    <p>Objectif : Repérer les traces d'une attaque dans les fichiers journaux du serveur web (Apache/Nginx).</p>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 2.1 : Identifier des attaques dans des logs (25 min)</h3>
    <div class="exercise-content">
      <p><strong>Voici des extraits de logs Apache (fichier d'accès web) :</strong></p>
      <pre><code>192.168.1.100 - - [18/Jan/2025:10:23:45] "GET /search.php?q=laptop HTTP/1.1" 200 1234
192.168.1.105 - - [18/Jan/2025:10:24:12] "GET /search.php?q=admin' OR '1'='1 HTTP/1.1" 200 5678
192.168.1.100 - - [18/Jan/2025:10:25:33] "GET /search.php?q=smartphone HTTP/1.1" 200 890
192.168.1.105 - - [18/Jan/2025:10:26:01] "GET /search.php?q=' UNION SELECT password FROM users-- HTTP/1.1" 200 3456
192.168.1.110 - - [18/Jan/2025:10:27:15] "GET /contact.php HTTP/1.1" 200 456
192.168.1.105 - - [18/Jan/2025:10:28:42] "GET /search.php?q='; DROP TABLE products-- HTTP/1.1" 500 234
192.168.1.100 - - [18/Jan/2025:10:29:10] "GET /index.php HTTP/1.1" 200 2345
192.168.1.105 - - [18/Jan/2025:10:30:05] "GET /search.php?q=admin'-- HTTP/1.1" 200 1890</code></pre>

      <div class="definition-box">
        <div class="definition-title">Analyser ces logs</div>
        <ol>
          <li><strong>Combien de lignes au total ?</strong></li>
          <li><strong>Combien de requêtes sont suspectes (tentatives d'injection) ?</strong></li>
          <li><strong>Comment fonctionnent chacune de ces requêtes ?</strong></li>
          <li><strong>Quelle est l'adresse IP de l'attaquant ?</strong></li>
          <li><strong>Compléter le tableau des attaques :</strong></li>
        </ol>
        
        <table>
          <thead>
            <tr>
              <th>Ligne n°</th>
              <th>Payload utilisé</th>
              <th>Type d'attaque</th>
              <th>Code HTTP</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>2</td>
              <td><code>admin' OR '1'='1</code></td>
              <td>Bypass authentification</td>
              <td>200</td>
            </tr>
            <tr>
              <td>4</td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>6</td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
            <tr>
              <td>8</td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          </tbody>
        </table>

        <p><strong>6. Quelle attaque a provoqué une erreur serveur (code 500) ?</strong></p>
        <ul>
          <li>Ligne n° :</li>
          <li>Payload :</li>
          <li>Pourquoi c'est dangereux ?</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 2.2 : Proposer des actions (15 min)</h3>
    <div class="exercise-content">
      <p><strong>En tant qu'administrateur système, définir les actions à entreprendre et justifier.</strong></p>
      <ul>
        <li>[ ] Bloquer l'IP 192.168.1.105</li>
        <li>[ ] Ne rien faire, c'est normal</li>
        <li>[ ] Alerter l'équipe de développement</li>
        <li>[ ] Installer un pare-feu applicatif (WAF)</li>
        <li>[ ] Supprimer le site web</li>
        <li>[ ] Analyser tous les logs pour chercher d'autres attaques</li>
        <li>[ ] Redémarrer le serveur</li>
      </ul>
    </div>
  </div>
</div>

<!-- PARTIE 3 -->
<div id="part3" class="course-content">
  <div class="concept-section">
    <h3 class="subsection-title">Partie 3 : Solutions de protection</h3>
    <p>Objectif : Mettre en place des contre-mesures techniques (WAF) et organisationnelles.</p>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 3.1 : Découvrir ModSecurity (15 min)</h3>
    <div class="exercise-content">
      <p><strong>Rechercher des informations sur ModSecurity :</strong></p>
      <ul>
        <li>Documentation : <a href="https://github.com/SpiderLabs/ModSecurity" target="_blank">https://github.com/SpiderLabs/ModSecurity</a></li>
        <li>Ou vidéo YouTube : "ModSecurity Tutorial" (5-10 min)</li>
      </ul>

      <div class="definition-box">
        <div class="definition-title">À noter dans le compte rendu</div>
        <ol>
          <li><strong>Qu'est ce que ModSecurity? Comment fonctionne-t-il?</strong></li>
          <li><strong>Que signifie OWASP CRS ?</strong></li>
          <li><strong>Donner 3 types d'attaques que ModSecurity peut bloquer :</strong></li>
        </ol>
      </div>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 3.2 : Simulation de configuration (15 min)</h3>
    <div class="exercise-content">
      <p><strong>Scénario :</strong> Il faut protéger le site web de l'entreprise.</p>
      <p><strong>Compléter cette configuration ModSecurity (remplacer les ___), justifier les choix :</strong></p>
      
      <pre><code># Configuration ModSecurity

# Activer le moteur de règles
SecRuleEngine ___          (Choix : On / Off / DetectionOnly)

# Bloquer les injections SQL
SecRule ARGS "@contains ___" \     (Choix : SELECT / DELETE / admin)
    "id:1001,\
    phase:2,\
    block,\
    msg:'Tentative injection SQL détectée'"

# Niveau de sévérité des logs
SecAuditLogType ___        (Choix : Serial / Concurrent / None)</code></pre>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 3.3 : Défense en profondeur (10 min)</h3>
    <div class="exercise-content">
      <p><strong>Le principe de "défense en profondeur" = plusieurs couches de protection.</strong></p>
      <p><strong>Classer ces mesures par ordre (1 = première ligne, 5 = dernière) :</strong></p>
      
      <table>
        <thead>
          <tr>
            <th>Mesure</th>
            <th>Ordre</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>WAF (ModSecurity)</td>
            <td></td>
          </tr>
          <tr>
            <td>Code sécurisé (requêtes préparées)</td>
            <td></td>
          </tr>
          <tr>
            <td>Pare-feu réseau</td>
            <td></td>
          </tr>
          <tr>
            <td>Surveillance des logs (SIEM)</td>
            <td></td>
          </tr>
          <tr>
            <td>Politique de mots de passe forts</td>
            <td></td>
          </tr>
        </tbody>
      </table>

      <div class="definition-box">
        <div class="definition-title">Dans le compte rendu</div>
        <p>Schématiser la défense en profondeur : dessiner les couches depuis Internet jusqu'à la base de données.</p>
        <code>[Internet] → [ ? ] → [ ? ] → [ ? ] → [ ? ] → [Base de données]</code>
      </div>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 3.4 (Bonus) : Automatisation</h3>
    <div class="exercise-content">
      <p><strong>Contexte :</strong> Bloquer manuellement les IP (comme vu dans l'exercice 2.2) est impossible à grande échelle.</p>
      <div class="definition-box">
        <div class="definition-title">Recherche rapide</div>
        <ol>
          <li>Quel outil Linux open-source permet de bannir automatiquement (via iptables) une IP qui génère trop d'erreurs ou de comportements suspects dans les logs ?</li>
          <li>Comment s'appelle le mécanisme utilisé par cet outil pour repérer les motifs d'attaque (ex: "UNION SELECT") dans les fichiers logs ?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- PARTIE 4 -->
<div id="part4" class="course-content">
  <div class="concept-section">
    <h3 class="subsection-title">Partie 4 : Mini-rapport (15 min)</h3>
    <p>Objectif : Rédiger un rapport professionnel synthétique pour la direction technique.</p>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Exercice 4.1 : Rapport d'incident</h3>
    <div class="exercise-content">
      <p><strong>Contexte :</strong> En tant que technicien SISR, le responsable IT vous demande un rapport suite aux logs suspects identifiés en partie 2.</p>
      <p><strong>Rédiger un court rapport (1/2 page) avec cette structure :</strong></p>
      
      <div style="border: 1px solid #ccc; padding: 20px; background: #fff;">
        <h4 style="text-align: center;">RAPPORT D'INCIDENT DE SÉCURITÉ</h4>
        <p><strong>Date :</strong> _____________ &nbsp;&nbsp; <strong>Rédigé par :</strong> _____________</p>
        
        <h5>1. RÉSUMÉ DE L'INCIDENT</h5>
        <p><em>(En 2-3 lignes, que s'est-il passé ?)</em></p>
        <br>
        
        <h5>2. ANALYSE TECHNIQUE</h5>
        <ul>
          <li>Nombre d'attaques détectées : _______</li>
          <li>Adresse IP source : _______</li>
          <li>Type d'attaque : _______</li>
          <li>Gravité (Faible/Moyenne/Élevée) : _______</li>
        </ul>
        
        <h5>3. IMPACT POTENTIEL</h5>
        <p><em>(Que pourrait-il se passer si ces attaques réussissaient ?)</em></p>
        <br>
        
        <h5>4. RECOMMANDATIONS IMMÉDIATES</h5>
        <ol>
          <li></li>
          <li></li>
        </ol>
        
        <h5>5. RECOMMANDATIONS À MOYEN TERME</h5>
        <ol>
          <li></li>
          <li></li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- LIVRABLES -->
<div id="livrables" class="course-content">
  <div class="concept-section">
    <h3 class="subsection-title">Livrables à rendre</h3>
    <div class="content-text">
      <p><strong>Format :</strong> Fichier PDF unique nommé <code>NOM_Prenom_TP_B3_SQL.pdf</code></p>
      <ul>
        <li>Réponses Partie 1 (capture tutoriel + questions)</li>
        <li>Tableau analyse logs complété (Partie 2)</li>
        <li>Actions proposées justifiées</li>
        <li>Réponses sur ModSecurity (Partie 3)</li>
        <li>Configuration ModSecurity complétée</li>
        <li>Schéma défense en profondeur</li>
        <li>Rapport d'incident (Partie 4)</li>
      </ul>
    </div>
  </div>

  <div class="exercise-card">
    <h3 class="exercise-title">Barème (/20)</h3>
    <table>
      <thead>
        <tr>
          <th>Partie</th>
          <th>Points</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Partie 1 - Découverte injection SQL</td>
          <td>/5</td>
        </tr>
        <tr>
          <td>Partie 2 - Analyse de logs</td>
          <td>/6</td>
        </tr>
        <tr>
          <td>Partie 3 - Solutions de protection</td>
          <td>/6</td>
        </tr>
        <tr>
          <td>Partie 4 - Rapport d'incident</td>
          <td>/3</td>
        </tr>
        <tr>
          <td><strong>TOTAL</strong></td>
          <td><strong>/20</strong></td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <div class="definition-box">
    <div class="definition-title">Rappels importants</div>
    <ul>
      <li>Ces techniques sont enseignées à des fins défensives uniquement</li>
      <li>Tester des injections SQL sans autorisation est illégal</li>
    </ul>
  </div>
</div>

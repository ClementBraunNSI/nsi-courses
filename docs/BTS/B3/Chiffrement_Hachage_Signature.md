<style>
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
.definition-content { color: var(--md-default-fg-color); font-size: 1.05rem; line-height: 1.6; }
.content-text { color: var(--md-default-fg-color); line-height: 1.7; margin: 1.2rem 0; font-size: 1.05rem; }
.highlight-fact { background: rgba(46, 204, 113, 0.1); border-left: 4px solid #2ecc71; padding: 1rem; margin: 1rem 0; border-radius: 8px; font-weight: 500; }
.warning-fact { background: rgba(241, 196, 15, 0.1); border-left: 4px solid #f1c40f; padding: 1rem; margin: 1rem 0; border-radius: 8px; font-weight: 500; }
.exercise-container { background: white; border-radius: 15px; padding: 1.5rem; margin: 1.5rem 0; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); border-left: 5px solid #3498db; }
.exercise-title { font-size: 1.4rem; font-weight: 600; color: #2980b9; margin-bottom: 1rem; }
.exercise-table { width: 100%; border-collapse: collapse; margin: 1rem 0; background: rgba(255, 255, 255, 0.85); border-radius: 8px; overflow: hidden; }
.exercise-table th, .exercise-table td { padding: 0.8rem; text-align: left; border: 1px solid rgba(52, 152, 219, 0.2); }
.exercise-table th { background: rgba(52, 152, 219, 0.2); font-weight: 600; color: #2c3e50; }
@media (max-width: 768px) { .course-title { font-size: 2rem; } .course-header { padding: 2rem; } }
h3.subsection-title { font-size: 1.6rem; font-weight: 600; color: #3498db; margin: 1.5rem 0 0.8rem 0; padding-bottom: 0.4rem; border-bottom: 2px solid rgba(52, 152, 219, 0.25); }
h4.subsubsection-title { font-size: 1.25rem; font-weight: 600; color: #2c3e50; margin: 1.2rem 0 0.6rem 0; padding-bottom: 0.3rem; border-bottom: 1px dashed rgba(44, 62, 80, 0.3); }
</style>

<div class="course-header">
  <h1 class="course-title">🔐 B3 — Chiffrement, Hachage, Signature</h1>
  <p class="course-subtitle">BTS SIO • Bloc 3 — Confidentialité, intégrité, authenticité et non-répudiation</p>
</div>

<div class="concept-section">
  <h2 class="section-title">1. Vue d’ensemble : pourquoi la cryptographie ?</h2>

  <div class="definition-box">
    <div class="definition-title">Objectifs</div>
    <div class="definition-content">
      <ul>
        <li>Confidentialité : lire uniquement si autorisé (chiffrement)</li>
        <li>Intégrité : vérifier qu’un message n’a pas été modifié (hachage/HMAC)</li>
        <li>Authenticité : savoir qui a envoyé (signature numérique)</li>
        <li>Non-répudiation : empêcher de nier une action (signature + preuve)</li>
      </ul>
    </div>
  </div>

  <div class="highlight-fact">La cryptographie est au cœur des services modernes (TLS sur le web, VPN, stockage chifré, authentification forte).</div>
</div>

<div class="concept-section">
  <h2 class="section-title">2. Chiffrement</h2>
  <h3 class="subsection-title">2.0 Définitions</h3>
  <div class="definition-box">
    <div class="definition-title">Terminologie</div>
    <div class="definition-content content-text">
      <ul>
        <li><strong>Cryptographie</strong> : ensemble de techniques mathématiques permettant d’assurer confidentialité, intégrité, authenticité et non‑répudiation des informations.</li>
        <li><strong>Chiffrement</strong> : transformation d’un message en clair en un message chifré au moyen d’un algorithme et d’une clé.</li>
        <li><strong>Déchiffrement</strong> : opération inverse du chiffrement réalisée avec la clé légitime, pour retrouver le message en clair.</li>
        <li><strong>Décryptage</strong> : tentative de retrouver le message en clair <em>sans</em> disposer de la clé légitime (attaque).</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">2.1 Chiffrement symétrique</h3>
  <div class="definition-box">
    <div class="definition-title">Principe</div>
    <div class="definition-content content-text">
      <p>Une même clé secrète sert pour chiffrer et déchiffrer. Rapide, idéal pour gros volumes.</p>
      <ul>
        <li>Algorithmes : AES (128/192/256), ChaCha20</li>
        <li>Modes : CBC (avec IV), GCM (authentifié), CTR (flux)</li>
        <li>Usages : disques/BDD chiffrés, sessions TLS (après échange de clés)</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">2.2 Chiffrement asymétrique</h3>
  <div class="definition-box">
    <div class="definition-title">Principe</div>
    <div class="definition-content content-text">
      <p>Deux clés différentes : une <strong>publique</strong> pour chiffrer, une <strong>privée</strong> pour déchiffrer. Plus coûteux, adapté à l’échange de clés et à la signature.</p>
      <ul>
        <li>Algorithmes : RSA (2048+), ECC (courbes elliptique, ex: secp256r1), Diffie‑Hellman/ECDH</li>
        <li>Usages : échange de la clé symétrique, certificats, signature</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">2.3 Bonnes pratiques</h3>
  <div class="definition-box">
    <div class="definition-title">Recommandations</div>
    <div class="definition-content content-text">
      <ul>
        <li>Ne pas créer ses propres algorithmes; utiliser des bibliothèques reconnues</li>
        <li>Privilégier AES‑GCM ou ChaCha20‑Poly1305 pour la confidentialité + intégrité</li>
        <li>Clés : tailles suffisantes (≥ 128 bits symétrique; RSA ≥ 2048; ECC courantes)</li>
        <li>Gestion des IV/nonce uniques par message en modes CBC/CTR/GCM</li>
        <li>Rotation et stockage sécurisé des clés (HSM, KMS)</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">2.4 Chiffrement de César</h3>
  <div class="definition-box">
    <div class="definition-title">Principe</div>
    <div class="definition-content content-text">
      <p>Substitution mono‑alphabétique par décalage : chaque lettre est déplacée d’un décalage <strong>k</strong> dans l’alphabet.</p>
      <table class="exercise-table">
        <thead>
          <tr><th>Alphabet</th><th>Codage</th><th>Formule</th></tr>
        </thead>
        <tbody>
          <tr><td>A…Z</td><td>A=0, B=1, …, Z=25</td><td><strong>E(x) = (x + k) mod 26</strong>; <strong>D(y) = (y − k) mod 26</strong></td></tr>
        </tbody>
      </table>
      <p>Ignorer les accents, conserver les espaces et ponctuation; travailler en majuscules pour simplifier.</p>
    </div>
  </div>

  <div class="exercise-container">
    <div class="exercise-title">📝 Exercices — César</div>
    <table class="exercise-table">
      <thead>
        <tr><th>Texte clair</th><th>k</th><th>Texte chifré</th></tr>
      </thead>
      <tbody>
        <tr><td>RENARD</td><td>3</td><td></td></tr>
        <tr><td>SECURITE</td><td>6</td><td></td></tr>
        <tr><td>CYBER</td><td>19</td><td></td></tr>
      </tbody>
    </table>
    <table class="exercise-table">
      <thead>
        <tr><th>Texte chifré</th><th>k</th><th>Texte clair</th></tr>
      </thead>
      <tbody>
        <tr><td>QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD</td><td>23</td><td></td></tr>
        <tr><td>DPDMZ MZ ETML</td><td>18</td><td></td></tr>
      </tbody>
    </table>
    <div class="content-text"><p>Proposer une méthode de <strong>décryptage</strong> sans connaître <em>k</em> (fréquence des lettres, test sur E/ES/LE). Appliquer au texte : <code>UIJT JT B TFTU PG DFTBS DJQIFSNFOU</code>.</p></div>
  </div>

  <h3 class="subsection-title">2.5 Chiffrement de Vigenère</h3>
  <div class="definition-box">
    <div class="definition-title">Principe</div>
    <div class="definition-content content-text">
      <p>Substitution poly‑alphabétique par décalages successifs dérivés d’une <strong>clé</strong> répétée.</p>
      <table class="exercise-table">
        <thead>
          <tr><th>Clair</th><th>Clé (répétée)</th><th>Codage</th><th>Formule</th></tr>
        </thead>
        <tbody>
          <tr><td>A…Z</td><td>RENARD…</td><td>A=0,…,Z=25</td><td><strong>E(i) = (P<i> + K<i>) mod 26</strong>; <strong>D(i) = (C<i> − K<i>) mod 26</strong></td></tr>
        </tbody>
      </table>
      <p>La clé est alignée sur la longueur du message (sans espaces). Ignorer les accents, travailler en majuscules.</p>
    </div>
  </div>

  <div class="exercise-container">
    <div class="exercise-title">📝 Exercices — Vigenère</div>
    <table class="exercise-table">
      <thead>
        <tr><th>Texte clair</th><th>Clé</th><th>Texte chifré</th></tr>
      </thead>
      <tbody>
        <tr><td>SECURITEINFORMATIQUE</td><td>RENARD</td><td></td></tr>
        <tr><td>CYBERDEFENSE</td><td>FOX</td><td></td></tr>
      </tbody>
    </table>
    <table class="exercise-table">
      <thead>
        <tr><th>Texte chifré</th><th>Clé</th><th>Texte clair</th></tr>
      </thead>
      <tbody>
        <tr><td>VNZV QH BWXWZ</td><td>KEY</td><td></td></tr>
      </tbody>
    </table>
    <div class="content-text"><p>Décryptage sans clé : proposer une approche simple (tester quelques longueurs de clé, repérer des répétitions, essayer des clés probables liées au contexte).</p></div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">3. Hachage</h2>

  <h3 class="subsection-title">3.1 Propriétés</h3>
  <div class="definition-box">
    <div class="definition-title">Fonctions de hachage cryptographique</div>
    <div class="definition-content content-text">
      <ul>
        <li>Pré‑image difficile : retrouver l’entrée depuis le hash est infaisable</li>
        <li>Seconde pré‑image difficile : trouver une entrée différente avec même hash</li>
        <li>Résistance aux collisions : deux entrées différentes ne doivent pas produire le même hash</li>
      </ul>
      <p>Exemples : SHA‑256, SHA‑3. Éviter MD5 et SHA‑1.</p>
    </div>
  </div>

  <h3 class="subsection-title">3.2 Usages</h3>
  <div class="definition-box">
    <div class="definition-title">Cas d’usage</div>
    <div class="definition-content content-text">
      <ul>
        <li>Empreintes de fichiers (vérification d’intégrité)</li>
        <li>Stockage de mots de passe : <strong>hachage dédié</strong> avec sel et durcissement (Argon2, bcrypt, PBKDF2)</li>
        <li>HMAC : intégrité et authentification de messages (hash avec clé)</li>
      </ul>
    </div>
  </div>

  <div class="warning-fact">Ne jamais stocker les mots de passe en clair ni avec un simple SHA‑256. Utiliser un algorithme de dérivation avec <strong>sel</strong> et <strong>itérations</strong>.</div>
</div>

<div class="concept-section">
  <h2 class="section-title">4. Signature numérique</h2>

  <h3 class="subsection-title">4.1 Principe</h3>
  <div class="definition-box">
    <div class="definition-title">Clés et opérations</div>
    <div class="definition-content content-text">
      <p>La signature utilise la <strong>clé privée</strong> du signataire pour générer une preuve sur le message; la vérification se fait avec la <strong>clé publique</strong>.</p>
      <ul>
        <li>Garanties : authenticité, intégrité, non‑répudiation</li>
        <li>Algorithmes : RSA‑PSS, ECDSA</li>
        <li>Pratique : on signe souvent le <strong>haché</strong> du message</li>
      </ul>
    </div>
  </div>

  <h3 class="subsection-title">4.2 Certificats et PKI</h3>
  <div class="definition-box">
    <div class="definition-title">Chaîne de confiance</div>
    <div class="definition-content content-text">
      <ul>
        <li>Certificat X.509 : contient la clé publique et l’identité, signé par une autorité</li>
        <li>Autorités de certification (CA) : racine, intermédiaire; révocation (CRL/OCSP)</li>
        <li>Usage dans TLS : authenticité du serveur, échange sécurisé des clés</li>
      </ul>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">5. TLS en bref</h2>
  <div class="definition-box">
    <div class="definition-title">Étapes simplifiées</div>
    <div class="definition-content content-text">
      <ol>
        <li>Négociation et présentation du certificat du serveur</li>
        <li>Vérification de la chaîne de confiance (PKI)</li>
        <li>Échange de clé de session (ECDHE) et paramètres</li>
        <li>Chiffrement symétrique de la session (AES‑GCM ou ChaCha20‑Poly1305)</li>
        <li>Intégrité des messages (AEAD) et fermeture sécurisée</li>
      </ol>
    </div>
  </div>
</div>

<div class="concept-section">
  <h2 class="section-title">6. Bonnes pratiques</h2>
  <div class="definition-box">
    <div class="definition-title">Sélection et mise en œuvre</div>
    <div class="definition-content content-text">
      <ul>
        <li>Bibliothèques éprouvées, mises à jour</li>
        <li>Politiques de gestion de clés : génération, stockage, rotation, révocation</li>
        <li>Chiffrement en transit (TLS) et au repos (disque/BDD)</li>
        <li>Durcissement des mots de passe : Argon2/bcrypt/PBKDF2 + sel</li>
        <li>Audit et supervision : journalisation, détection d’anomalies</li>
      </ul>
    </div>
  </div>
  <div class="highlight-fact">Associer cryptographie, gouvernance et supervision pour un niveau de sécurité cohérent avec les risques.</div>
</div>

<div class="concept-section">
  <h2 class="section-title">7. Exercices</h2>

  <div class="exercise-container">
    <div class="exercise-title">📝 Exercice 1 — Associer usage et technique</div>
    <table class="exercise-table">
      <thead>
        <tr>
          <th>Usage</th>
          <th>Technique adaptée</th>
          <th>Justification</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Stockage de mots de passe</td><td></td><td></td></tr>
        <tr><td>Vérifier l’intégrité d’un fichier téléchargé</td><td></td><td></td></tr>
        <tr><td>Sécuriser une session web</td><td></td><td></td></tr>
        <tr><td>Prouver l’origine d’un document</td><td></td><td></td></tr>
      </tbody>
    </table>
  </div>

  <div class="exercise-container">
    <div class="exercise-title">📝 Exercice 2 — Certificat et PKI</div>
    <div class="content-text"><p>Expliquer la chaîne de confiance pour un site web et indiquer 3 erreurs de configuration courantes à éviter.</p></div>
  </div>

  <div class="exercise-container">
    <div class="exercise-title">📝 Exercice 3 — Choix d’algorithmes</div>
    <div class="content-text"><p>Proposer un choix d’algorithmes et paramètres pour : chiffrement d’une base de données, stockage de mots de passe, signature d’un contrat PDF.</p></div>
  </div>
</div>
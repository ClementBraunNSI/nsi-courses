# Fiche d'exercices : Encodage des caractères

<style>
/* Styles pour les fiches d'exercices avec système de cartes et onglets */
.exercise-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.exercise-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(102, 126, 234, 0.4);
}

.exercise-title {
    color: #ffffff;
    font-size: 1.3em;
    font-weight: bold;
    margin-bottom: 15px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.solution {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    border-left: 4px solid #4CAF50;
    backdrop-filter: blur(5px);
}

.solution-toggle {
    background: linear-gradient(135deg, #4CAF50, #45a049);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 0.9em;
    transition: all 0.3s ease;
    margin-bottom: 10px;
}

.solution-toggle:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.solution-content {
    display: none;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.code-block {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    padding: 15px;
    font-family: 'Courier New', monospace;
    margin: 10px 0;
    border-left: 3px solid #ff6b6b;
}

.ascii-table {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    font-family: monospace;
    font-size: 0.9em;
}
</style>

## Encodage en table ASCII

**Décoder les messages suivants en hexadécimal à l'aide de la table ASCII**

   1. `48 65 6C 6C 6F`
   2. `57 6F 72 6C 64`
   3. `31 32 33 34 35`

**Encoder les messages suivants à l'aide de la table ASCII**  

   1. `Hello`  
   2. `123`  
   3. `!@#`  
   4. `Code`  

**Python permet d'encoder des messages à l'aide de divers encodages. Il existe la méthode `encode` des chaînes de caractères. Elle s'utilise de cette manière chaine_de_caractere.encode('Méthode d'encodage').**  

   1. Instancier la chaîne de caractère : *La vitesse de la lumière est de 300 000km/s*.  
   2. Que se passe-t-il si l'on veut afficher l'encodage en ASCII de cette chaîne de caractère? Comment l'expliquer?  

**La méthode `decode` de Python permet de donner le caractère associé à un point de code donné.**  
**Cela s'utilise de cette manière : chaine_de_caractere.decode('Méthode de décodage').**  
**Donner les caractères associés à ces points de code :**  
      1. b'\x41'  
      2. b'\xce\xa9'  
      3. b'\xe3\x81\x93'

<div class="exercise-card">
<h4 class="exercise-title">Exercice 4 - Conversion binaire vers ASCII ⭐⭐</h4>

**Convertir les séquences binaires suivantes en caractères ASCII :**

1. `01001000 01100101 01101100 01101100 01101111`
2. `01010000 01111001 01110100 01101000 01101111 01101110`
3. `00110001 00110010 00110011 00110100 00110101`

<button class="solution-toggle" onclick="toggleSolution('sol4')">💡 Voir les solutions</button>
<div class="solution" id="sol4">
<div class="solution-content">
<strong>Solutions :</strong><br>
1. H-e-l-l-o → "Hello"<br>
2. P-y-t-h-o-n → "Python"<br>
3. 1-2-3-4-5 → "12345"
</div>
</div>
</div>

<div class="exercise-card">
<h4 class="exercise-title">Exercice 5 - Encodage UTF-8 ⭐⭐⭐</h4>

**Comprendre l'encodage UTF-8 :**

1. Expliquer pourquoi le caractère 'é' nécessite 2 octets en UTF-8
2. Encoder le mot "café" en UTF-8 (donner les octets en hexadécimal)
3. Décoder la séquence UTF-8 : `C3 A9 74 C3 A9`
4. Combien d'octets sont nécessaires pour encoder "🐍" (emoji serpent) ?

<button class="solution-toggle" onclick="toggleSolution('sol5')">💡 Voir les solutions</button>
<div class="solution" id="sol5">
<div class="solution-content">
<strong>1.</strong> Le 'é' a un point de code U+00E9 (233 en décimal), qui dépasse 127, donc nécessite l'encodage multi-octets UTF-8.<br><br>
<strong>2.</strong> "café" → 63 61 66 C3 A9<br>
<strong>3.</strong> "été"<br>
<strong>4.</strong> 4 octets (F0 9F 90 8D)
</div>
</div>
</div>

<div class="exercise-card">
<h4 class="exercise-title">Exercice 6 - Programmation avec encodages ⭐⭐⭐</h4>

**Écrire des fonctions Python :**

1. `ascii_vers_binaire(texte)` : convertit un texte ASCII en binaire
2. `binaire_vers_ascii(binaire)` : convertit du binaire en texte ASCII
3. `compter_octets_utf8(texte)` : compte le nombre d'octets nécessaires en UTF-8
4. `est_ascii_pur(texte)` : vérifie si un texte ne contient que des caractères ASCII

<button class="solution-toggle" onclick="toggleSolution('sol6')">💡 Voir les solutions</button>
<div class="solution" id="sol6">
<div class="solution-content">
<div class="code-block">
def ascii_vers_binaire(texte):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return ' '.join(format(ord(c), '08b') for c in texte)<br><br>
def binaire_vers_ascii(binaire):<br>
&nbsp;&nbsp;&nbsp;&nbsp;octets = binaire.split()<br>
&nbsp;&nbsp;&nbsp;&nbsp;return ''.join(chr(int(b, 2)) for b in octets)<br><br>
def compter_octets_utf8(texte):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return len(texte.encode('utf-8'))<br><br>
def est_ascii_pur(texte):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return all(ord(c) < 128 for c in texte)
</div>
</div>
</div>
</div>

<div class="exercise-card">
<h4 class="exercise-title">Exercice 7 - Chiffrement César ⭐⭐⭐</h4>

**Implémenter le chiffrement César avec les codes ASCII :**

1. Écrire `chiffrer_cesar(texte, decalage)` qui décale chaque lettre
2. Écrire `dechiffrer_cesar(texte_chiffre, decalage)` pour déchiffrer
3. Tester avec le message "HELLO" et un décalage de 3
4. Que devient "PYTHON" avec un décalage de 13 ?

<button class="solution-toggle" onclick="toggleSolution('sol7')">💡 Voir les solutions</button>
<div class="solution" id="sol7">
<div class="solution-content">
<div class="code-block">
def chiffrer_cesar(texte, decalage):<br>
&nbsp;&nbsp;&nbsp;&nbsp;resultat = ""<br>
&nbsp;&nbsp;&nbsp;&nbsp;for c in texte:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if c.isalpha():<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base = ord('A') if c.isupper() else ord('a')<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultat += chr((ord(c) - base + decalage) % 26 + base)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resultat += c<br>
&nbsp;&nbsp;&nbsp;&nbsp;return resultat<br><br>
def dechiffrer_cesar(texte_chiffre, decalage):<br>
&nbsp;&nbsp;&nbsp;&nbsp;return chiffrer_cesar(texte_chiffre, -decalage)
</div>
<strong>3.</strong> "HELLO" → "KHOOR"<br>
<strong>4.</strong> "PYTHON" → "CLGUBA"
</div>
</div>
</div>

<div class="ascii-table">
<strong>📋 Rappel - Table ASCII (extrait) :</strong><br>
32=' ' 33='!' 48='0' 49='1' 65='A' 66='B' 97='a' 98='b'<br>
34='"' 35='#' 50='2' 51='3' 67='C' 68='D' 99='c' 100='d'<br>
...
</div>

<script>
function toggleSolution(id) {
    const content = document.querySelector(`#${id} .solution-content`);
    if (content.style.display === 'none' || content.style.display === '') {
        content.style.display = 'block';
    } else {
        content.style.display = 'none';
    }
}
</script>

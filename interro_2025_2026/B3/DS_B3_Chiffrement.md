# Devoir Surveillé – BTS SIO 1ère année (B3)

## Chiffrement — Sujet (Durée: 2 heures)

- Barème total: 20 points
- Matériel autorisé: aucun
- Rendu: réponses claires et justifiées quand demandé

| N° | Consigne | Points |
|---|---|---|
| 1 | Définir en une phrase: chiffrement, hachage, signature numérique | 3 |
| 2 | Expliquer la différence entre chiffrement symétrique et asymétrique. Donner 1 avantage et 1 inconvénient de chaque. | 2 |
| 3 | En RSA, expliquer le rôle des clés publique et privée pour chiffrer et pour signer. | 2 |
| 4 | QCM — cocher la bonne réponse et justifier en une phrase: a) Le chiffrement protège surtout la: (Confidentialité/Intégrité/Disponibilité); b) La signature numérique assure: (Authenticité/Chiffrement/Disponibilité); c) AES est: (Symétrique/Asymétrique) | 1.5 |
| 5 | Associer chaque technique à la propriété principale qu’elle garantit: chiffrement, hachage, signature numérique → (Confidentialité, Intégrité, Authenticité/Non‑répudiation). | 1.5 |
| 6 | César: chiffrer « BONJOUR » avec clé 3; déchiffrer « ERQMRXU » avec clé 3; indiquer la clé correcte via force brute (justifier brièvement). | 2 |
| 7 | Vigenère: chiffrer « HELLO WORLD » avec la clé « KEY » (ignorer les espaces; lettres en majuscules). | 2 |
| 8 | RSA simplifié: avec p=61 et q=53, calculer n, φ(n). Choisir e=17 (premier avec φ(n)). Calculer d tel que (d×e) % φ(n) = 1. Donner clé publique et clé privée. | 4 |
| 9 | RSA calcul: avec la clé publique de la question 8, chiffrer le nombre m=123 → c. Puis déchiffrer c pour retrouver m (donner les valeurs). | 2 |

Données utiles:
- Alphabet: `ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"`
- Modulo: `%26` pour revenir au début de l’alphabet
- Indices de lettres: `A=0, B=1, ..., Z=25`
- RSA: `n = p×q`, `φ(n) = (p-1)×(q-1)`, `c = m^e mod n`, `m = c^d mod n`

---

## Corrigé — Tableau récapitulatif

| N° | Réponse attendue | Barème |
|---|---|---|
| 1 | Chiffrement: rendre un message illisible sans clé (confidentialité). Hachage: empreinte non réversible pour vérifier intégrité. Signature numérique: preuve d’auteur et intégrité avec clé privée (authenticité/non‑répudiation). | 3×1 |
| 2 | Symétrique: une seule clé partagée (avantage: rapide, inconvénient: distribution de clé). Asymétrique: paire (publique/privée) (avantage: partage sûr de la clé publique, inconvénient: plus lent). | 2 |
| 3 | RSA: chiffrer avec clé publique `(e,n)`, déchiffrer avec clé privée `(d,n)`; signer avec clé privée, vérifier la signature avec clé publique. | 2 |
| 4 | a) Confidentialité (chiffrement) — justification; b) Authenticité (signature) — justification; c) AES: symétrique — justification. | 3×0.5 |
| 5 | Chiffrement → Confidentialité; Hachage → Intégrité; Signature numérique → Authenticité/Non‑répudiation. | 1.5 |
| 6 | Chiffrement César clé 3: « BONJOUR » → « ERQMRXU »; Déchiffrer « ERQMRXU » clé 3 → « BONJOUR »; Force brute: clé correcte = 3 (argument: sortie lisible). | 2 (0.75+0.75+0.5) |
| 7 | Vigenère « HELLO WORLD » avec « KEY » → « RIJVS UYVJN ». | 2 |
| 8 | p=61, q=53 → `n=3233`, `φ(n)=3120`; `e=17`; `d=2753` (inverse modulaire: `(d×17) % 3120 = 1`); Clé publique `(17, 3233)`, clé privée `(2753, 3233)`. | 4 (n:1, φ:1, e:1, d:1) |
| 9 | `c = 123^17 mod 3233 = 855`; `m = 855^2753 mod 3233 = 123`. | 2 (1+1) |

---

### Notes de correction
- Justifications courtes acceptées si exactes et liées au contexte.
- Vigenère: majuscules et espaces conservés; toute méthode correcte acceptée.
- RSA: valeurs numériques attendues comme ci‑dessus; méthode (inverse modulaire) cohérente.

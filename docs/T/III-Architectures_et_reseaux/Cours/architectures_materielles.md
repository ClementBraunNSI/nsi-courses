# Architectures matérielles et systèmes

## Introduction

L'architecture matérielle d'un ordinateur détermine ses capacités et ses performances. Comprendre ces concepts est essentiel pour optimiser les programmes et comprendre les limitations des systèmes informatiques.

### Évolution historique

**Générations d'ordinateurs :**
1. **1ère génération (1940-1950)** : tubes à vide, ENIAC
2. **2ème génération (1950-1960)** : transistors, IBM 7090
3. **3ème génération (1960-1970)** : circuits intégrés, IBM System/360
4. **4ème génération (1970-aujourd'hui)** : microprocesseurs, PC
5. **5ème génération (futur)** : intelligence artificielle, informatique quantique

---

## Architecture de von Neumann

### Principe fondamental

L'architecture de von Neumann, proposée en 1945, reste la base des ordinateurs modernes.

### Composants principaux

#### 1. Unité Centrale de Traitement (CPU)

**Rôles :**
- Exécution des instructions
- Contrôle des autres composants
- Calculs arithmétiques et logiques

**Sous-composants :**

**Unité de Contrôle (UC) :**
- Décode les instructions
- Génère les signaux de contrôle
- Gère le séquencement

**Unité Arithmétique et Logique (UAL/ALU) :**
- Opérations arithmétiques (+, -, ×, ÷)
- Opérations logiques (AND, OR, NOT, XOR)
- Comparaisons
- Décalages de bits

**Registres :**
- Mémoire ultra-rapide intégrée au processeur
- Stockage temporaire des données et instructions

#### 2. Mémoire

**Mémoire principale (RAM) :**
- Stockage temporaire des programmes et données
- Accès direct et rapide
- Volatile (perdue à l'extinction)

**Mémoire de masse :**
- Stockage permanent
- Disques durs, SSD, etc.
- Plus lente mais plus grande capacité

#### 3. Unités d'Entrée/Sortie

**Entrée :**
- Clavier, souris, microphone
- Capteurs, caméras
- Interfaces réseau

**Sortie :**
- Écran, imprimante, haut-parleurs
- Moteurs, actionneurs
- Interfaces réseau

#### 4. Bus de communication

**Bus de données :**
- Transport des données entre composants
- Largeur détermine la quantité de données transférées

**Bus d'adresses :**
- Spécifie l'emplacement mémoire
- Largeur détermine l'espace adressable

**Bus de contrôle :**
- Signaux de synchronisation
- Signaux de lecture/écriture

### Schéma de l'architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PROCESSEUR (CPU)                        │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │ Unité de Contrôle│    │  Unité Arithmétique et Logique │ │
│  │      (UC)       │    │            (UAL)               │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                  REGISTRES                             │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┼─────────┐
                    │    BUS SYSTÈME    │
                    └─────────┼─────────┘
                              │
┌─────────────────┐  ┌─────────┼─────────┐  ┌─────────────────┐
│    MÉMOIRE      │  │                   │  │   ENTRÉES/      │
│   PRINCIPALE    │  │                   │  │    SORTIES      │
│     (RAM)       │  │                   │  │                 │
└─────────────────┘  └───────────────────┘  └─────────────────┘
```

---

## Le processeur en détail

### Cycle d'exécution des instructions

#### Cycle Fetch-Decode-Execute

1. **FETCH (Recherche) :**
   - Lecture de l'instruction en mémoire
   - Adresse donnée par le compteur de programme (PC)
   - Instruction chargée dans le registre d'instruction (IR)

2. **DECODE (Décodage) :**
   - Analyse de l'instruction
   - Identification de l'opération à effectuer
   - Détermination des opérandes

3. **EXECUTE (Exécution) :**
   - Réalisation de l'opération
   - Mise à jour des registres
   - Calcul de l'adresse de la prochaine instruction

#### Exemple détaillé

```assembly
; Instruction : ADD R1, R2, R3  (R1 = R2 + R3)

1. FETCH:
   - PC contient l'adresse de l'instruction
   - Lecture de l'instruction en mémoire
   - Chargement dans IR
   - PC = PC + 1

2. DECODE:
   - Identification : opération ADD
   - Opérandes : R2 et R3 (sources), R1 (destination)
   - Préparation des chemins de données

3. EXECUTE:
   - Lecture des valeurs de R2 et R3
   - Addition dans l'UAL
   - Stockage du résultat dans R1
   - Mise à jour des flags (zéro, carry, etc.)
```

### Registres du processeur

#### Types de registres

**Registres généraux :**
- Stockage temporaire des données
- Utilisés par les instructions arithmétiques
- Exemple : R0, R1, R2, ..., R15

**Registres spéciaux :**

**Compteur de Programme (PC) :**
- Adresse de la prochaine instruction
- Modifié automatiquement ou par les branchements

**Registre d'Instruction (IR) :**
- Contient l'instruction en cours d'exécution
- Utilisé par l'unité de décodage

**Pointeur de Pile (SP) :**
- Adresse du sommet de la pile
- Utilisé pour les appels de fonctions

**Registre d'État (SR/FLAGS) :**
- Indicateurs du résultat des opérations
- Zero (Z), Carry (C), Negative (N), Overflow (V)

#### Exemple d'utilisation

```python
# Simulation simple d'un processeur
class ProcesseurSimple:
    def __init__(self):
        # Registres généraux
        self.registres = [0] * 16  # R0 à R15
        
        # Registres spéciaux
        self.pc = 0        # Compteur de programme
        self.ir = 0        # Registre d'instruction
        self.sp = 1000     # Pointeur de pile
        self.flags = {
            'zero': False,
            'carry': False,
            'negative': False,
            'overflow': False
        }
        
        # Mémoire simulée
        self.memoire = [0] * 1024
    
    def fetch(self):
        """Étape FETCH : récupère l'instruction"""
        self.ir = self.memoire[self.pc]
        self.pc += 1
        return self.ir
    
    def decode(self, instruction):
        """Étape DECODE : décode l'instruction"""
        # Format simple : OPCODE(4 bits) | REG1(4 bits) | REG2(4 bits) | REG3(4 bits)
        opcode = (instruction >> 12) & 0xF
        reg1 = (instruction >> 8) & 0xF
        reg2 = (instruction >> 4) & 0xF
        reg3 = instruction & 0xF
        
        return opcode, reg1, reg2, reg3
    
    def execute(self, opcode, reg1, reg2, reg3):
        """Étape EXECUTE : exécute l'instruction"""
        if opcode == 1:  # ADD
            resultat = self.registres[reg2] + self.registres[reg3]
            self.registres[reg1] = resultat & 0xFFFF  # Limitation 16 bits
            self.mettre_a_jour_flags(resultat)
            
        elif opcode == 2:  # SUB
            resultat = self.registres[reg2] - self.registres[reg3]
            self.registres[reg1] = resultat & 0xFFFF
            self.mettre_a_jour_flags(resultat)
            
        elif opcode == 3:  # LOAD
            adresse = self.registres[reg2] + reg3  # Adressage indexé
            self.registres[reg1] = self.memoire[adresse]
            
        elif opcode == 4:  # STORE
            adresse = self.registres[reg2] + reg3
            self.memoire[adresse] = self.registres[reg1]
            
        elif opcode == 5:  # JUMP
            self.pc = self.registres[reg1]
    
    def mettre_a_jour_flags(self, resultat):
        """Met à jour les flags selon le résultat"""
        self.flags['zero'] = (resultat == 0)
        self.flags['negative'] = (resultat < 0)
        self.flags['carry'] = (resultat > 0xFFFF)
        # Overflow pour addition/soustraction signée
    
    def cycle(self):
        """Un cycle complet d'exécution"""
        # FETCH
        instruction = self.fetch()
        
        # DECODE
        opcode, reg1, reg2, reg3 = self.decode(instruction)
        
        # EXECUTE
        self.execute(opcode, reg1, reg2, reg3)
    
    def executer_programme(self, programme):
        """Exécute un programme complet"""
        # Charger le programme en mémoire
        for i, instruction in enumerate(programme):
            self.memoire[i] = instruction
        
        self.pc = 0
        
        # Exécuter jusqu'à instruction HALT (0)
        while self.memoire[self.pc] != 0:
            self.cycle()
            print(f"PC: {self.pc-1}, Registres: {self.registres[:4]}")

# Exemple d'utilisation
if __name__ == "__main__":
    cpu = ProcesseurSimple()
    
    # Programme : calculer 5 + 3 et stocker en mémoire
    programme = [
        0x1012,  # ADD R0, R1, R2  (R0 = R1 + R2)
        0x4003,  # STORE R0, R0, 3 (mémoire[3] = R0)
        0x0000   # HALT
    ]
    
    # Initialiser les registres
    cpu.registres[1] = 5  # R1 = 5
    cpu.registres[2] = 3  # R2 = 3
    
    print("Avant exécution:")
    print(f"R1 = {cpu.registres[1]}, R2 = {cpu.registres[2]}")
    
    cpu.executer_programme(programme)
    
    print("\nAprès exécution:")
    print(f"R0 = {cpu.registres[0]}")
    print(f"Mémoire[3] = {cpu.memoire[3]}")
```

---

## Hiérarchie mémoire

### Principe de localité

**Localité temporelle :**
- Les données récemment utilisées ont plus de chances d'être réutilisées
- Exemple : variables dans une boucle

**Localité spatiale :**
- Les données proches de celles utilisées ont plus de chances d'être utilisées
- Exemple : éléments consécutifs d'un tableau

### Niveaux de mémoire

```
┌─────────────────┐  ←── Plus rapide, plus cher, plus petit
│    REGISTRES    │
├─────────────────┤
│   CACHE L1      │
├─────────────────┤
│   CACHE L2      │
├─────────────────┤
│   CACHE L3      │
├─────────────────┤
│  MÉMOIRE VIVE   │
│     (RAM)       │
├─────────────────┤
│  MÉMOIRE FLASH  │
│     (SSD)       │
├─────────────────┤
│  DISQUE DUR     │
│     (HDD)       │
└─────────────────┘  ←── Plus lent, moins cher, plus grand
```

#### Caractéristiques par niveau

| Niveau | Capacité | Temps d'accès | Coût/Go |
|--------|----------|---------------|----------|
| Registres | 32-64 octets | 0.1 ns | Très élevé |
| Cache L1 | 32-64 Ko | 1 ns | Élevé |
| Cache L2 | 256 Ko-1 Mo | 3-10 ns | Élevé |
| Cache L3 | 8-32 Mo | 10-20 ns | Moyen |
| RAM | 4-64 Go | 50-100 ns | Moyen |
| SSD | 256 Go-4 To | 0.1-1 ms | Bas |
| HDD | 1-20 To | 5-10 ms | Très bas |

### Mémoire cache

#### Principe de fonctionnement

**Cache hit :**
- Donnée trouvée dans le cache
- Accès rapide

**Cache miss :**
- Donnée non trouvée dans le cache
- Chargement depuis le niveau inférieur
- Mise en cache pour les accès futurs

#### Politiques de remplacement

**LRU (Least Recently Used) :**
- Remplace la donnée la moins récemment utilisée
- Exploite la localité temporelle

**FIFO (First In, First Out) :**
- Remplace la donnée la plus ancienne
- Simple à implémenter

**Random :**
- Remplacement aléatoire
- Évite les cas pathologiques

#### Simulation d'un cache simple

```python
class CacheSimple:
    def __init__(self, taille, politique='LRU'):
        self.taille = taille
        self.politique = politique
        self.donnees = {}  # adresse -> valeur
        self.ordre_acces = []  # Pour LRU
        self.hits = 0
        self.misses = 0
    
    def lire(self, adresse, memoire_principale):
        """Lit une donnée (cache ou mémoire principale)"""
        if adresse in self.donnees:
            # Cache hit
            self.hits += 1
            if self.politique == 'LRU':
                self.ordre_acces.remove(adresse)
                self.ordre_acces.append(adresse)
            return self.donnees[adresse]
        else:
            # Cache miss
            self.misses += 1
            valeur = memoire_principale.get(adresse, 0)
            self.ajouter_au_cache(adresse, valeur)
            return valeur
    
    def ajouter_au_cache(self, adresse, valeur):
        """Ajoute une donnée au cache"""
        if len(self.donnees) >= self.taille:
            # Cache plein, remplacer selon la politique
            if self.politique == 'LRU':
                adresse_a_remplacer = self.ordre_acces.pop(0)
            elif self.politique == 'FIFO':
                adresse_a_remplacer = min(self.donnees.keys())
            
            del self.donnees[adresse_a_remplacer]
        
        self.donnees[adresse] = valeur
        if self.politique == 'LRU':
            self.ordre_acces.append(adresse)
    
    def taux_hit(self):
        """Calcule le taux de succès du cache"""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0
    
    def afficher_stats(self):
        """Affiche les statistiques du cache"""
        print(f"Hits: {self.hits}, Misses: {self.misses}")
        print(f"Taux de hit: {self.taux_hit():.2%}")
        print(f"Contenu du cache: {self.donnees}")

# Simulation
if __name__ == "__main__":
    # Mémoire principale simulée
    memoire = {i: i*2 for i in range(100)}  # Adresse i contient valeur i*2
    
    # Cache de taille 4
    cache = CacheSimple(4, 'LRU')
    
    # Séquence d'accès
    accès = [1, 2, 3, 4, 1, 5, 6, 1, 2, 7]
    
    print("Simulation d'accès mémoire avec cache:")
    for adresse in accès:
        valeur = cache.lire(adresse, memoire)
        print(f"Lecture adresse {adresse}: valeur {valeur}")
        cache.afficher_stats()
        print()
```

---

## Parallélisme et performance

### Pipeline d'instructions

#### Principe
Le pipeline permet d'exécuter plusieurs instructions en parallèle en décomposant l'exécution en étapes.

#### Étapes du pipeline

1. **IF (Instruction Fetch)** : Lecture de l'instruction
2. **ID (Instruction Decode)** : Décodage et lecture des registres
3. **EX (Execute)** : Exécution de l'opération
4. **MEM (Memory Access)** : Accès mémoire si nécessaire
5. **WB (Write Back)** : Écriture du résultat

#### Exemple de pipeline

```
Temps:    1    2    3    4    5    6    7    8
Instr1:  [IF] [ID] [EX] [MEM] [WB]
Instr2:       [IF] [ID] [EX] [MEM] [WB]
Instr3:            [IF] [ID] [EX] [MEM] [WB]
Instr4:                 [IF] [ID] [EX] [MEM] [WB]
```

**Sans pipeline :** 4 instructions × 5 cycles = 20 cycles
**Avec pipeline :** 5 + 3 = 8 cycles (gain de 2.5×)

#### Aléas du pipeline

**Aléas de données :**
```assembly
ADD R1, R2, R3  ; R1 = R2 + R3
SUB R4, R1, R5  ; R4 = R1 - R5 (dépend de R1)
```

**Solutions :**
- Forwarding (transmission anticipée)
- Insertion de bulles (stalls)
- Réorganisation du code

**Aléas de contrôle :**
```assembly
BEQ R1, R2, LABEL  ; Branchement conditionnel
ADD R3, R4, R5     ; Instruction suivante
```

**Solutions :**
- Prédiction de branchement
- Exécution spéculative
- Branch delay slots

### Architectures multi-cœurs

#### Types de parallélisme

**Parallélisme au niveau instruction (ILP) :**
- Exécution simultanée d'instructions indépendantes
- Processeurs superscalaires
- Exécution dans le désordre

**Parallélisme au niveau thread (TLP) :**
- Plusieurs threads par cœur
- Hyperthreading/SMT
- Masquage des latences

**Parallélisme au niveau processus :**
- Plusieurs cœurs indépendants
- Mémoire partagée ou distribuée
- Communication par messages

#### Exemple de programmation parallèle

```python
import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def calcul_intensif(n):
    """Fonction simulant un calcul intensif"""
    total = 0
    for i in range(n):
        total += i * i
    return total

def mesurer_performance():
    """Compare les performances séquentiel vs parallèle"""
    taches = [1000000] * 8  # 8 tâches identiques
    
    # Exécution séquentielle
    start = time.time()
    resultats_seq = [calcul_intensif(n) for n in taches]
    temps_seq = time.time() - start
    
    # Exécution parallèle avec threads
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        resultats_thread = list(executor.map(calcul_intensif, taches))
    temps_thread = time.time() - start
    
    # Exécution parallèle avec processus
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        resultats_process = list(executor.map(calcul_intensif, taches))
    temps_process = time.time() - start
    
    print(f"Séquentiel: {temps_seq:.2f}s")
    print(f"Threads: {temps_thread:.2f}s (speedup: {temps_seq/temps_thread:.1f}x)")
    print(f"Processus: {temps_process:.2f}s (speedup: {temps_seq/temps_process:.1f}x)")
    
    # Vérifier que les résultats sont identiques
    assert resultats_seq == resultats_thread == resultats_process

if __name__ == "__main__":
    mesurer_performance()
```

---

## Architectures spécialisées

### Processeurs graphiques (GPU)

#### Caractéristiques
- Milliers de cœurs simples
- Optimisés pour le parallélisme massif
- Mémoire haute bande passante
- Architecture SIMD (Single Instruction, Multiple Data)

#### Applications
- Rendu graphique
- Calcul scientifique
- Intelligence artificielle
- Cryptomonnaies

#### Exemple de calcul GPU (conceptuel)

```python
# Simulation d'un calcul parallèle sur GPU
class GPUSimule:
    def __init__(self, nb_coeurs=1024):
        self.nb_coeurs = nb_coeurs
    
    def addition_vecteurs(self, a, b):
        """Addition de deux vecteurs en parallèle"""
        if len(a) != len(b):
            raise ValueError("Les vecteurs doivent avoir la même taille")
        
        # Simulation : chaque cœur traite un élément
        resultat = [0] * len(a)
        
        # En réalité, ceci se ferait en parallèle sur le GPU
        for i in range(len(a)):
            resultat[i] = a[i] + b[i]
        
        return resultat
    
    def produit_matriciel(self, A, B):
        """Produit matriciel parallèle"""
        n, m = len(A), len(B[0])
        C = [[0] * m for _ in range(n)]
        
        # Chaque cœur calcule un élément de la matrice résultat
        for i in range(n):
            for j in range(m):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        
        return C

# Exemple d'utilisation
gpu = GPUSimule()
vecteur_a = list(range(1000))
vecteur_b = list(range(1000, 2000))
resultat = gpu.addition_vecteurs(vecteur_a, vecteur_b)
print(f"Premier élément du résultat: {resultat[0]}")  # 0 + 1000 = 1000
```

### Processeurs embarqués

#### Caractéristiques
- Faible consommation
- Taille réduite
- Fonctionnalités spécialisées
- Contraintes temps réel

#### Applications
- Internet des objets (IoT)
- Systèmes automobiles
- Appareils médicaux
- Domotique

### Architectures quantiques

#### Principes
- Qubits (bits quantiques)
- Superposition d'états
- Intrication quantique
- Parallélisme quantique

#### Avantages potentiels
- Factorisation d'entiers (cryptographie)
- Simulation quantique
- Optimisation
- Intelligence artificielle

---

## Mesure des performances

### Métriques importantes

#### Fréquence d'horloge
- Nombre de cycles par seconde (Hz)
- Ne détermine pas seule la performance
- Dépend de l'architecture

#### Instructions par cycle (IPC)
- Efficacité du processeur
- Varie selon le type d'instructions
- Impactée par les aléas du pipeline

#### Débit (Throughput)
- Nombre d'opérations par unité de temps
- Important pour les serveurs
- Mesure la capacité globale

#### Latence
- Temps pour compléter une opération
- Important pour l'interactivité
- Difficile à réduire

### Lois de performance

#### Loi d'Amdahl
**Énoncé :** Le gain de performance d'un système parallèle est limité par la partie séquentielle du programme.

**Formule :**
```
Speedup = 1 / (s + (1-s)/p)
```
- s = fraction séquentielle
- p = nombre de processeurs

**Exemple :**
```python
def loi_amdahl(fraction_sequentielle, nb_processeurs):
    """Calcule le speedup selon la loi d'Amdahl"""
    return 1 / (fraction_sequentielle + (1 - fraction_sequentielle) / nb_processeurs)

# Exemples
print(f"10% séquentiel, 4 processeurs: {loi_amdahl(0.1, 4):.2f}x")
print(f"10% séquentiel, 8 processeurs: {loi_amdahl(0.1, 8):.2f}x")
print(f"50% séquentiel, 4 processeurs: {loi_amdahl(0.5, 4):.2f}x")
```

#### Loi de Moore
**Énoncé original :** Le nombre de transistors double tous les 18-24 mois.

**Évolution :**
- Ralentissement depuis 2005
- Limites physiques atteintes
- Focus sur l'efficacité énergétique
- Architectures spécialisées

---

## Optimisation des performances

### Techniques logicielles

#### Optimisation du code

```python
# Exemple : optimisation d'accès mémoire

# Version non optimisée (mauvaise localité)
def somme_matrice_lente(matrice):
    total = 0
    n, m = len(matrice), len(matrice[0])
    
    # Accès par colonnes (mauvais pour le cache)
    for j in range(m):
        for i in range(n):
            total += matrice[i][j]
    
    return total

# Version optimisée (bonne localité)
def somme_matrice_rapide(matrice):
    total = 0
    
    # Accès par lignes (bon pour le cache)
    for ligne in matrice:
        for element in ligne:
            total += element
    
    return total

# Test de performance
import time
import random

# Créer une grande matrice
n, m = 1000, 1000
matrice = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

# Mesurer les performances
start = time.time()
resultat1 = somme_matrice_lente(matrice)
temps1 = time.time() - start

start = time.time()
resultat2 = somme_matrice_rapide(matrice)
temps2 = time.time() - start

print(f"Version lente: {temps1:.3f}s")
print(f"Version rapide: {temps2:.3f}s")
print(f"Speedup: {temps1/temps2:.1f}x")
assert resultat1 == resultat2
```

#### Utilisation efficace du cache

```python
# Multiplication matricielle optimisée pour le cache
def multiplication_matrices_optimisee(A, B, taille_bloc=64):
    """Multiplication par blocs pour optimiser l'usage du cache"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    # Multiplication par blocs
    for i0 in range(0, n, taille_bloc):
        for j0 in range(0, n, taille_bloc):
            for k0 in range(0, n, taille_bloc):
                # Multiplication du bloc
                for i in range(i0, min(i0 + taille_bloc, n)):
                    for j in range(j0, min(j0 + taille_bloc, n)):
                        for k in range(k0, min(k0 + taille_bloc, n)):
                            C[i][j] += A[i][k] * B[k][j]
    
    return C
```

### Techniques matérielles

#### Prédiction de branchement
- Prédicteurs statiques
- Prédicteurs dynamiques
- Prédicteurs à deux niveaux

#### Exécution spéculative
- Exécution avant confirmation
- Annulation si prédiction fausse
- Gain sur les branchements fréquents

#### Renommage de registres
- Élimination des dépendances artificielles
- Augmentation du parallélisme
- Complexité matérielle

---

## Exercices pratiques

### Exercice 1 : Simulation de cache
Implémentez un simulateur de cache avec différentes politiques de remplacement et mesurez l'impact sur les performances.

### Exercice 2 : Analyse de pipeline
Analysez les aléas dans une séquence d'instructions et proposez des optimisations.

### Exercice 3 : Parallélisation
Parallélisez un algorithme de tri et mesurez le speedup obtenu.

### Exercice 4 : Optimisation mémoire
Optimisez l'accès mémoire dans un algorithme de traitement d'images.

---

## Conclusion

L'architecture matérielle influence directement les performances des programmes. Comprendre ces concepts permet :

- **Optimisation** : Écrire du code plus efficace
- **Choix technologiques** : Sélectionner le matériel approprié
- **Prédiction** : Anticiper les goulots d'étranglement
- **Innovation** : Concevoir de nouvelles architectures

L'évolution vers le parallélisme massif et les architectures spécialisées redéfinit les défis de l'informatique moderne.
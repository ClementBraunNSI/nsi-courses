# Fiche d'exercices : Encodage des caractères

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
      2. b'\xce\xa9  
      3. b'\xe3\x81\x93'  

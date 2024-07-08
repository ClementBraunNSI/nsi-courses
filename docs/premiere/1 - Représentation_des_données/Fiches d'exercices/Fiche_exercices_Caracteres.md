# Fiche d'exercices : Encodage des caractères

## Encodage en table ASCII

1. Décoder les messages suivants en hexadécimal à l'aide de la table ASCII
   a. `48 65 6C 6C 6F`
   b. `57 6F 72 6C 64`
   c. `31 32 33 34 35`

2. Encoder les messages suivants à l'aide de la table ASCII
   a. `Hello`
   b. `123`
   c. `!@#`
   d. `Code`

3. Python permet d'encoder des messages à l'aide de divers encodages. Il existe la méthode `encode` des chaînes de caractères. Elle s'utilise de cette manière chaine_de_caractere.encode('Méthode d'encodage').
   a. Instancier la chaîne de caractère : *La vitesse de la lumière est de 300 000km/s*.
   b. Que se passe-t-il si l'on veut afficher l'encodage en ASCII de cette chaîne de caractère? Comment l'expliquer?

4. La méthode `decode` de Python permet de donner le caractère associé à un point de code donné. Cela s'utilise de cette manière : chaine_de_caractere.decode('Méthode de décodage'). Donner les caractères associés à ces points de code :
   a. b'\x41'
   b. b'\xce\xa9
   c. b'\xe3\x81\x93'

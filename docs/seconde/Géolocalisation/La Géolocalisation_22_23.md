# La Géolocalisation



### 1 - Notions Géographiques

1 - Compléter le paragraphe suivant avec les mots suivants: géolocalisation, longitude, satellite, altitude, latitude, GPS

Indiquer quel schéma représente la latitude et lequel représente la longitude.

La ....(géolocalisation).................... est une technique permettant de situer de manière précise un lieu, une personne, un objet sur la planète. Pour se faire, on doit connaître au moins trois coordonnées géographiques.

La .......(latitude)................... est la mesure de l'angle formé entre le point extrême de l'équateur, le centre de la terre et la position de ce que l'on cherche à localiser exprimée en degrés. La  .......(longitude)................... est une mesure faite par rapport à un des méridien de la Terre sur 360° exprimée en degrés. L' .......(altitude)................... est la hauteur du point maximal de l'objet que l'on cherche à situer par rapport au niveau 0 de la mer, elle est exprimée en mètres.



<img src="im1.png" style="zoom:33%" /><img src="im2.png" alt="image-20230320173930303" style="zoom:33%;" /><img src="im3.png" alt="image-20230320181747753" style="zoom:50%;" />



Cette géolocalisation est permise grâce à un système mondialement connu le **GPS (Global Positioning System)**. Le .......(GPS)....... a été développé en 1960 par l'armée américaine mais le premier satellite GPS a été envoyé dans l'espace en dans les années 1980. D'autres systèmes ont été mis en place par d'autres pays et notamment **Galileo** le système de navigation européen qui est plus précis que son homologue américain.

Par exemple, la position de la ville de Paris est **48.8588897 (latitude) et 2.320041 (longitude)**.

__________



### 2 - La trilatération



<img src="https://gisgeography.com/wp-content/uploads/2016/11/Trilateration-4.png" alt="How GPS Receivers Work - Trilateration vs Triangulation - GIS Geography" style="zoom:30%;" />



La **trilatération** est l'utilisation de 3 satellites pour déterminer une position. À intervalles réguliers, plusieurs satellites emettent des ............(signaux)....... sur la Terre. Les .......(récepteurs)....... GPS placés dans nos divers ......(appareils)...... domestiques ou personnels reçoivent ces signaux et cela permet de localiser plus ou moins précisément ce que l'on chercahe.

Cependant, il faut noter l'utilisation d'un quatrième satellite qui sert à la synchronisation des autres pour éviter de mauvais envois de signaux (comme un diapason).



### 3 - Le protocole NMEA-0183

Le protocole NMEA-0183 est un protocole mis en place par la National Marine Electronics Association (NMEA). Ce protocole permet de fournir la localisation d'un objet ou d'une personne en trames facilement décodables.

Généralement, on exprime les coordonnées géographiques dans le système sexagésimal, noté DMS pour degrés, minutes, secondes. Par exemple 49°30'30'' pour 49 degrés, 30 minutes et 30 secondes. Une minute d'angle vaut 1/60 degrés tandis qu'une seconde d'angle vaut 1/3600 degrés.

Un exemple de trame NMEA-0183 :

- **GPGGA** : type de la trame
- **064036.289** : heure d'envoi de la trame, ici 06h 40min 36,289s (UTC)
- **4836.5375, N** : latitude Nord, ici 48°36,5375' (en degrés minutes)
- **00740.9373, E** : longitude Est, ici 7°40,9373' (en degrés minutes)
- **1** : type de positionnement (1 pour le positionnement GPS)
- **04** : nombre de satellites utilisés
- **3.2** : précision horizontale
- **200.2, M** : altitude, ici 200 mètres

```
$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E
```

Cette trame NMEA donne la localisation de Paris.



### Exercices : 

#### Les coordonnées GPS

1. Sur votre téléphone ou sur Google Maps, retrouvez les coordonnées GPS du lycée.

	
	
2. Voici des coordonnées GPS : , donnez le nombre de restaurants et de boutiques aux alentours.

	
	
3. Retrouver les coordonnées GPS des lieux où ont été prises les photos fournies en annexe grâce aux propriétés de celles-ci et donner les lieux où elles ont été prises.

	
	
4. Donnez les coordonnées GPS de la Tour Eiffel à Paris et de la Statue de la Liberté à New York. Calculez la distance entre ces deux lieux en kilomètres en utilisant de l'outil lexilogos[^1].




[^1]:https://www.lexilogos.com/calcul_distances.htm



#### Décoder des trames NMEA

A l'aide du site https://rl.se/gprmc, donner la ville dont la localisation est donnée par les trames NMEA suivantes :

```
$GPGGA,175737.303,4449.833,N,00034.772,W,1,04,1.0,0.0,M,0.0,M,,*7C

$GPGGA,175736.303,5038.047,N,00303.695,E,1,03,1.0,0.0,M,0.0,M,,*68

$GPGGA,175738.303,4545.175,N,00450.039,E,1,12,1.0,0.0,M,0.0,M,,*69
```

On va utiliser la trame

```
$GPGGA,175736.303,4533.786,N,00554.803,E,1,05,1.0,154.3,M,0.0,M,,*68
```

*Combien de satellites ont été utilisés ?_________________________________________________*

*A quelle hauteur est située l'objet? _________________________________________________*

*A quelle ville correspondent ces coordonnées : 41.921; 8.735 ?* 



### Activités sur Algorea

Localisation d'un point gràce à la latitude et la longitude sur la planète  :

https://parcours.algorea.org/contents/4707-4702-1067253748629066205-183305583351435935-1207970506541061357-237778358454750514-380941821572110134/

La trilatération concrètement:

https://parcours.algorea.org/contents/4707-4702-1067253748629066205-183305583351435935-1207970506541061357-237778358454750514-88752303685492924/

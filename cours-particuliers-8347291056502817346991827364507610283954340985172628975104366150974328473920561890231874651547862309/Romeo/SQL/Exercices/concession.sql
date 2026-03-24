-- Création de la table Voitures
CREATE TABLE IF NOT EXISTS Voitures (
    id INTEGER PRIMARY KEY,
    marque TEXT,
    modele TEXT,
    couleur TEXT,
    annee INTEGER,
    prix INTEGER,
    kilometrage INTEGER
);

-- Insertion des données
INSERT INTO Voitures (id, marque, modele, couleur, annee, prix, kilometrage) VALUES
(1, 'Renault', 'Clio', 'Rouge', 2018, 12000, 45000),
(2, 'Peugeot', '208', 'Blanc', 2020, 15000, 20000),
(3, 'Tesla', 'Model 3', 'Noir', 2022, 35000, 10000),
(4, 'Renault', 'Mégane', 'Bleu', 2015, 8000, 120000),
(5, 'Porsche', '911', 'Gris', 2019, 95000, 15000);

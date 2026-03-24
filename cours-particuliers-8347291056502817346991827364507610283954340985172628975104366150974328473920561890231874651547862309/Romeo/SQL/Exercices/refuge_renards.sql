-- Création de la table Enclos
CREATE TABLE IF NOT EXISTS Enclos (
    id INTEGER PRIMARY KEY,
    nom_enclos TEXT,
    surface_m2 INTEGER,
    type_sol TEXT
);

-- Insertion des données Enclos
INSERT INTO Enclos (id, nom_enclos, surface_m2, type_sol) VALUES
(1, 'La Forêt', 500, 'Terre'),
(2, 'La Plaine', 300, 'Herbe'),
(3, 'La Tanière', 50, 'Sable');

-- Création de la table Renards
CREATE TABLE IF NOT EXISTS Renards (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    sexe TEXT,
    age INTEGER,
    id_enclos INTEGER,
    FOREIGN KEY (id_enclos) REFERENCES Enclos(id)
);

-- Insertion des données Renards
INSERT INTO Renards (id, nom, sexe, age, id_enclos) VALUES
(1, 'Rusty', 'M', 3, 1),
(2, 'Vixey', 'F', 2, 1),
(3, 'Zorro', 'M', 5, 2),
(4, 'Luna', 'F', 1, 3),
(5, 'Shadow', 'M', 4, NULL);

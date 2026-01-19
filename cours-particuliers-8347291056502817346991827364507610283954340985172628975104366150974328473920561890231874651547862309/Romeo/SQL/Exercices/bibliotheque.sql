-- Création de la table Livres
CREATE TABLE IF NOT EXISTS Livres (
    id INTEGER PRIMARY KEY,
    titre TEXT,
    auteur TEXT,
    annee_publication INTEGER,
    genre TEXT,
    disponible INTEGER -- 1 pour Oui, 0 pour Non
);

-- Insertion des données
INSERT INTO Livres (id, titre, auteur, annee_publication, genre, disponible) VALUES
(1, '1984', 'George Orwell', 1949, 'SF', 1),
(2, 'Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 0),
(3, 'Dune', 'Frank Herbert', 1965, 'SF', 1),
(4, 'Les Misérables', 'Victor Hugo', 1862, 'Roman', 1),
(5, 'Fondation', 'Isaac Asimov', 1951, 'SF', 0);

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import SecondePage from './pages/SecondePage';
import PremierePage from './pages/PremierePage';
import TerminalePage from './pages/TerminalePage';
import CourseViewer from './components/CourseViewer';
import ExercisePage from './pages/ExercisePage';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/seconde" element={<SecondePage />} />
            <Route path="/premiere" element={<PremierePage />} />
            <Route path="/terminale" element={<TerminalePage />} />
            <Route path="/exercises/:exerciseId" element={<ExercisePage />} />
            
            {/* Routes pour les cours de seconde */}
            <Route path="/seconde/I_-_Internet/:course" element={<CourseViewer level="seconde" chapter="I_-_Internet" />} />
            <Route path="/seconde/II_-_Web/:course" element={<CourseViewer level="seconde" chapter="II_-_Web" />} />
            <Route path="/seconde/III_-_Reseaux_sociaux/:course" element={<CourseViewer level="seconde" chapter="III_-_Reseaux_sociaux" />} />
            <Route path="/seconde/IIII_-_Programmation_Python/:course" element={<CourseViewer level="seconde" chapter="IIII_-_Programmation_Python" />} />
            <Route path="/seconde/V_-_Photographie_Numerique/:course" element={<CourseViewer level="seconde" chapter="V_-_Photographie_Numerique" />} />
            <Route path="/seconde/VI_-_Geolocalisation/:course" element={<CourseViewer level="seconde" chapter="VI_-_Geolocalisation" />} />
            <Route path="/seconde/VII_-_Donnees_Structurees/:course" element={<CourseViewer level="seconde" chapter="VII_-_Donnees_Structurees" />} />
            <Route path="/seconde/VIII_-_Objets_Connectes/:course" element={<CourseViewer level="seconde" chapter="VIII_-_Objets_Connectes" />} />
            
            {/* Routes pour les cours de première */}
            <Route path="/premiere/I-Constructions_elementaires/:course" element={<CourseViewer level="premiere" chapter="I-Constructions_elementaires" />} />
            <Route path="/premiere/II-Representation_des_donnees/:course" element={<CourseViewer level="premiere" chapter="II-Representation_des_donnees" />} />
            <Route path="/premiere/III-Structures_de_donnees_lineaires/:course" element={<CourseViewer level="premiere" chapter="III-Structures_de_donnees_lineaires" />} />
            <Route path="/premiere/IV-Architecture_d_une_machine/:course" element={<CourseViewer level="premiere" chapter="IV-Architecture_d_une_machine" />} />
            <Route path="/premiere/V-Dictionnaires_et_Traitement_de_tables/:course" element={<CourseViewer level="premiere" chapter="V-Dictionnaires_et_Traitement_de_tables" />} />
            <Route path="/premiere/VI-Internet_et_Reseaux/:course" element={<CourseViewer level="premiere" chapter="VI-Internet_et_Reseaux" />} />
            <Route path="/premiere/VII-Algorithmes_sur_les_tableaux/:course" element={<CourseViewer level="premiere" chapter="VII-Algorithmes_sur_les_tableaux" />} />
            <Route path="/premiere/VIII-Algorithmes_Gloutons/:course" element={<CourseViewer level="premiere" chapter="VIII-Algorithmes_Gloutons" />} />
            <Route path="/premiere/VIIII-Systemes_d_exploitation_et_commandes_Linux/:course" element={<CourseViewer level="premiere" chapter="VIIII-Systemes_d_exploitation_et_commandes_Linux" />} />
            <Route path="/premiere/X-Web_et_HTTP/:course" element={<CourseViewer level="premiere" chapter="X-Web_et_HTTP" />} />
            <Route path="/premiere/XI-K_plus_proches_voisins/:course" element={<CourseViewer level="premiere" chapter="XI-K_plus_proches_voisins" />} />
            <Route path="/premiere/XII-Pour_aller_plus_loin/:course" element={<CourseViewer level="premiere" chapter="XII-Pour_aller_plus_loin" />} />
            <Route path="/premiere/XIII-Projets/:course" element={<CourseViewer level="premiere" chapter="XIII-Projets" />} />
            <Route path="/premiere/New_Year_Advent/:course" element={<CourseViewer level="premiere" chapter="New_Year_Advent" />} />
            <Route path="/premiere/Aides/:course" element={<CourseViewer level="premiere" chapter="Aides" />} />
            
            {/* Routes pour les cours de terminale */}
            <Route path="/terminale/I-Rappels/:course" element={<CourseViewer level="terminale" chapter="I-Rappels" />} />
            <Route path="/terminale/II-Structures_de_donnees/:course" element={<CourseViewer level="terminale" chapter="II-Structures_de_donnees" />} />
            <Route path="/terminale/III-Bases_de_donnees/:course" element={<CourseViewer level="terminale" chapter="III-Bases_de_donnees" />} />
            <Route path="/terminale/IV-Architectures_et_reseaux/:course" element={<CourseViewer level="terminale" chapter="IV-Architectures_et_reseaux" />} />
            <Route path="/terminale/V-Langages_et_programmation/:course" element={<CourseViewer level="terminale" chapter="V-Langages_et_programmation" />} />
            <Route path="/terminale/VI-Algorithmique/:course" element={<CourseViewer level="terminale" chapter="VI-Algorithmique" />} />
            <Route path="/terminale/VII-Projets/:course" element={<CourseViewer level="terminale" chapter="VII-Projets" />} />
            <Route path="/terminale/VIII-Preparation_bac/:course" element={<CourseViewer level="terminale" chapter="VIII-Preparation_bac" />} />
          </Routes>
      </main>
    </div>
  );
}

export default App;
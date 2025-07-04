import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Home.css';

const Home = () => {
  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1 className="hero-title">
            Bienvenue sur le site de 
            <span className="highlight"> M. BRAUN.</span>
          </h1>
          <p className="hero-subtitle">
            Découvrez les Sciences Numériques et l'Informatique à travers des cours,
            des exercices pratiques et des projets.
          </p>
          <div className="hero-cta">
            <Link to="#levels" className="cta-button primary">
              Commencer l'aventure
            </Link>
          </div>
        </div>
        <div className="hero-visual">
          <div className="floating-elements">
            <div className="element element-1">🦊</div>
            <div className="element element-2">💻</div>
            <div className="element element-3">🔬</div>
            <div className="element element-4">🚀</div>
          </div>
        </div>
      </section>

      <section className="levels" id="levels">
        <div className="levels-container">
          <h2 className="section-title">Choisissez votre niveau</h2>
          <div className="levels-grid">
            <Link to="/seconde" className="level-card seconde">
              <div className="level-icon">
                <img src="/fox_seconde.png" alt="Seconde" />
              </div>
              <h3>Seconde SNT</h3>
              <p>Sciences Numériques et Technologie</p>
              <div className="level-topics">
                <span className="topic">Internet</span>
                <span className="topic">Web</span>
                <span className="topic">Réseaux sociaux</span>
                <span className="topic">Programmation Python</span>
              </div>
              <div className="level-arrow">→</div>
            </Link>

            <Link to="/premiere" className="level-card premiere">
              <div className="level-icon">
                <img src="/fox_premiere.png" alt="Première" />
              </div>
              <h3>Première NSI</h3>
              <p>Numérique et Sciences Informatiques</p>
              <div className="level-topics">
                <span className="topic">Algorithmes</span>
                <span className="topic">Structures de données</span>
                <span className="topic">Architecture</span>
                <span className="topic">Projets</span>
              </div>
              <div className="level-arrow">→</div>
            </Link>

            <Link to="/terminale" className="level-card terminale">
              <div className="level-icon">
                <img src="/fox_terminale.png" alt="Terminale" />
              </div>
              <h3>Terminale NSI</h3>
              <p>Approfondissement et Spécialisation</p>
              <div className="level-topics">
                <span className="topic">Bases de données</span>
                <span className="topic">Algorithmique avancée</span>
                <span className="topic">Réseaux</span>
                <span className="topic">Préparation BAC</span>
              </div>
              <div className="level-arrow">→</div>
            </Link>

            <Link to="www.chasse-aux-ren-arts.ovh" className="level-card premiere">
              <div className="level-icon">
                <img src="/chasserenarts.png" alt="chasse" />
              </div>
              <h3>Chasse aux ren'arts</h3>
              <p>Numérique et Sciences Informatiques</p>
              <div className="level-topics">
                <span className="topic">Algorithmes</span>
                <span className="topic">Structures de données</span>
                <span className="topic">Architecture</span>
                <span className="topic">Projets</span>
              </div>
              <div className="level-arrow">→</div>
            </Link>
          </div>
        </div>
      </section>

      <section className="bac-evaluation">
        <div className="bac-container">
          <h2 className="section-title">🎓 Évaluation au Baccalauréat NSI</h2>
          <p className="bac-description">
            Le baccalauréat NSI est composé de deux épreuves complémentaires évaluant les compétences théoriques et pratiques.
          </p>
          <div className="exam-grid">
            <div className="exam-card">
              <div className="exam-header">
                <div className="exam-icon">📝</div>
                <h3 className="exam-title">Épreuve Écrite</h3>
              </div>
              <div className="exam-details">
                <div className="detail-item">
                  <span className="detail-label">Durée</span>
                  <span className="detail-value">3h30</span>
                </div>
                <div className="detail-item">
                  <span className="detail-label">Exercices</span>
                  <span className="detail-value">3 exercices</span>
                </div>
                <div className="detail-item">
                  <span className="detail-label">Répartition</span>
                  <span className="detail-value">2×6pts + 1×8pts</span>
                </div>
              </div>
              <div className="weight-indicator">
                <span className="weight-fraction">3/4</span>
                <small>de la note finale</small>
              </div>
              <p className="exam-description">
                Épreuve théorique couvrant les concepts du cours, algorithmes et résolution de problèmes informatiques.
              </p>
            </div>
            
            <div className="exam-card">
              <div className="exam-header">
                <div className="exam-icon">💻</div>
                <h3 className="exam-title">Épreuve Pratique</h3>
              </div>
              <div className="exam-details">
                <div className="detail-item">
                  <span className="detail-label">Durée</span>
                  <span className="detail-value">1h00</span>
                </div>
                <div className="detail-item">
                  <span className="detail-label">Exercices</span>
                  <span className="detail-value">2 exercices</span>
                </div>
                <div className="detail-item">
                  <span className="detail-label">Sujets</span>
                  <span className="detail-value">~40 sujets</span>
                </div>
              </div>
              <div className="weight-indicator">
                <span className="weight-fraction">1/4</span>
                <small>de la note finale</small>
              </div>
              <p className="exam-description">
                Programmation sur machine : rédaction d'algorithme et complétion de code à trous.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="contributors">
        <div className="contributors-container">
          <h2 className="section-title">👥 Ont contribué à ce site</h2>
          <div className="contributors-grid">
            <div className="contributor">
              <div className="contributor-icon">🦊</div>
              <h3>BRAUN Clément</h3>
              <p>Enseignant d'informatique <br/>Lycée Paul Duez - Cambrai</p>
            </div>
            <div className="contributor">
              <div className="contributor-icon">💻</div>
              <h3>DELPLACE Nicolas</h3>
              <p>Enseignant d'informatique</p>
            </div>
            <div className="contributor">
              <div className="contributor-icon">🎓</div>
              <h3>RAMSTEIN Stéphane</h3>
              <p>Enseignant d'informatique<br />Lycée Raymond Queneau - Villeneuve d'Ascq</p>
            </div>
            <div className="contributor">
              <div className="contributor-icon">🏫</div>
              <h3>PAPEGAY Benoit</h3>
              <p>Enseignant à l'Université de Lille</p>
            </div>
            <div className="contributor">
              <div className="contributor-icon">🎯</div>
              <h3>MARCHAND Mathieu</h3>
              <p>Enseignant d'informatique<br />Lycée Benjamin Franklin</p>
            </div>
          </div>
        </div>
      </section>

      <section className="colleague-sites">
        <div className="colleague-sites-container">
          <h2 className="section-title">🌐 Sites de collègues de NSI</h2>
          <div className="sites-grid">
            <div className="site-card">
              <div className="site-icon">📚</div>
              <h3>RELMY Lucas</h3>
              <p>Ressources complètes et exercices pratiques pour NSI</p>
              <a href="https://lucasrelmynsi.gitlab.io/site_cours/" className="site-link">Visiter </a>
            </div>
            <div className="site-card">
              <div className="site-icon">🔬</div>
              <h3>DEMERVILLE Erwan</h3>
              <p>Cours détaillés et projets innovants en NSI</p>
              <a href="https://nsi.erwandemerville.fr" className="site-link" target="_blank" rel="noopener noreferrer">Visiter </a>
            </div>
            <div className="site-card">
              <div className="site-icon">⚡</div>
              <h3>RAMSTEIN Stéphane</h3>
              <p>Approche pédagogique moderne et interactive</p>
              <a href="https://stephane_ramstein.gitlab.io/nsi/" className="site-link" target="_blank" rel="noopener noreferrer">Visiter </a>
            </div>
            <div className="site-card">
              <div className="site-icon">🚀</div>
              <h3>MARCHAND Mathieu</h3>
              <p>Contenus avancés et méthodologie rigoureuse</p>
              <a href="https://mmarchand-nsi.github.io" className="site-link" target="_blank" rel="noopener noreferrer">Visiter </a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
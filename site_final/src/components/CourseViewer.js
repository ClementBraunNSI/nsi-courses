import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import '../styles/CourseViewer.css';

const CourseViewer = ({ level, chapter }) => {
  const { course } = useParams();
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fonction pour convertir le JSON en HTML
  const convertJsonToHtml = (jsonData) => {
    if (!jsonData || !jsonData.title || !jsonData.sections) {
      return '<div class="error">Format de données invalide</div>';
    }

    // Fonction pour convertir le texte Markdown en HTML basique
    const convertMarkdownToHtml = (text) => {
      if (!text) return '';
      
      let html = text;
      
      // Convertir les images ![alt](src)
      html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (match, alt, src) => {
        // Ajuster le chemin des images pour qu'il soit relatif au dossier public
        const imagePath = src.startsWith('img/') ? `/courses-json/images/${src.substring(4)}` : src;
        return `<img src="${imagePath}" alt="${alt}" class="course-image" />`;
      });
      
      // Convertir les tableaux markdown
      html = html.replace(/\|(.+)\|\n\|[-\s|:]+\|\n((\|.+\|\n?)+)/g, (match, header, separator, rows) => {
        const headerCells = header.split('|').map(cell => cell.trim()).filter(cell => cell);
        const rowLines = rows.trim().split('\n');
        
        let tableHtml = '<table class="markdown-table"><thead><tr>';
        headerCells.forEach(cell => {
          tableHtml += `<th>${cell}</th>`;
        });
        tableHtml += '</tr></thead><tbody>';
        
        rowLines.forEach(row => {
          if (row.trim()) {
            const cells = row.split('|').map(cell => cell.trim()).filter(cell => cell);
            tableHtml += '<tr>';
            cells.forEach(cell => {
              tableHtml += `<td>${cell}</td>`;
            });
            tableHtml += '</tr>';
          }
        });
        
        tableHtml += '</tbody></table>';
        return tableHtml;
      });
      
      // Convertir les blocs de code
      html = html.replace(/```([\s\S]*?)```/g, (match, code) => {
        return `<pre><code>${code.trim()}</code></pre>`;
      });
      
      // Convertir le code inline
      html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
      
      // Convertir le gras
      html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
      
      // Convertir l'italique
      html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');
      
      // Convertir les listes
      html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
      html = html.replace(/(<li>.+<\/li>\n?)+/g, '<ul>$&</ul>');
      
      // Convertir les liens [text](url)
      html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
      
      // Convertir les paragraphes et retours à la ligne
      html = html.replace(/\n\n/g, '</p><p>');
      html = html.replace(/\n/g, '<br>');
      
      return html;
    };

    // Générer le HTML pour le titre principal
    let htmlContent = `<h1>${jsonData.title}</h1>`;
    
    // Générer le HTML pour chaque section
    jsonData.sections.forEach(section => {
      if (section.title) {
        htmlContent += `<h2>${section.title}</h2>`;
      }
      
      if (section.content) {
        htmlContent += `<div class="section-content"><p>${convertMarkdownToHtml(section.content)}</p></div>`;
      }
    });
    
    return htmlContent;
  };

  useEffect(() => {
    const loadCourse = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Déterminer le format du chemin en fonction du niveau et du cours
        let coursePath;
        
        // Ajouter des logs pour déboguer
        console.log('Niveau:', level);
        console.log('Chapitre:', chapter);
        console.log('Cours:', course);
        
        try {
          if (level === 'seconde') {
            // Pour la seconde, les fichiers suivent le format: seconde_Cours_I_Internet.json
            // Extraire la partie principale du chapitre (ex: I_-_Internet -> I_Internet)
            const chapterMain = chapter.replace(/_-_/g, '_');
            coursePath = `/courses-json/${level}_${course}_${chapterMain}.json`;
          } else if (level === 'premiere' || level === 'terminale') {
            // Pour premiere/terminale, les fichiers suivent le format: premiere_NomDuCours.json
            // Le nom du cours contient déjà toutes les informations nécessaires
            coursePath = `/courses-json/${level}_${course}.json`;
          } else {
            throw new Error('Niveau non reconnu');
          }
        } catch (err) {
          console.error('Erreur lors de la construction du chemin:', err);
          throw new Error('Format de chemin invalide');
        }
        
        console.log('Tentative de chargement:', coursePath);
        
        const response = await fetch(coursePath);
        console.log('Réponse fetch:', response.status, response.statusText);
        
        if (!response.ok) {
          console.error(`Erreur HTTP: ${response.status} - ${response.statusText}`);
          throw new Error(`Cours non trouvé: ${response.status} - ${response.statusText}`);
        }
        
        const jsonData = await response.json();
        console.log('Données JSON chargées:', jsonData);
        
        const htmlContent = convertJsonToHtml(jsonData);
        console.log('Contenu HTML généré:', htmlContent.substring(0, 200) + '...');
        
        setContent(htmlContent);
        
        // Déclencher le rendu MathJax après mise à jour du contenu
        if (window.MathJax) {
          window.MathJax.typesetPromise().catch((err) => console.log('MathJax error:', err));
        }
      } catch (err) {
        console.error('Erreur lors du chargement du cours:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    loadCourse();
  }, [level, chapter, course]);

  // Déclencher MathJax quand le contenu change
  useEffect(() => {
    if (content && window.MathJax) {
      window.MathJax.typesetPromise().catch((err) => console.log('MathJax error:', err));
    }
  }, [content]);

  const getLevelDisplayName = (level) => {
    switch(level) {
      case 'seconde': return 'Seconde';
      case 'premiere': return 'Première';
      case 'terminale': return 'Terminale';
      default: return level;
    }
  };

  const getChapterDisplayName = (chapter) => {
    return chapter.replace(/_/g, ' ').replace(/-/g, ' - ');
  };

  const getCourseDisplayName = (course) => {
    return course.replace(/_/g, ' ').replace(/\//g, ' - ');
  };

  if (loading) {
    return (
      <div className="course-viewer">
        <div className="course-content">
          <div className="loading-container">
            <div className="loading-spinner"></div>
            <p>Chargement du cours...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="course-viewer">
        <div className="course-content">
          <div className="error-container">
            <h2>❌ Erreur</h2>
            <p>Impossible de charger le cours: {error}</p>
            <Link to={`/${level}`} className="back-link">
              ← Retour à {getLevelDisplayName(level)}
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="course-viewer">
      <div className="course-content">
        <div className="course-header">
          <nav className="breadcrumb">
            <Link to="/" className="breadcrumb-link">Accueil</Link>
            <span className="breadcrumb-separator">›</span>
            <Link to={`/${level}`} className="breadcrumb-link">
              {getLevelDisplayName(level)}
            </Link>
            <span className="breadcrumb-separator">›</span>
            <span className="breadcrumb-current">
              {getChapterDisplayName(chapter)}
            </span>
            <span className="breadcrumb-separator">›</span>
            <span className="breadcrumb-current">
              {getCourseDisplayName(course)}
            </span>
          </nav>
          
          <div className="course-title-section">
            <h1 className="course-title">{getCourseDisplayName(course)}</h1>
            <p className="course-subtitle">
              {getLevelDisplayName(level)} - {getChapterDisplayName(chapter)}
            </p>
          </div>
        </div>

        <div className="course-body">
          <style>{`
            .course-image {
              max-width: 100%;
              height: auto;
              margin: 10px 0;
              border-radius: 8px;
              box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .markdown-table {
              width: 100%;
              border-collapse: collapse;
              margin: 15px 0;
              font-size: 14px;
              box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .markdown-table th,
            .markdown-table td {
              border: 1px solid #ddd;
              padding: 12px;
              text-align: left;
            }
            .markdown-table th {
              background-color: #f5f5f5;
              font-weight: bold;
              color: #333;
            }
            .markdown-table tr:nth-child(even) {
              background-color: #f9f9f9;
            }
            .markdown-table tr:hover {
              background-color: #f0f0f0;
            }
          `}</style>
          <div 
            className="course-markdown-content"
            dangerouslySetInnerHTML={{ __html: content }}
          />
        </div>

        <div className="course-footer">
          <Link to={`/${level}`} className="back-to-level">
            ← Retour à {getLevelDisplayName(level)}
          </Link>
        </div>
      </div>
    </div>
  );
};

export default CourseViewer;
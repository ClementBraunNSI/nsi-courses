# Galerie des Monstres

<style>
/* Styles pour la sélection d'année */
.year-selector {
    background: linear-gradient(135deg, #ffb347 0%, #ff8c42 50%, #ff6b35 100%);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(193, 131, 38, 0.3);
}

.year-selector:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(255, 127, 42, 0.4);
}

.year-selector h2 {
    color: white;
    margin: 0;
    font-size: 2rem;
    font-weight: bold;
}

.year-selector p {
    color: rgba(255, 255, 255, 0.9);
    margin: 0.5rem 0 0 0;
    font-size: 1.1rem;
}

/* Styles pour la grille des classes */
.classes-grid {
    display: none;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

.classes-grid.active {
    display: grid;
}

.class-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(193, 131, 38, 0.3);
    transition: all 0.3s ease;
    cursor: pointer;
    border: 2px solid transparent;
}

.class-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 25px rgba(255, 127, 42, 0.4);
    border-color: #ff7f2a;
}

.class-card h3 {
    color: #ff7f2a;
    margin: 0 0 0.5rem 0;
    font-size: 1.5rem;
    font-weight: bold;
}

.class-card p {
    color: var(--md-default-fg-color--light);
    margin: 0;
    font-size: 0.9rem;
}

.class-card .student-count {
    background: rgba(255, 127, 42, 0.1);
    color: #ff7f2a;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
    margin-top: 0.5rem;
    display: inline-block;
}

/* Styles pour la galerie d'images */
.monster-gallery {
    display: none;
    margin: 2rem 0;
}

.monster-gallery.active {
    display: block;
}

.gallery-header {
    text-align: center;
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, rgba(255, 179, 71, 0.1), rgba(255, 107, 53, 0.1));
    border-radius: 15px;
    border: 1px solid rgba(255, 127, 42, 0.2);
}

.gallery-header h3 {
    color: #ff7f2a;
    margin: 0 0 0.5rem 0;
    font-size: 1.8rem;
    font-weight: bold;
}

.gallery-header p {
    color: var(--md-default-fg-color--light);
    margin: 0;
    font-size: 1rem;
}

.monsters-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    padding: 1rem;
}

.monster-card {
    background: var(--md-default-bg-color);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(193, 131, 38, 0.2);
    transition: all 0.3s ease;
    position: relative;
    z-index: 1;
}

.monster-card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 25px rgba(255, 127, 42, 0.3);
    z-index: 100;
}

.monster-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    transition: all 0.3s ease;
    cursor: pointer;
}

.monster-card:hover img {
    filter: brightness(1.1);
}

.monster-name {
    padding: 1rem;
    text-align: center;
    background: rgba(255, 127, 42, 0.05);
    border-top: 1px solid rgba(255, 127, 42, 0.1);
}

.monster-name h4 {
    margin: 0;
    color: #ff7f2a;
    font-size: 1rem;
    font-weight: bold;
    text-transform: capitalize;
}

/* Bouton de retour */
.back-button {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background: linear-gradient(135deg, #ffb347, #ff6b35);
    color: white;
    border: none;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    margin: 1rem 0;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(255, 127, 42, 0.3);
}

.back-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(255, 127, 42, 0.4);
    color: white;
    text-decoration: none;
}

/* Responsive design */
@media (max-width: 768px) {
    .classes-grid {
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        padding: 1rem;
    }
    
    .monsters-grid {
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
    }
    
    .monster-card img {
        height: 150px;
    }
    
    .year-selector h2 {
        font-size: 1.5rem;
    }
    
    .gallery-header h3 {
        font-size: 1.4rem;
    }
}
</style>

<!-- Sélecteur d'année -->
<div class="year-selector" onclick="toggleYear('2024_2025')">
    <h2>🎓 Année 2024-2025</h2>
    <p>Cliquez pour découvrir les créations de nos élèves</p>
</div>

<!-- Grille des classes -->
<div id="classes-2024_2025" class="classes-grid">
    <div class="class-card" onclick="showClass('2024_2025', '2DE1')">
        <h3>2DE1</h3>
        <p>Classe de seconde</p>
        <span class="student-count">18 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE2')">
        <h3>2DE2</h3>
        <p>Classe de seconde</p>
        <span class="student-count">26 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE3')">
        <h3>2DE3</h3>
        <p>Classe de seconde</p>
        <span class="student-count">22 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE5')">
        <h3>2DE5</h3>
        <p>Classe de seconde</p>
        <span class="student-count">20 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE6')">
        <h3>2DE6</h3>
        <p>Classe de seconde</p>
        <span class="student-count">28 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE7')">
        <h3>2DE7</h3>
        <p>Classe de seconde</p>
        <span class="student-count">28 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE9')">
        <h3>2DE9</h3>
        <p>Classe de seconde</p>
        <span class="student-count">21 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE10')">
        <h3>2DE10</h3>
        <p>Classe de seconde</p>
        <span class="student-count">27 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', '2DE11')">
        <h3>2DE11</h3>
        <p>Classe de seconde</p>
        <span class="student-count">26 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', 'S01')">
        <h3>S01</h3>
        <p>Seconde</p>
        <span class="student-count">21 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', 'S16')">
        <h3>S16</h3>
        <p>Seconde</p>
        <span class="student-count">21 élèves</span>
    </div>
    
    <div class="class-card" onclick="showClass('2024_2025', 'S18')">
        <h3>S18</h3>
        <p>Seconde</p>
        <span class="student-count">19 élèves</span>
    </div>
</div>

<!-- Galeries pour chaque classe -->

<!-- Galerie 2DE1 -->
<div id="gallery-2024_2025-2DE1" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE1</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE1</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/Hayrunnisa.webp" alt="Monstre d'Hayrunnisa" loading="lazy">
            <div class="monster-name"><h4>Hayrunnisa</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/acelya.webp" alt="Monstre d'Acelya" loading="lazy">
            <div class="monster-name"><h4>Acelya</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/alexa.webp" alt="Monstre d'Alexa" loading="lazy">
            <div class="monster-name"><h4>Alexa</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/clea.webp" alt="Monstre de Clea" loading="lazy">
            <div class="monster-name"><h4>Clea</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/clemence.webp" alt="Monstre de Clemence" loading="lazy">
            <div class="monster-name"><h4>Clemence</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/emlyne.webp" alt="Monstre d'Emlyne" loading="lazy">
            <div class="monster-name"><h4>Emlyne</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/joan.webp" alt="Monstre de Joan" loading="lazy">
            <div class="monster-name"><h4>Joan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/lina.webp" alt="Monstre de Lina" loading="lazy">
            <div class="monster-name"><h4>Lina</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/louna.webp" alt="Monstre de Louna" loading="lazy">
            <div class="monster-name"><h4>Louna</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/lylian.webp" alt="Monstre de Lylian" loading="lazy">
            <div class="monster-name"><h4>Lylian</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/maelle.webp" alt="Monstre de Maelle" loading="lazy">
            <div class="monster-name"><h4>Maelle</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/maxime.webp" alt="Monstre de Maxime" loading="lazy">
            <div class="monster-name"><h4>Maxime</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/naome.webp" alt="Monstre de Naome" loading="lazy">
            <div class="monster-name"><h4>Naome</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/noor.webp" alt="Monstre de Noor" loading="lazy">
            <div class="monster-name"><h4>Noor</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/quentin.webp" alt="Monstre de Quentin" loading="lazy">
            <div class="monster-name"><h4>Quentin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/salome.webp" alt="Monstre de Salome" loading="lazy">
            <div class="monster-name"><h4>Salome</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/sofia.webp" alt="Monstre de Sofia" loading="lazy">
            <div class="monster-name"><h4>Sofia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE1/thibault.webp" alt="Monstre de Thibault" loading="lazy">
            <div class="monster-name"><h4>Thibault</h4></div>
        </div>
    </div>
</div>

<!-- Galerie 2DE2 -->
<div id="gallery-2024_2025-2DE2" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE2</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE2</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/alyssia.webp" alt="Monstre d'Alyssia" loading="lazy">
            <div class="monster-name"><h4>Alyssia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/antoine.webp" alt="Monstre d'Antoine" loading="lazy">
            <div class="monster-name"><h4>Antoine</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/aya.webp" alt="Monstre d'Aya" loading="lazy">
            <div class="monster-name"><h4>Aya</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/baptiste.webp" alt="Monstre de Baptiste" loading="lazy">
            <div class="monster-name"><h4>Baptiste</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/binti.webp" alt="Monstre de Binti" loading="lazy">
            <div class="monster-name"><h4>Binti</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/camille.webp" alt="Monstre de Camille" loading="lazy">
            <div class="monster-name"><h4>Camille</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/elise.webp" alt="Monstre d'Elise" loading="lazy">
            <div class="monster-name"><h4>Elise</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/ethan.webp" alt="Monstre d'Ethan" loading="lazy">
            <div class="monster-name"><h4>Ethan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/gabriel.webp" alt="Monstre de Gabriel" loading="lazy">
            <div class="monster-name"><h4>Gabriel</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/ilona.webp" alt="Monstre d'Ilona" loading="lazy">
            <div class="monster-name"><h4>Ilona</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/kaila.webp" alt="Monstre de Kaila" loading="lazy">
            <div class="monster-name"><h4>Kaila</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/kylian.webp" alt="Monstre de Kylian" loading="lazy">
            <div class="monster-name"><h4>Kylian</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/kyllian.webp" alt="Monstre de Kyllian" loading="lazy">
            <div class="monster-name"><h4>Kyllian</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/leo.webp" alt="Monstre de Leo" loading="lazy">
            <div class="monster-name"><h4>Leo</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/lise-anne.webp" alt="Monstre de Lise-Anne" loading="lazy">
            <div class="monster-name"><h4>Lise-Anne</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/lison.webp" alt="Monstre de Lison" loading="lazy">
            <div class="monster-name"><h4>Lison</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/loeiz.webp" alt="Monstre de Loeiz" loading="lazy">
            <div class="monster-name"><h4>Loeiz</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/lola.webp" alt="Monstre de Lola" loading="lazy">
            <div class="monster-name"><h4>Lola</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/maelys.webp" alt="Monstre de Maelys" loading="lazy">
            <div class="monster-name"><h4>Maelys</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/maxime.webp" alt="Monstre de Maxime" loading="lazy">
            <div class="monster-name"><h4>Maxime</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/melina.webp" alt="Monstre de Melina" loading="lazy">
            <div class="monster-name"><h4>Melina</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/oscar.webp" alt="Monstre d'Oscar" loading="lazy">
            <div class="monster-name"><h4>Oscar</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/sirine.webp" alt="Monstre de Sirine" loading="lazy">
            <div class="monster-name"><h4>Sirine</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/youn.webp" alt="Monstre de Youn" loading="lazy">
            <div class="monster-name"><h4>Youn</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE2/zoe_emma.webp" alt="Monstre de Zoe Emma" loading="lazy">
            <div class="monster-name"><h4>Zoe Emma</h4></div>
        </div>
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/zyan.webp" alt="Monstre de Zyan" loading="lazy">
             <div class="monster-name"><h4>Zyan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/loeiz.webp" alt="Monstre de Loeiz" loading="lazy">
             <div class="monster-name"><h4>Loeiz</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/kaila.webp" alt="Monstre de Kaila" loading="lazy">
             <div class="monster-name"><h4>Kaila</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/antoine.webp" alt="Monstre d'Antoine" loading="lazy">
             <div class="monster-name"><h4>Antoine</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/alyssia.webp" alt="Monstre d'Alyssia" loading="lazy">
             <div class="monster-name"><h4>Alyssia</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/melina.webp" alt="Monstre de Melina" loading="lazy">
             <div class="monster-name"><h4>Melina</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/maxime.webp" alt="Monstre de Maxime" loading="lazy">
             <div class="monster-name"><h4>Maxime</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/oscar.webp" alt="Monstre d'Oscar" loading="lazy">
             <div class="monster-name"><h4>Oscar</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/kylian.webp" alt="Monstre de Kylian" loading="lazy">
             <div class="monster-name"><h4>Kylian</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/leo.webp" alt="Monstre de Leo" loading="lazy">
             <div class="monster-name"><h4>Leo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/youn.webp" alt="Monstre de Youn" loading="lazy">
             <div class="monster-name"><h4>Youn</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/elise.webp" alt="Monstre d'Elise" loading="lazy">
             <div class="monster-name"><h4>Elise</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/baptiste.webp" alt="Monstre de Baptiste" loading="lazy">
             <div class="monster-name"><h4>Baptiste</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/camille.webp" alt="Monstre de Camille" loading="lazy">
             <div class="monster-name"><h4>Camille</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/kyllian.webp" alt="Monstre de Kyllian" loading="lazy">
             <div class="monster-name"><h4>Kyllian</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/sirine.webp" alt="Monstre de Sirine" loading="lazy">
             <div class="monster-name"><h4>Sirine</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/ethan.webp" alt="Monstre d'Ethan" loading="lazy">
             <div class="monster-name"><h4>Ethan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/maelys.webp" alt="Monstre de Maelys" loading="lazy">
             <div class="monster-name"><h4>Maelys</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/lise-anne.webp" alt="Monstre de Lise-anne" loading="lazy">
             <div class="monster-name"><h4>Lise-anne</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/zoe_emma.webp" alt="Monstre de Zoe_emma" loading="lazy">
             <div class="monster-name"><h4>Zoe Emma</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/lison.webp" alt="Monstre de Lison" loading="lazy">
             <div class="monster-name"><h4>Lison</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/aya.webp" alt="Monstre d'Aya" loading="lazy">
             <div class="monster-name"><h4>Aya</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/gabriel.webp" alt="Monstre de Gabriel" loading="lazy">
             <div class="monster-name"><h4>Gabriel</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE2/binti.webp" alt="Monstre de Binti" loading="lazy">
             <div class="monster-name"><h4>Binti</h4></div>
         </div>
     </div>
</div>

<!-- Galerie 2DE3 -->
<div id="gallery-2024_2025-2DE3" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE3</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE3</p>
    </div>
    <div class="monsters-grid">
        <!-- Les images seront ajoutées ici -->
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/anouk.webp" alt="Monstre d'Anouk" loading="lazy">
            <div class="monster-name"><h4>Anouk</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/chloe.webp" alt="Monstre de Chloe" loading="lazy">
            <div class="monster-name"><h4>Chloe</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/eline_batterie.webp" alt="Monstre d'Eline (Batterie)" loading="lazy">
            <div class="monster-name"><h4>Eline (Batterie)</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/eline_guitare.webp" alt="Monstre d'Eline (Guitare)" loading="lazy">
            <div class="monster-name"><h4>Eline (Guitare)</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/eline_piano.webp" alt="Monstre d'Eline (Piano)" loading="lazy">
            <div class="monster-name"><h4>Eline (Piano)</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/eline_trompette.webp" alt="Monstre d'Eline (Trompette)" loading="lazy">
            <div class="monster-name"><h4>Eline (Trompette)</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/elisa.webp" alt="Monstre d'Elisa" loading="lazy">
            <div class="monster-name"><h4>Elisa</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/enora.webp" alt="Monstre d'Enora" loading="lazy">
            <div class="monster-name"><h4>Enora</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/gabin.webp" alt="Monstre de Gabin" loading="lazy">
            <div class="monster-name"><h4>Gabin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/ilhan.webp" alt="Monstre d'Ilhan" loading="lazy">
            <div class="monster-name"><h4>Ilhan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/joseph.webp" alt="Monstre de Joseph" loading="lazy">
            <div class="monster-name"><h4>Joseph</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/laureline.webp" alt="Monstre de Laureline" loading="lazy">
            <div class="monster-name"><h4>Laureline</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/leo.webp" alt="Monstre de Leo" loading="lazy">
            <div class="monster-name"><h4>Leo</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/madeg.webp" alt="Monstre de Madeg" loading="lazy">
            <div class="monster-name"><h4>Madeg</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/mathys.webp" alt="Monstre de Mathys" loading="lazy">
            <div class="monster-name"><h4>Mathys</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/mila.webp" alt="Monstre de Mila" loading="lazy">
            <div class="monster-name"><h4>Mila</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/niev.webp" alt="Monstre de Niev" loading="lazy">
            <div class="monster-name"><h4>Niev</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/nil.webp" alt="Monstre de Nil" loading="lazy">
            <div class="monster-name"><h4>Nil</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/rose.webp" alt="Monstre de Rose" loading="lazy">
            <div class="monster-name"><h4>Rose</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/sasha.webp" alt="Monstre de Sasha" loading="lazy">
            <div class="monster-name"><h4>Sasha</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/sebastian.webp" alt="Monstre de Sebastian" loading="lazy">
            <div class="monster-name"><h4>Sebastian</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE3/shannon.webp" alt="Monstre de Shannon" loading="lazy">
            <div class="monster-name"><h4>Shannon</h4></div>
        </div>
    </div>
</div>

<!-- Galerie 2DE5 -->
<div id="gallery-2024_2025-2DE5" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE5</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE5</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/agathe_maiwen.webp" alt="Monstre d'Agathe Maiwen" loading="lazy">
             <div class="monster-name"><h4>Agathe Maiwen</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/alan.webp" alt="Monstre d'Alan" loading="lazy">
             <div class="monster-name"><h4>Alan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/allyson_thea.webp" alt="Monstre d'Allyson Thea" loading="lazy">
             <div class="monster-name"><h4>Allyson Thea</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/anais.webp" alt="Monstre d'Anais" loading="lazy">
             <div class="monster-name"><h4>Anais</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/camille_etoile.webp" alt="Monstre de Camille Etoile" loading="lazy">
             <div class="monster-name"><h4>Camille Etoile</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/camille_nuage.webp" alt="Monstre de Camille Nuage" loading="lazy">
             <div class="monster-name"><h4>Camille Nuage</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/camille_pluie.webp" alt="Monstre de Camille Pluie" loading="lazy">
             <div class="monster-name"><h4>Camille Pluie</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/camille_soleil.webp" alt="Monstre de Camille Soleil" loading="lazy">
             <div class="monster-name"><h4>Camille Soleil</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/eliott.webp" alt="Monstre d'Eliott" loading="lazy">
             <div class="monster-name"><h4>Eliott</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/eva.webp" alt="Monstre d'Eva" loading="lazy">
             <div class="monster-name"><h4>Eva</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/guewen.webp" alt="Monstre de Guewen" loading="lazy">
             <div class="monster-name"><h4>Guewen</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/ilan.webp" alt="Monstre d'Ilan" loading="lazy">
             <div class="monster-name"><h4>Ilan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/jules.webp" alt="Monstre de Jules" loading="lazy">
             <div class="monster-name"><h4>Jules</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/maxence.webp" alt="Monstre de Maxence" loading="lazy">
             <div class="monster-name"><h4>Maxence</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/milan.webp" alt="Monstre de Milan" loading="lazy">
             <div class="monster-name"><h4>Milan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/patricia_zelie.webp" alt="Monstre de Patricia Zelie" loading="lazy">
             <div class="monster-name"><h4>Patricia Zelie</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/romane.webp" alt="Monstre de Romane" loading="lazy">
             <div class="monster-name"><h4>Romane</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/timeo.webp" alt="Monstre de Timeo" loading="lazy">
             <div class="monster-name"><h4>Timeo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/timeo_g.webp" alt="Monstre de Timeo G" loading="lazy">
             <div class="monster-name"><h4>Timeo G</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE5/tino.webp" alt="Monstre de Tino" loading="lazy">
             <div class="monster-name"><h4>Tino</h4></div>
         </div>
    </div>
</div>

<!-- Galerie 2DE6 -->
<div id="gallery-2024_2025-2DE6" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE6</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE6</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/aela.webp" alt="Monstre d'Aela" loading="lazy">
             <div class="monster-name"><h4>Aela</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/alwena.webp" alt="Monstre d'Alwena" loading="lazy">
             <div class="monster-name"><h4>Alwena</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/elianor.webp" alt="Monstre d'Elianor" loading="lazy">
             <div class="monster-name"><h4>Elianor</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/elsa.webp" alt="Monstre d'Elsa" loading="lazy">
             <div class="monster-name"><h4>Elsa</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/emma.webp" alt="Monstre d'Emma" loading="lazy">
             <div class="monster-name"><h4>Emma</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/ethel.webp" alt="Monstre d'Ethel" loading="lazy">
             <div class="monster-name"><h4>Ethel</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/ferdinand.webp" alt="Monstre de Ferdinand" loading="lazy">
             <div class="monster-name"><h4>Ferdinand</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/haizia.webp" alt="Monstre d'Haizia" loading="lazy">
             <div class="monster-name"><h4>Haizia</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/jade.webp" alt="Monstre de Jade" loading="lazy">
             <div class="monster-name"><h4>Jade</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/jeanne.webp" alt="Monstre de Jeanne" loading="lazy">
             <div class="monster-name"><h4>Jeanne</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/joris.webp" alt="Monstre de Joris" loading="lazy">
             <div class="monster-name"><h4>Joris</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/juliette.webp" alt="Monstre de Juliette" loading="lazy">
             <div class="monster-name"><h4>Juliette</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/leandre.webp" alt="Monstre de Leandre" loading="lazy">
             <div class="monster-name"><h4>Leandre</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/lena.webp" alt="Monstre de Lena" loading="lazy">
             <div class="monster-name"><h4>Lena</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/lise.webp" alt="Monstre de Lise" loading="lazy">
             <div class="monster-name"><h4>Lise</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/ludmila.webp" alt="Monstre de Ludmila" loading="lazy">
             <div class="monster-name"><h4>Ludmila</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/mael.webp" alt="Monstre de Mael" loading="lazy">
             <div class="monster-name"><h4>Mael</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/mayane.webp" alt="Monstre de Mayane" loading="lazy">
             <div class="monster-name"><h4>Mayane</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/merlin.webp" alt="Monstre de Merlin" loading="lazy">
             <div class="monster-name"><h4>Merlin</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/nathan.webp" alt="Monstre de Nathan" loading="lazy">
             <div class="monster-name"><h4>Nathan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/nina.webp" alt="Monstre de Nina" loading="lazy">
             <div class="monster-name"><h4>Nina</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/noah.webp" alt="Monstre de Noah" loading="lazy">
             <div class="monster-name"><h4>Noah</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/nolan.webp" alt="Monstre de Nolan" loading="lazy">
             <div class="monster-name"><h4>Nolan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/rival_leandre.webp" alt="Monstre de Rival Leandre" loading="lazy">
             <div class="monster-name"><h4>Rival Leandre</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/rozenn.webp" alt="Monstre de Rozenn" loading="lazy">
             <div class="monster-name"><h4>Rozenn</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/salomee.webp" alt="Monstre de Salomee" loading="lazy">
             <div class="monster-name"><h4>Salomee</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/sarah.webp" alt="Monstre de Sarah" loading="lazy">
             <div class="monster-name"><h4>Sarah</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE6/timoté.webp" alt="Monstre de Timoté" loading="lazy">
             <div class="monster-name"><h4>Timoté</h4></div>
         </div>
    </div>
</div>

<!-- Galerie 2DE7 -->
<div id="gallery-2024_2025-2DE7" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE7</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE7</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/alan.webp" alt="Monstre d'Alan" loading="lazy">
             <div class="monster-name"><h4>Alan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/alice.webp" alt="Monstre d'Alice" loading="lazy">
             <div class="monster-name"><h4>Alice</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/alou.webp" alt="Monstre d'Alou" loading="lazy">
             <div class="monster-name"><h4>Alou</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/charline.webp" alt="Monstre de Charline" loading="lazy">
             <div class="monster-name"><h4>Charline</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/dalila.webp" alt="Monstre de Dalila" loading="lazy">
             <div class="monster-name"><h4>Dalila</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/eloa.webp" alt="Monstre d'Eloa" loading="lazy">
             <div class="monster-name"><h4>Eloa</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/emma.webp" alt="Monstre d'Emma" loading="lazy">
             <div class="monster-name"><h4>Emma</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/ethan.webp" alt="Monstre d'Ethan" loading="lazy">
             <div class="monster-name"><h4>Ethan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/hugo.webp" alt="Monstre d'Hugo" loading="lazy">
             <div class="monster-name"><h4>Hugo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/ilan.webp" alt="Monstre d'Ilan" loading="lazy">
             <div class="monster-name"><h4>Ilan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/jade.webp" alt="Monstre de Jade" loading="lazy">
             <div class="monster-name"><h4>Jade</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/jules.webp" alt="Monstre de Jules" loading="lazy">
             <div class="monster-name"><h4>Jules</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/karim.webp" alt="Monstre de Karim" loading="lazy">
             <div class="monster-name"><h4>Karim</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/lilie-rose.webp" alt="Monstre de Lilie-rose" loading="lazy">
             <div class="monster-name"><h4>Lilie-rose</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/lilou.webp" alt="Monstre de Lilou" loading="lazy">
             <div class="monster-name"><h4>Lilou</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/mael.webp" alt="Monstre de Mael" loading="lazy">
             <div class="monster-name"><h4>Mael</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/maelys.webp" alt="Monstre de Maelys" loading="lazy">
             <div class="monster-name"><h4>Maelys</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/mathilde.webp" alt="Monstre de Mathilde" loading="lazy">
             <div class="monster-name"><h4>Mathilde</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/maxime.webp" alt="Monstre de Maxime" loading="lazy">
             <div class="monster-name"><h4>Maxime</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/milo.webp" alt="Monstre de Milo" loading="lazy">
             <div class="monster-name"><h4>Milo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/moncef.webp" alt="Monstre de Moncef" loading="lazy">
             <div class="monster-name"><h4>Moncef</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/nolan.webp" alt="Monstre de Nolan" loading="lazy">
             <div class="monster-name"><h4>Nolan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/orlane.webp" alt="Monstre d'Orlane" loading="lazy">
             <div class="monster-name"><h4>Orlane</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/soan.webp" alt="Monstre de Soan" loading="lazy">
             <div class="monster-name"><h4>Soan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/talel.webp" alt="Monstre de Talel" loading="lazy">
             <div class="monster-name"><h4>Talel</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/timeo.webp" alt="Monstre de Timeo" loading="lazy">
             <div class="monster-name"><h4>Timeo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/youen.webp" alt="Monstre de Youen" loading="lazy">
             <div class="monster-name"><h4>Youen</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE7/younes.webp" alt="Monstre de Younes" loading="lazy">
             <div class="monster-name"><h4>Younes</h4></div>
         </div>
    </div>
</div>

<!-- Galerie 2DE9 -->
<div id="gallery-2024_2025-2DE9" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE9</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE9</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/aidie.webp" alt="Monstre d'Aidie" loading="lazy">
             <div class="monster-name"><h4>Aidie</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/alice.webp" alt="Monstre d'Alice" loading="lazy">
             <div class="monster-name"><h4>Alice</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/charlotte.webp" alt="Monstre de Charlotte" loading="lazy">
             <div class="monster-name"><h4>Charlotte</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/eliott.webp" alt="Monstre d'Eliott" loading="lazy">
             <div class="monster-name"><h4>Eliott</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/elise.webp" alt="Monstre d'Elise" loading="lazy">
             <div class="monster-name"><h4>Elise</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/elsa.webp" alt="Monstre d'Elsa" loading="lazy">
             <div class="monster-name"><h4>Elsa</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/iwen.webp" alt="Monstre d'Iwen" loading="lazy">
             <div class="monster-name"><h4>Iwen</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/janelle.webp" alt="Monstre de Janelle" loading="lazy">
             <div class="monster-name"><h4>Janelle</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/jeanne.webp" alt="Monstre de Jeanne" loading="lazy">
             <div class="monster-name"><h4>Jeanne</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/lena.webp" alt="Monstre de Lena" loading="lazy">
             <div class="monster-name"><h4>Lena</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/lina.webp" alt="Monstre de Lina" loading="lazy">
             <div class="monster-name"><h4>Lina</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/maelys.webp" alt="Monstre de Maelys" loading="lazy">
             <div class="monster-name"><h4>Maelys</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/marisa.webp" alt="Monstre de Marisa" loading="lazy">
             <div class="monster-name"><h4>Marisa</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/marko.webp" alt="Monstre de Marko" loading="lazy">
             <div class="monster-name"><h4>Marko</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/mathys.webp" alt="Monstre de Mathys" loading="lazy">
             <div class="monster-name"><h4>Mathys</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/maxence.webp" alt="Monstre de Maxence" loading="lazy">
             <div class="monster-name"><h4>Maxence</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/mylan_ilyess.webp" alt="Monstre de Mylan Ilyess" loading="lazy">
             <div class="monster-name"><h4>Mylan Ilyess</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/nathael.webp" alt="Monstre de Nathael" loading="lazy">
             <div class="monster-name"><h4>Nathael</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/sylvia.webp" alt="Monstre de Sylvia" loading="lazy">
             <div class="monster-name"><h4>Sylvia</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/theo.webp" alt="Monstre de Theo" loading="lazy">
             <div class="monster-name"><h4>Theo</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE9/yael.webp" alt="Monstre de Yael" loading="lazy">
             <div class="monster-name"><h4>Yael</h4></div>
         </div>
    </div>
</div>

<!-- Galerie 2DE10 -->
<div id="gallery-2024_2025-2DE10" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE10</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE10</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/abigael.webp" alt="Monstre d'Abigael" loading="lazy">
             <div class="monster-name"><h4>Abigael</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/alexis.webp" alt="Monstre d'Alexis" loading="lazy">
             <div class="monster-name"><h4>Alexis</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/anna-rose.webp" alt="Monstre d'Anna-rose" loading="lazy">
             <div class="monster-name"><h4>Anna-rose</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/esther.webp" alt="Monstre d'Esther" loading="lazy">
             <div class="monster-name"><h4>Esther</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/eyaelle.webp" alt="Monstre d'Eyaelle" loading="lazy">
             <div class="monster-name"><h4>Eyaelle</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/ilyan.webp" alt="Monstre d'Ilyan" loading="lazy">
             <div class="monster-name"><h4>Ilyan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/jade.webp" alt="Monstre de Jade" loading="lazy">
             <div class="monster-name"><h4>Jade</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/johan.webp" alt="Monstre de Johan" loading="lazy">
             <div class="monster-name"><h4>Johan</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/louise.webp" alt="Monstre de Louise" loading="lazy">
             <div class="monster-name"><h4>Louise</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/lucas.webp" alt="Monstre de Lucas" loading="lazy">
             <div class="monster-name"><h4>Lucas</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mailys.webp" alt="Monstre de Mailys" loading="lazy">
             <div class="monster-name"><h4>Mailys</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/margaux.webp" alt="Monstre de Margaux" loading="lazy">
             <div class="monster-name"><h4>Margaux</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_1.webp" alt="Monstre de Mathys 1" loading="lazy">
             <div class="monster-name"><h4>Mathys 1</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_2.webp" alt="Monstre de Mathys 2" loading="lazy">
             <div class="monster-name"><h4>Mathys 2</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_3.webp" alt="Monstre de Mathys 3" loading="lazy">
             <div class="monster-name"><h4>Mathys 3</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_4.webp" alt="Monstre de Mathys 4" loading="lazy">
             <div class="monster-name"><h4>Mathys 4</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_5.webp" alt="Monstre de Mathys 5" loading="lazy">
             <div class="monster-name"><h4>Mathys 5</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/mathys_s.webp" alt="Monstre de Mathys S" loading="lazy">
             <div class="monster-name"><h4>Mathys S</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/melina.webp" alt="Monstre de Melina" loading="lazy">
             <div class="monster-name"><h4>Melina</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/naomée.webp" alt="Monstre de Naomée" loading="lazy">
             <div class="monster-name"><h4>Naomée</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/nassim.webp" alt="Monstre de Nassim" loading="lazy">
             <div class="monster-name"><h4>Nassim</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/nina.webp" alt="Monstre de Nina" loading="lazy">
             <div class="monster-name"><h4>Nina</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/pierre.webp" alt="Monstre de Pierre" loading="lazy">
             <div class="monster-name"><h4>Pierre</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/roxanne.webp" alt="Monstre de Roxanne" loading="lazy">
             <div class="monster-name"><h4>Roxanne</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/samira.webp" alt="Monstre de Samira" loading="lazy">
             <div class="monster-name"><h4>Samira</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/semih.webp" alt="Monstre de Semih" loading="lazy">
             <div class="monster-name"><h4>Semih</h4></div>
         </div>
         <div class="monster-card">
             <img src="../monstres/2024_2025/2DE10/telio.webp" alt="Monstre de Telio" loading="lazy">
             <div class="monster-name"><h4>Telio</h4></div>
         </div>
    </div>
</div>

<!-- Galerie 2DE11 -->
<div id="gallery-2024_2025-2DE11" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe 2DE11</h3>
        <p>Découvrez les créations fantastiques des élèves de 2DE11</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/aaron.webp" alt="Monstre d'Aaron" loading="lazy">
            <div class="monster-name"><h4>Aaron</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/alice.webp" alt="Monstre d'Alice" loading="lazy">
            <div class="monster-name"><h4>Alice</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/anais.webp" alt="Monstre d'Anais" loading="lazy">
            <div class="monster-name"><h4>Anais</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/anouk.webp" alt="Monstre d'Anouk" loading="lazy">
            <div class="monster-name"><h4>Anouk</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/hanae.webp" alt="Monstre d'Hanae" loading="lazy">
            <div class="monster-name"><h4>Hanae</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/ilann.webp" alt="Monstre d'Ilann" loading="lazy">
            <div class="monster-name"><h4>Ilann</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/jeanne.webp" alt="Monstre de Jeanne" loading="lazy">
            <div class="monster-name"><h4>Jeanne</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/jorys.webp" alt="Monstre de Jorys" loading="lazy">
            <div class="monster-name"><h4>Jorys</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/jules.webp" alt="Monstre de Jules" loading="lazy">
            <div class="monster-name"><h4>Jules</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/jules_r.webp" alt="Monstre de Jules R" loading="lazy">
            <div class="monster-name"><h4>Jules R</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/lucas.webp" alt="Monstre de Lucas" loading="lazy">
            <div class="monster-name"><h4>Lucas</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/lysa.webp" alt="Monstre de Lysa" loading="lazy">
            <div class="monster-name"><h4>Lysa</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/madyar.webp" alt="Monstre de Madyar" loading="lazy">
            <div class="monster-name"><h4>Madyar</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/mailye.webp" alt="Monstre de Mailye" loading="lazy">
            <div class="monster-name"><h4>Mailye</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/maria.webp" alt="Monstre de Maria" loading="lazy">
            <div class="monster-name"><h4>Maria</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/maylane.webp" alt="Monstre de Maylane" loading="lazy">
            <div class="monster-name"><h4>Maylane</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/melia.webp" alt="Monstre de Melia" loading="lazy">
            <div class="monster-name"><h4>Melia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/nhayla.webp" alt="Monstre de Nhayla" loading="lazy">
            <div class="monster-name"><h4>Nhayla</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/quentin.webp" alt="Monstre de Quentin" loading="lazy">
            <div class="monster-name"><h4>Quentin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/servane.webp" alt="Monstre de Servane" loading="lazy">
            <div class="monster-name"><h4>Servane</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/sham.webp" alt="Monstre de Sham" loading="lazy">
            <div class="monster-name"><h4>Sham</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/shanice.webp" alt="Monstre de Shanice" loading="lazy">
            <div class="monster-name"><h4>Shanice</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/tess.webp" alt="Monstre de Tess" loading="lazy">
            <div class="monster-name"><h4>Tess</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/titouan.webp" alt="Monstre de Titouan" loading="lazy">
            <div class="monster-name"><h4>Titouan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/yoann.webp" alt="Monstre de Yoann" loading="lazy">
            <div class="monster-name"><h4>Yoann</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/2DE11/zoe.webp" alt="Monstre de Zoe" loading="lazy">
            <div class="monster-name"><h4>Zoe</h4></div>
        </div>
    </div>
</div>

<!-- Galerie S01 -->
<div id="gallery-2024_2025-S01" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe S01</h3>
        <p>Découvrez les créations fantastiques des élèves de S01</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/awena.webp" alt="Monstre d'Awena" loading="lazy">
            <div class="monster-name"><h4>Awena</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/charlotte.webp" alt="Monstre de Charlotte" loading="lazy">
            <div class="monster-name"><h4>Charlotte</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/clea.webp" alt="Monstre de Clea" loading="lazy">
            <div class="monster-name"><h4>Clea</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/honore.webp" alt="Monstre d'Honore" loading="lazy">
            <div class="monster-name"><h4>Honore</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/jade.webp" alt="Monstre de Jade" loading="lazy">
            <div class="monster-name"><h4>Jade</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/jade_2.webp" alt="Monstre de Jade 2" loading="lazy">
            <div class="monster-name"><h4>Jade 2</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/junon.webp" alt="Monstre de Junon" loading="lazy">
            <div class="monster-name"><h4>Junon</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/louise.webp" alt="Monstre de Louise" loading="lazy">
            <div class="monster-name"><h4>Louise</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/louise_2.webp" alt="Monstre de Louise 2" loading="lazy">
            <div class="monster-name"><h4>Louise 2</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/louna_2.webp" alt="Monstre de Louna 2" loading="lazy">
            <div class="monster-name"><h4>Louna 2</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/maiann.webp" alt="Monstre de Maiann" loading="lazy">
            <div class="monster-name"><h4>Maiann</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/melanie.webp" alt="Monstre de Melanie" loading="lazy">
            <div class="monster-name"><h4>Melanie</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/melwynn.webp" alt="Monstre de Melwynn" loading="lazy">
            <div class="monster-name"><h4>Melwynn</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/molene.webp" alt="Monstre de Molene" loading="lazy">
            <div class="monster-name"><h4>Molene</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/nora-lea.webp" alt="Monstre de Nora-lea" loading="lazy">
            <div class="monster-name"><h4>Nora-lea</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/olivia.webp" alt="Monstre d'Olivia" loading="lazy">
            <div class="monster-name"><h4>Olivia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/rose.webp" alt="Monstre de Rose" loading="lazy">
            <div class="monster-name"><h4>Rose</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/thomas.webp" alt="Monstre de Thomas" loading="lazy">
            <div class="monster-name"><h4>Thomas</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/tiago.webp" alt="Monstre de Tiago" loading="lazy">
            <div class="monster-name"><h4>Tiago</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/yves.webp" alt="Monstre d'Yves" loading="lazy">
            <div class="monster-name"><h4>Yves</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S01/zoe.webp" alt="Monstre de Zoe" loading="lazy">
            <div class="monster-name"><h4>Zoe</h4></div>
        </div>
    </div>
</div>

<!-- Galerie S16 -->
<div id="gallery-2024_2025-S16" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe S16</h3>
        <p>Découvrez les créations fantastiques des élèves de S16</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/alex.webp" alt="Monstre d'Alex" loading="lazy">
            <div class="monster-name"><h4>Alex</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/eliz.webp" alt="Monstre d'Eliz" loading="lazy">
            <div class="monster-name"><h4>Eliz</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/emmy.webp" alt="Monstre d'Emmy" loading="lazy">
            <div class="monster-name"><h4>Emmy</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/gabin.webp" alt="Monstre de Gabin" loading="lazy">
            <div class="monster-name"><h4>Gabin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/gaspard.webp" alt="Monstre de Gaspard" loading="lazy">
            <div class="monster-name"><h4>Gaspard</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/julia.webp" alt="Monstre de Julia" loading="lazy">
            <div class="monster-name"><h4>Julia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/liam.webp" alt="Monstre de Liam" loading="lazy">
            <div class="monster-name"><h4>Liam</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/louise_r.webp" alt="Monstre de Louise R" loading="lazy">
            <div class="monster-name"><h4>Louise R</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/lylia.webp" alt="Monstre de Lylia" loading="lazy">
            <div class="monster-name"><h4>Lylia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/maely.webp" alt="Monstre de Maely" loading="lazy">
            <div class="monster-name"><h4>Maely</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/maelys.webp" alt="Monstre de Maelys" loading="lazy">
            <div class="monster-name"><h4>Maelys</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/marie_ellynn.webp" alt="Monstre de Marie Ellynn" loading="lazy">
            <div class="monster-name"><h4>Marie Ellynn</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/marina.webp" alt="Monstre de Marina" loading="lazy">
            <div class="monster-name"><h4>Marina</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/maxime.webp" alt="Monstre de Maxime" loading="lazy">
            <div class="monster-name"><h4>Maxime</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/mila.webp" alt="Monstre de Mila" loading="lazy">
            <div class="monster-name"><h4>Mila</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/noa.webp" alt="Monstre de Noa" loading="lazy">
            <div class="monster-name"><h4>Noa</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/nolan.webp" alt="Monstre de Nolan" loading="lazy">
            <div class="monster-name"><h4>Nolan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/oceane.webp" alt="Monstre d'Oceane" loading="lazy">
            <div class="monster-name"><h4>Oceane</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/paul.webp" alt="Monstre de Paul" loading="lazy">
            <div class="monster-name"><h4>Paul</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/pierre.webp" alt="Monstre de Pierre" loading="lazy">
            <div class="monster-name"><h4>Pierre</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/romain.webp" alt="Monstre de Romain" loading="lazy">
            <div class="monster-name"><h4>Romain</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/sasha.webp" alt="Monstre de Sasha" loading="lazy">
            <div class="monster-name"><h4>Sasha</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/simon.webp" alt="Monstre de Simon" loading="lazy">
            <div class="monster-name"><h4>Simon</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/tess.webp" alt="Monstre de Tess" loading="lazy">
            <div class="monster-name"><h4>Tess</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/titouan.webp" alt="Monstre de Titouan" loading="lazy">
            <div class="monster-name"><h4>Titouan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/tom.webp" alt="Monstre de Tom" loading="lazy">
            <div class="monster-name"><h4>Tom</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/yann.webp" alt="Monstre de Yann" loading="lazy">
            <div class="monster-name"><h4>Yann</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S16/yoann.webp" alt="Monstre de Yoann" loading="lazy">
            <div class="monster-name"><h4>Yoann</h4></div>
        </div>
    </div>
</div>

<!-- Galerie S18 -->
<div id="gallery-2024_2025-S18" class="monster-gallery">
    <button class="back-button" onclick="hideGallery()">← Retour aux classes</button>
    <div class="gallery-header">
        <h3>Monstres de la classe S18</h3>
        <p>Découvrez les créations fantastiques des élèves de S18</p>
    </div>
    <div class="monsters-grid">
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/anae.webp" alt="Monstre d'Anae" loading="lazy">
            <div class="monster-name"><h4>Anae</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/baptiste.webp" alt="Monstre de Baptiste" loading="lazy">
            <div class="monster-name"><h4>Baptiste</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/calie.webp" alt="Monstre de Calie" loading="lazy">
            <div class="monster-name"><h4>Calie</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/emma.webp" alt="Monstre d'Emma" loading="lazy">
            <div class="monster-name"><h4>Emma</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/ethan.webp" alt="Monstre d'Ethan" loading="lazy">
            <div class="monster-name"><h4>Ethan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/gabin.webp" alt="Monstre de Gabin" loading="lazy">
            <div class="monster-name"><h4>Gabin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/joan.webp" alt="Monstre de Joan" loading="lazy">
            <div class="monster-name"><h4>Joan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/lilou.webp" alt="Monstre de Lilou" loading="lazy">
            <div class="monster-name"><h4>Lilou</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/lilwenn.webp" alt="Monstre de Lilwenn" loading="lazy">
            <div class="monster-name"><h4>Lilwenn</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/lola.webp" alt="Monstre de Lola" loading="lazy">
            <div class="monster-name"><h4>Lola</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/manon.webp" alt="Monstre de Manon" loading="lazy">
            <div class="monster-name"><h4>Manon</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/mathurin.webp" alt="Monstre de Mathurin" loading="lazy">
            <div class="monster-name"><h4>Mathurin</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/maxence.webp" alt="Monstre de Maxence" loading="lazy">
            <div class="monster-name"><h4>Maxence</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/nathan.webp" alt="Monstre de Nathan" loading="lazy">
            <div class="monster-name"><h4>Nathan</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/renzo.webp" alt="Monstre de Renzo" loading="lazy">
            <div class="monster-name"><h4>Renzo</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/romane.webp" alt="Monstre de Romane" loading="lazy">
            <div class="monster-name"><h4>Romane</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/sofia.webp" alt="Monstre de Sofia" loading="lazy">
            <div class="monster-name"><h4>Sofia</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/tahyna.webp" alt="Monstre de Tahyna" loading="lazy">
            <div class="monster-name"><h4>Tahyna</h4></div>
        </div>
        <div class="monster-card">
            <img src="../monstres/2024_2025/S18/thais.webp" alt="Monstre de Thais" loading="lazy">
            <div class="monster-name"><h4>Thais</h4></div>
        </div>
    </div>
</div>

<script>
function toggleYear(year) {
    const classesGrid = document.getElementById(`classes-${year}`);
    const isVisible = classesGrid.classList.contains('active');
    
    // Masquer toutes les galeries
    hideAllGalleries();
    
    // Basculer l'affichage de la grille des classes
    if (isVisible) {
        classesGrid.classList.remove('active');
    } else {
        classesGrid.classList.add('active');
    }
}

function showClass(year, className) {
    // Masquer toutes les galeries
    hideAllGalleries();
    
    // Afficher la galerie de la classe sélectionnée
    const gallery = document.getElementById(`gallery-${year}-${className}`);
    if (gallery) {
        gallery.classList.add('active');
        gallery.scrollIntoView({ behavior: 'smooth' });
    }
}

function hideGallery() {
    // Masquer toutes les galeries
    hideAllGalleries();
    
    // Faire défiler vers la grille des classes
    const classesGrid = document.querySelector('.classes-grid.active');
    if (classesGrid) {
        classesGrid.scrollIntoView({ behavior: 'smooth' });
    }
}

function hideAllGalleries() {
    const galleries = document.querySelectorAll('.monster-gallery');
    galleries.forEach(gallery => {
        gallery.classList.remove('active');
    });
}

// Gestion du redimensionnement de la fenêtre
window.addEventListener('resize', function() {
    // Réajuster la mise en page si nécessaire
});

// Lazy loading des images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
});
</script>

<style>
.level-header { background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(193, 131, 38, 0.93); text-align: center; margin: 2rem 0; }
.level-header h1 { margin: 0; font-size: 2rem; font-weight: 700; background: linear-gradient(135deg, #ffb347, #ff6b35); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.level-header p { margin: 0.5rem 0; color: #333; }
.categories-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.category-card { background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: 0 8px 32px rgba(0,0,0,0.1); transition: transform 0.3s ease; }
.category-card:hover { transform: translateY(-8px); }
.chapter-links { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.chapter-link { background: rgba(255,255,255,0.9); color: #34495e; padding: 0.4rem 0.8rem; border-radius: 8px; text-decoration: none; border: 1px solid rgba(255,255,255,0.6); }
.chapter-link:hover { transform: scale(1.03); }
.btn { display: inline-block; padding: 0.5rem 1rem; background: white !important; color: orange !important; border: 2px solid orange; border-radius: 5px; text-decoration: none; }
</style>

<div class="level-header">
  <img src="../../../images/fox_terminale.png" alt="Roméo" style="width:90px;height:90px;object-fit:contain;" />
  <h1>Espace R</h1>
  <p>Révisions personnalisées</p>
</div>

<div class="categories-grid">
  <div class="category-card">
    <h3>Bases de Données & SQL</h3>
    <p>Modèle relationnel, requêtes, filtrage et jointures</p>
    <div class="chapter-links">
      <a href="../SQL/Cours/Cours_SQL" class="chapter-link">📚 Cours SQL Complet</a>
      <a href="../SQL/Exercices/exercices_sql" class="chapter-link">📚 Exercices Progressifs</a>
    </div>
  </div>
</div>

<script>
(function(){
  try {
    var ok = sessionStorage.getItem('cp_token');
    if (ok !== 'ok') { location.href = '/'; }
  } catch(e) { location.href = '/'; }
})();
</script>

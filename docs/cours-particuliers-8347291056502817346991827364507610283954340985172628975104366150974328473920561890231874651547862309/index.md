# Cours particuliers

<script>
(function(){
  try {
    var ok = sessionStorage.getItem('cp_token');
    if (ok !== 'ok') { location.href = '/'; }
  } catch(e) { location.href = '/'; }
})();
</script>

<style>
.level-cards-container { display: flex; flex-wrap: nowrap; gap: 1rem; justify-content: center; align-items: stretch; overflow-x: auto; padding: 1rem 0; }
.level-card { background: var(--md-default-bg-color); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(193, 131, 38, 0.93); text-align: center; transition: transform 0.3s ease; display: flex; flex-direction: column; min-height: 450px; flex: 0 0 300px; }
.level-card:hover { transform: translateY(-10px); }
.level-card img { width: 100%; height: 160px; object-fit: contain; margin-bottom: 1rem; }
.btn { display: inline-block; padding: 0.5rem 1rem; background: white !important; color: orange !important; border: 2px solid orange; border-radius: 5px; text-decoration: none; margin-top: auto; }
</style>

<div class="level-cards-container">
  <div class="level-card">
    <img src="../../images/fox_premiere.png" alt="Cléo">
    <h2>C</h2>
    <p>Suivi particulier — révision des bases du langage C</p>
    <a href="Cleo/index_cleo/" class="btn">Accéder à l’espace</a>
  </div>

  <div class="level-card">
    <img src="../../images/fox_terminale.png" alt="Roméo">
    <h2>SQL</h2>
    <p>Suivi particulier — Programme de terminale NSI</p>
    <a href="Romeo/index_romeo/" class="btn">Accéder à l’espace</a>
  </div>
</div>

<!-- Accès contrôlé par sessionStorage défini depuis la page d'accueil -->

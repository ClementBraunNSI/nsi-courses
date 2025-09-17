<style>
/* Styles modernes pour le cours Conformité et Veille BTS SIO */
.course-header {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 3rem;
    margin: 2rem 0;
    border: 1px solid rgba(155, 89, 182, 0.2);
    text-align: center;
}

.course-title {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}

.course-subtitle {
    color: #7f8c8d;
    font-size: 1.2rem;
    font-weight: 300;
    margin-bottom: 2rem;
}

.concept-section {
    background: var(--md-default-bg-color);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.section-title {
    font-size: 2.2rem;
    font-weight: 600;
    color: #9b59b6;
    margin-bottom: 2rem;
    text-align: center;
}

.definition-box {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-left: 5px solid #9b59b6;
    border-radius: 12px;
    padding: 2rem;
    margin: 2rem 0;
    backdrop-filter: blur(10px);
}

.definition-title {
    font-size: 1.3rem;
    font-weight: 600;
    color: #9b59b6;
    margin-bottom: 1rem;
}

.definition-content {
    color: var(--md-default-fg-color);
    font-size: 1.1rem;
    line-height: 1.6;
}

.rgpd-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
}

.rgpd-card {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.4);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(5px);
}

.rgpd-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 24px rgba(155, 89, 182, 0.2);
}

.rgpd-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-align: center;
}

.rgpd-title {
    font-size: 1.2rem;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.rgpd-description {
    color: #7f8c8d;
    font-size: 0.9rem;
    line-height: 1.5;
}

.highlight-fact {
    background: rgba(155, 89, 182, 0.1);
    border-left: 4px solid #9b59b6;
    padding: 1rem;
    margin: 1rem 0;
    border-radius: 8px;
    font-weight: 500;
}

.norms-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.norm-card {
    background: linear-gradient(135deg, rgba(155, 89, 182, 0.1), rgba(142, 68, 173, 0.05));
    border-radius: 15px;
    padding: 1.5rem;
    border: 1px solid rgba(155, 89, 182, 0.2);
    transition: all 0.3s ease;
}

.norm-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(155, 89, 182, 0.2);
}

.code-example {
    background: #1a202c;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    border-left: 4px solid #9b59b6;
}

.code-title {
    color: #9b59b6;
    font-weight: 700;
    margin-bottom: 1rem;
    font-size: 1rem;
}

.demo-box {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.demo-title {
    color: #3498db;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.compliance-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1rem 0;
    background: rgba(255, 255, 255, 0.8);
    border-radius: 8px;
    overflow: hidden;
}

.compliance-table th, .compliance-table td {
    padding: 0.8rem;
    text-align: left;
    border: 1px solid rgba(155, 89, 182, 0.2);
}

.compliance-table th {
    background: rgba(155, 89, 182, 0.2);
    font-weight: 600;
    color: #2c3e50;
}

.identity-step {
    background: rgba(46, 204, 113, 0.1);
    border-left: 4px solid #2ecc71;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.identity-title {
    color: #2ecc71;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.veille-source {
    background: rgba(52, 152, 219, 0.1);
    border-left: 4px solid #3498db;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 6px;
}

.veille-source-title {
    color: #3498db;
    font-weight: 600;
    margin-bottom: 0.3rem;
    font-size: 0.9rem;
}

.sanction-box {
    background: rgba(231, 76, 60, 0.1);
    border-left: 4px solid #e74c3c;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}

.sanction-title {
    color: #e74c3c;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.checklist-item {
    background: rgba(46, 204, 113, 0.1);
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem 0;
    border-left: 4px solid #2ecc71;
}

.checklist-title {
    color: #2ecc71;
    font-weight: 600;
    margin-bottom: 0.3rem;
}

/* Styles pour les titres h3 */
h3 {
    font-size: 1.8rem;
    font-weight: 600;
    color: #9b59b6;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(155, 89, 182, 0.3);
    background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
</style>

<div class="course-header">
    <h1 class="course-title">B3.6 - Conformité et Veille Sécurité</h1>
    <p class="course-subtitle">RGPD, Normes et Identité Numérique - BTS SIO</p>
</div>

## 🎯 Objectifs du cours

À l'issue de ce cours, vous serez capable de :
- Appliquer les exigences du RGPD dans un contexte informatique
- Comprendre les principales normes de sécurité (ISO 27001, ANSSI)
- Mettre en place une stratégie de veille sécurité
- Préserver et gérer l'identité numérique d'une organisation

---

<div class="concept-section">
<h2 class="section-title">🛡️ RGPD - Règlement Général sur la Protection des Données</h2>

<div class="definition-box">
<div class="definition-title">RGPD (GDPR)</div>
<div class="definition-content">
Règlement européen entré en vigueur le 25 mai 2018, qui encadre le traitement des données personnelles sur le territoire de l'Union européenne. Il vise à redonner aux citoyens le contrôle de leurs données personnelles.
</div>
</div>

<h3>Principes fondamentaux du RGPD</h3>

<div class="rgpd-grid">
<div class="rgpd-card">
<div class="rgpd-icon">🎯</div>
<div class="rgpd-title">Finalité</div>
<div class="rgpd-description">
Les données doivent être collectées pour des finalités déterminées, explicites et légitimes. Pas de traitement ultérieur incompatible.
</div>
</div>

<div class="rgpd-card">
<div class="rgpd-icon">📏</div>
<div class="rgpd-title">Proportionnalité</div>
<div class="rgpd-description">
Les données collectées doivent être adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités.
</div>
</div>

<div class="rgpd-card">
<div class="rgpd-icon">⏰</div>
<div class="rgpd-title">Conservation limitée</div>
<div class="rgpd-description">
Les données ne peuvent être conservées que pendant la durée nécessaire aux finalités pour lesquelles elles sont traitées.
</div>
</div>

<div class="rgpd-card">
<div class="rgpd-icon">🔒</div>
<div class="rgpd-title">Sécurité</div>
<div class="rgpd-description">
Mise en place de mesures techniques et organisationnelles appropriées pour assurer la sécurité des données.
</div>
</div>

<div class="rgpd-card">
<div class="rgpd-icon">✅</div>
<div class="rgpd-title">Exactitude</div>
<div class="rgpd-description">
Les données doivent être exactes et, si nécessaire, tenues à jour. Toute mesure raisonnable doit être prise pour effacer ou rectifier.
</div>
</div>

<div class="rgpd-card">
<div class="rgpd-icon">👁️</div>
<div class="rgpd-title">Transparence</div>
<div class="rgpd-description">
Information claire et compréhensible des personnes concernées sur le traitement de leurs données personnelles.
</div>
</div>
</div>

<h3>Droits des personnes concernées</h3>

<div class="demo-box">
<div class="demo-title">Les 8 droits fondamentaux</div>
<ol>
<li><strong>Droit à l'information :</strong> Être informé de la collecte et du traitement</li>
<li><strong>Droit d'accès :</strong> Obtenir une copie des données personnelles</li>
<li><strong>Droit de rectification :</strong> Corriger les données inexactes</li>
<li><strong>Droit à l'effacement :</strong> "Droit à l'oubli" sous certaines conditions</li>
<li><strong>Droit à la limitation :</strong> Restreindre le traitement</li>
<li><strong>Droit à la portabilité :</strong> Récupérer ses données dans un format structuré</li>
<li><strong>Droit d'opposition :</strong> S'opposer au traitement pour des raisons légitimes</li>
<li><strong>Droits relatifs à la prise de décision automatisée :</strong> Ne pas subir de décision basée uniquement sur un traitement automatisé</li>
</ol>
</div>

### Obligations des responsables de traitement

<table class="compliance-table">
<thead>
<tr>
<th>Obligation</th>
<th>Description</th>
<th>Mise en œuvre technique</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Registre des traitements</strong></td>
<td>Documenter tous les traitements de données</td>
<td>Base de données des traitements, cartographie des flux</td>
</tr>
<tr>
<td><strong>Privacy by Design</strong></td>
<td>Intégrer la protection dès la conception</td>
<td>Chiffrement, pseudonymisation, minimisation</td>
</tr>
<tr>
<td><strong>Analyse d'impact (PIA)</strong></td>
<td>Évaluer les risques pour les droits et libertés</td>
<td>Méthodologie CNIL, outils d'évaluation</td>
</tr>
<tr>
<td><strong>Notification de violation</strong></td>
<td>Signaler les incidents dans les 72h</td>
<td>Procédures d'incident, outils de notification</td>
</tr>
<tr>
<td><strong>Désignation d'un DPO</strong></td>
<td>Délégué à la protection des données</td>
<td>Formation, outils de gestion de la conformité</td>
</tr>
</tbody>
</table>

### Sanctions et amendes

<div class="sanction-box">
<div class="sanction-title">Sanctions administratives</div>
<ul>
<li><strong>Niveau 1 :</strong> Jusqu'à 10 millions d'euros ou 2% du CA annuel mondial</li>
<li><strong>Niveau 2 :</strong> Jusqu'à 20 millions d'euros ou 4% du CA annuel mondial</li>
<li><strong>Autres sanctions :</strong> Avertissement, mise en demeure, limitation temporaire ou définitive du traitement, suspension des flux de données</li>
</ul>
</div>

### Mise en conformité technique

<div class="code-example">
<div class="code-title">Exemple d'implémentation RGPD en Python</div>
```python
#!/usr/bin/env python3
"""
Système de gestion de la conformité RGPD
Exemple d'implémentation des droits des utilisateurs
"""

import hashlib
import json
import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class ConsentType(Enum):
    EXPLICIT = "explicit"
    IMPLICIT = "implicit"
    WITHDRAWN = "withdrawn"

class LegalBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTERESTS = "vital_interests"
    PUBLIC_TASK = "public_task"
    LEGITIMATE_INTERESTS = "legitimate_interests"

@dataclass
class PersonalData:
    """Représentation d'une donnée personnelle"""
    field_name: str
    value: str
    category: str  # identité, contact, professionnel, etc.
    sensitivity: str  # normal, sensible, très_sensible
    source: str
    collection_date: datetime.datetime
    retention_period: int  # en jours
    legal_basis: LegalBasis
    
    def is_expired(self) -> bool:
        """Vérifier si la donnée a dépassé sa durée de conservation"""
        expiry_date = self.collection_date + datetime.timedelta(days=self.retention_period)
        return datetime.datetime.now() > expiry_date
    
    def anonymize(self) -> str:
        """Anonymiser la donnée"""
        return hashlib.sha256(self.value.encode()).hexdigest()[:8]

@dataclass
class DataSubject:
    """Personne concernée par le traitement"""
    subject_id: str
    email: str
    consents: Dict[str, ConsentType]
    personal_data: List[PersonalData]
    created_at: datetime.datetime
    last_updated: datetime.datetime
    
    def grant_consent(self, purpose: str, consent_type: ConsentType = ConsentType.EXPLICIT):
        """Accorder un consentement"""
        self.consents[purpose] = consent_type
        self.last_updated = datetime.datetime.now()
    
    def withdraw_consent(self, purpose: str):
        """Retirer un consentement"""
        self.consents[purpose] = ConsentType.WITHDRAWN
        self.last_updated = datetime.datetime.now()
    
    def has_valid_consent(self, purpose: str) -> bool:
        """Vérifier si le consentement est valide"""
        return self.consents.get(purpose) == ConsentType.EXPLICIT

class GDPRCompliance:
    """Système de gestion de la conformité RGPD"""
    
    def __init__(self):
        self.data_subjects: Dict[str, DataSubject] = {}
        self.processing_activities: List[Dict] = []
        self.data_breaches: List[Dict] = []
    
    def register_data_subject(self, subject_id: str, email: str) -> DataSubject:
        """Enregistrer une nouvelle personne concernée"""
        subject = DataSubject(
            subject_id=subject_id,
            email=email,
            consents={},
            personal_data=[],
            created_at=datetime.datetime.now(),
            last_updated=datetime.datetime.now()
        )
        self.data_subjects[subject_id] = subject
        return subject
    
    def collect_personal_data(self, subject_id: str, data: PersonalData) -> bool:
        """Collecter une donnée personnelle"""
        if subject_id not in self.data_subjects:
            return False
        
        subject = self.data_subjects[subject_id]
        
        # Vérifier la base légale
        if data.legal_basis == LegalBasis.CONSENT:
            if not subject.has_valid_consent("data_collection"):
                return False
        
        subject.personal_data.append(data)
        subject.last_updated = datetime.datetime.now()
        return True
    
    def exercise_right_of_access(self, subject_id: str) -> Optional[Dict]:
        """Droit d'accès - Fournir toutes les données de la personne"""
        if subject_id not in self.data_subjects:
            return None
        
        subject = self.data_subjects[subject_id]
        
        return {
            "subject_id": subject.subject_id,
            "email": subject.email,
            "consents": subject.consents,
            "personal_data": [asdict(data) for data in subject.personal_data],
            "created_at": subject.created_at.isoformat(),
            "last_updated": subject.last_updated.isoformat()
        }
    
    def exercise_right_of_rectification(self, subject_id: str, field_name: str, new_value: str) -> bool:
        """Droit de rectification - Corriger une donnée"""
        if subject_id not in self.data_subjects:
            return False
        
        subject = self.data_subjects[subject_id]
        
        for data in subject.personal_data:
            if data.field_name == field_name:
                data.value = new_value
                subject.last_updated = datetime.datetime.now()
                return True
        
        return False
    
    def exercise_right_of_erasure(self, subject_id: str, field_name: Optional[str] = None) -> bool:
        """Droit à l'effacement - Supprimer des données"""
        if subject_id not in self.data_subjects:
            return False
        
        subject = self.data_subjects[subject_id]
        
        if field_name:
            # Supprimer une donnée spécifique
            subject.personal_data = [
                data for data in subject.personal_data 
                if data.field_name != field_name
            ]
        else:
            # Supprimer toutes les données
            del self.data_subjects[subject_id]
        
        return True
    
    def exercise_right_of_portability(self, subject_id: str) -> Optional[str]:
        """Droit à la portabilité - Export des données en JSON"""
        data = self.exercise_right_of_access(subject_id)
        if data:
            return json.dumps(data, indent=2, ensure_ascii=False)
        return None
    
    def data_retention_cleanup(self):
        """Nettoyage automatique des données expirées"""
        cleaned_count = 0
        
        for subject in self.data_subjects.values():
            original_count = len(subject.personal_data)
            subject.personal_data = [
                data for data in subject.personal_data 
                if not data.is_expired()
            ]
            cleaned_count += original_count - len(subject.personal_data)
        
        return cleaned_count
    
    def report_data_breach(self, description: str, affected_subjects: List[str], 
                          severity: str, measures_taken: str):
        """Signaler une violation de données"""
        breach = {
            "id": hashlib.md5(f"{datetime.datetime.now()}{description}".encode()).hexdigest(),
            "description": description,
            "affected_subjects": affected_subjects,
            "severity": severity,
            "measures_taken": measures_taken,
            "reported_at": datetime.datetime.now().isoformat(),
            "notified_to_authority": False,
            "subjects_notified": False
        }
        
        self.data_breaches.append(breach)
        
        # Notification automatique si plus de 72h
        if severity in ["high", "critical"]:
            breach["requires_immediate_notification"] = True
        
        return breach["id"]
    
    def generate_compliance_report(self) -> Dict:
        """Générer un rapport de conformité"""
        total_subjects = len(self.data_subjects)
        total_data_points = sum(len(s.personal_data) for s in self.data_subjects.values())
        
        consent_stats = {}
        for subject in self.data_subjects.values():
            for purpose, consent in subject.consents.items():
                if purpose not in consent_stats:
                    consent_stats[purpose] = {"explicit": 0, "withdrawn": 0}
                if consent == ConsentType.EXPLICIT:
                    consent_stats[purpose]["explicit"] += 1
                elif consent == ConsentType.WITHDRAWN:
                    consent_stats[purpose]["withdrawn"] += 1
        
        return {
            "report_date": datetime.datetime.now().isoformat(),
            "total_data_subjects": total_subjects,
            "total_data_points": total_data_points,
            "consent_statistics": consent_stats,
            "data_breaches_count": len(self.data_breaches),
            "compliance_score": self._calculate_compliance_score()
        }
    
    def _calculate_compliance_score(self) -> float:
        """Calculer un score de conformité basique"""
        if not self.data_subjects:
            return 100.0
        
        total_score = 0
        total_subjects = len(self.data_subjects)
        
        for subject in self.data_subjects.values():
            subject_score = 0
            
            # Points pour les consentements explicites
            explicit_consents = sum(1 for c in subject.consents.values() 
                                  if c == ConsentType.EXPLICIT)
            if explicit_consents > 0:
                subject_score += 30
            
            # Points pour la fraîcheur des données
            days_since_update = (datetime.datetime.now() - subject.last_updated).days
            if days_since_update < 30:
                subject_score += 20
            
            # Points pour la limitation des données
            if len(subject.personal_data) < 10:  # Principe de minimisation
                subject_score += 25
            
            # Points pour l'absence de données expirées
            expired_data = sum(1 for data in subject.personal_data if data.is_expired())
            if expired_data == 0:
                subject_score += 25
            
            total_score += subject_score
        
        return min(100.0, total_score / total_subjects)

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialisation du système RGPD
    gdpr_system = GDPRCompliance()
    
    # Enregistrement d'un utilisateur
    user = gdpr_system.register_data_subject("user123", "user@example.com")
    user.grant_consent("data_collection", ConsentType.EXPLICIT)
    user.grant_consent("marketing", ConsentType.EXPLICIT)
    
    # Collecte de données personnelles
    personal_data = PersonalData(
        field_name="nom",
        value="Dupont",
        category="identité",
        sensitivity="normal",
        source="formulaire_inscription",
        collection_date=datetime.datetime.now(),
        retention_period=365,  # 1 an
        legal_basis=LegalBasis.CONSENT
    )
    
    gdpr_system.collect_personal_data("user123", personal_data)
    
    # Exercice des droits
    print("=== Droit d'accès ===")
    access_data = gdpr_system.exercise_right_of_access("user123")
    print(json.dumps(access_data, indent=2, ensure_ascii=False))
    
    print("\n=== Droit de portabilité ===")
    portable_data = gdpr_system.exercise_right_of_portability("user123")
    print(portable_data)
    
    print("\n=== Rapport de conformité ===")
    compliance_report = gdpr_system.generate_compliance_report()
    print(json.dumps(compliance_report, indent=2, ensure_ascii=False))
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">📋 Normes et Standards de Sécurité</h2>

<div class="definition-box">
<div class="definition-title">Normes de sécurité</div>
<div class="definition-content">
Référentiels internationaux qui définissent les bonnes pratiques et exigences pour la mise en place d'un système de management de la sécurité de l'information efficace.
</div>
</div>

### Principales normes de sécurité

<div class="norms-grid">
<div class="norm-card">
<h4>🏆 ISO 27001</h4>
<p><strong>Système de Management de la Sécurité de l'Information (SMSI)</strong></p>
<ul>
<li>Approche par les risques</li>
<li>Amélioration continue (PDCA)</li>
<li>114 mesures de sécurité</li>
<li>Certification possible</li>
</ul>
</div>

<div class="norm-card">
<h4>🇫🇷 ANSSI</h4>
<p><strong>Agence Nationale de la Sécurité des Systèmes d'Information</strong></p>
<ul>
<li>Guide d'hygiène informatique</li>
<li>Référentiel général de sécurité (RGS)</li>
<li>Critères communs (CC)</li>
<li>Certification CSPN</li>
</ul>
</div>

<div class="norm-card">
<h4>🏭 IEC 62443</h4>
<p><strong>Sécurité des systèmes industriels</strong></p>
<ul>
<li>Systèmes de contrôle industriel</li>
<li>Zones et conduits de sécurité</li>
<li>Niveaux de sécurité (SL)</li>
<li>Cybersécurité OT</li>
</ul>
</div>

<div class="norm-card">
<h4>💳 PCI DSS</h4>
<p><strong>Payment Card Industry Data Security Standard</strong></p>
<ul>
<li>Protection des données de cartes</li>
<li>12 exigences principales</li>
<li>Tests de pénétration obligatoires</li>
<li>Audit annuel</li>
</ul>
</div>

<div class="norm-card">
<h4>🏥 HDS</h4>
<p><strong>Hébergement de Données de Santé</strong></p>
<ul>
<li>Données de santé à caractère personnel</li>
<li>Certification obligatoire</li>
<li>Traçabilité et chiffrement</li>
<li>Procédures d'urgence</li>
</ul>
</div>

<div class="norm-card">
<h4>🌐 NIST</h4>
<p><strong>National Institute of Standards and Technology</strong></p>
<ul>
<li>Cybersecurity Framework</li>
<li>5 fonctions principales</li>
<li>Identify, Protect, Detect, Respond, Recover</li>
<li>Approche par maturité</li>
</ul>
</div>
</div>

### ISO 27001 - Détail des domaines

<table class="compliance-table">
<thead>
<tr>
<th>Domaine</th>
<th>Objectifs</th>
<th>Mesures clés</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>A.5 - Politiques de sécurité</strong></td>
<td>Orientation et soutien de la direction</td>
<td>Politique de sécurité, revue régulière</td>
</tr>
<tr>
<td><strong>A.6 - Organisation</strong></td>
<td>Cadre de gouvernance de la sécurité</td>
<td>Rôles et responsabilités, accords de confidentialité</td>
</tr>
<tr>
<td><strong>A.7 - Sécurité RH</strong></td>
<td>Personnel de confiance et sensibilisé</td>
<td>Vérification des antécédents, formation</td>
</tr>
<tr>
<td><strong>A.8 - Gestion des actifs</strong></td>
<td>Protection appropriée des actifs</td>
<td>Inventaire, classification, manipulation</td>
</tr>
<tr>
<td><strong>A.9 - Contrôle d'accès</strong></td>
<td>Accès autorisé uniquement</td>
<td>Politique d'accès, gestion des privilèges</td>
</tr>
<tr>
<td><strong>A.10 - Cryptographie</strong></td>
<td>Usage approprié de la cryptographie</td>
<td>Politique cryptographique, gestion des clés</td>
</tr>
<tr>
<td><strong>A.11 - Sécurité physique</strong></td>
<td>Protection des zones et équipements</td>
<td>Périmètres sécurisés, protection contre les menaces</td>
</tr>
<tr>
<td><strong>A.12 - Sécurité d'exploitation</strong></td>
<td>Fonctionnement sécurisé des systèmes</td>
<td>Procédures d'exploitation, gestion des vulnérabilités</td>
</tr>
<tr>
<td><strong>A.13 - Sécurité des communications</strong></td>
<td>Protection des informations en transit</td>
<td>Gestion du réseau, transferts sécurisés</td>
</tr>
<tr>
<td><strong>A.14 - Développement sécurisé</strong></td>
<td>Sécurité intégrée dans le cycle de vie</td>
<td>Politique de développement, tests de sécurité</td>
</tr>
<tr>
<td><strong>A.15 - Relations fournisseurs</strong></td>
<td>Protection dans les relations tierces</td>
<td>Politique fournisseurs, accords de service</td>
</tr>
<tr>
<td><strong>A.16 - Gestion des incidents</strong></td>
<td>Réponse cohérente et efficace</td>
<td>Procédures d'incident, amélioration continue</td>
</tr>
<tr>
<td><strong>A.17 - Continuité d'activité</strong></td>
<td>Maintien des opérations critiques</td>
<td>Plan de continuité, tests réguliers</td>
</tr>
<tr>
<td><strong>A.18 - Conformité</strong></td>
<td>Respect des exigences légales</td>
<td>Identification des exigences, audits</td>
</tr>
</tbody>
</table>

### Checklist de mise en conformité ISO 27001

<div class="checklist-item">
<div class="checklist-title">✅ Phase 1 : Préparation</div>
<ul>
<li>Définir le périmètre du SMSI</li>
<li>Identifier les parties intéressées</li>
<li>Établir la politique de sécurité</li>
<li>Nommer un responsable SMSI</li>
</ul>
</div>

<div class="checklist-item">
<div class="checklist-title">✅ Phase 2 : Analyse des risques</div>
<ul>
<li>Inventaire des actifs informationnels</li>
<li>Identification des menaces et vulnérabilités</li>
<li>Évaluation des risques (probabilité × impact)</li>
<li>Définition du niveau de risque acceptable</li>
</ul>
</div>

<div class="checklist-item">
<div class="checklist-title">✅ Phase 3 : Traitement des risques</div>
<ul>
<li>Sélection des mesures de sécurité</li>
<li>Déclaration d'applicabilité (SoA)</li>
<li>Plan de traitement des risques</li>
<li>Validation par la direction</li>
</ul>
</div>

<div class="checklist-item">
<div class="checklist-title">✅ Phase 4 : Mise en œuvre</div>
<ul>
<li>Déploiement des mesures techniques</li>
<li>Formation et sensibilisation</li>
<li>Documentation des procédures</li>
<li>Tests et validation</li>
</ul>
</div>

<div class="checklist-item">
<div class="checklist-title">✅ Phase 5 : Surveillance</div>
<ul>
<li>Indicateurs de performance (KPI)</li>
<li>Audits internes réguliers</li>
<li>Revue de direction</li>
<li>Amélioration continue</li>
</ul>
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🔍 Veille Sécurité</h2>

<div class="definition-box">
<div class="definition-title">Veille sécurité</div>
<div class="definition-content">
Processus continu de collecte, d'analyse et de diffusion d'informations sur les menaces, vulnérabilités et évolutions technologiques en matière de cybersécurité.
</div>
</div>

### Sources de veille sécurité

<div class="veille-source">
<div class="veille-source-title">🏛️ Sources institutionnelles</div>
<ul>
<li><strong>ANSSI :</strong> Bulletins d'alerte, guides de bonnes pratiques</li>
<li><strong>CERT-FR :</strong> Alertes de sécurité, avis de vulnérabilités</li>
<li><strong>CISA :</strong> Cybersecurity advisories (États-Unis)</li>
<li><strong>ENISA :</strong> Rapports sur les menaces (Europe)</li>
</ul>
</div>

<div class="veille-source">
<div class="veille-source-title">🔍 Bases de vulnérabilités</div>
<ul>
<li><strong>CVE (Common Vulnerabilities and Exposures) :</strong> Base internationale</li>
<li><strong>NVD (National Vulnerability Database) :</strong> NIST</li>
<li><strong>VulnDB :</strong> Base commerciale détaillée</li>
<li><strong>Exploit-DB :</strong> Exploits publics</li>
</ul>
</div>

<div class="veille-source">
<div class="veille-source-title">🌐 Communautés et forums</div>
<ul>
<li><strong>Reddit :</strong> r/netsec, r/cybersecurity</li>
<li><strong>Twitter :</strong> Comptes d'experts en sécurité</li>
<li><strong>Discord/Slack :</strong> Communautés spécialisées</li>
<li><strong>Conférences :</strong> BlackHat, DefCon, SSTIC</li>
</ul>
</div>

<div class="veille-source">
<div class="veille-source-title">🏢 Sources commerciales</div>
<ul>
<li><strong>Threat Intelligence :</strong> FireEye, CrowdStrike</li>
<li><strong>Rapports sectoriels :</strong> Verizon DBIR, IBM X-Force</li>
<li><strong>Éditeurs de sécurité :</strong> Bulletins produits</li>
<li><strong>Cabinets de conseil :</strong> Analyses prospectives</li>
</ul>
</div>

### Automatisation de la veille

<div class="code-example">
<div class="code-title">Système automatisé de veille sécurité</div>
```python
#!/usr/bin/env python3
"""
Système automatisé de veille sécurité
Collecte et analyse des informations de sécurité
"""

import requests
import feedparser
import json
import re
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import sqlite3
from dataclasses import dataclass
import smtplib
from email.mime.text import MimeText
from email.mime.multipart import MimeMultipart

@dataclass
class SecurityAlert:
    """Alerte de sécurité"""
    id: str
    title: str
    description: str
    severity: str
    source: str
    published_date: datetime
    cve_ids: List[str]
    affected_products: List[str]
    url: str
    tags: List[str]

class SecurityWatchdog:
    """Système de veille sécurité automatisé"""
    
    def __init__(self, db_path: str = "security_watch.db"):
        self.db_path = db_path
        self.init_database()
        
        # Sources RSS/Atom
        self.rss_feeds = {
            "CERT-FR": "https://www.cert.ssi.gouv.fr/feed/",
            "US-CERT": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
            "NVD": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
            "SANS": "https://isc.sans.edu/rssfeed.xml",
            "Krebs": "https://krebsonsecurity.com/feed/",
            "Schneier": "https://www.schneier.com/feed/"
        }
        
        # APIs de threat intelligence
        self.apis = {
            "cve_details": "https://cve.circl.lu/api/",
            "vulndb": "https://vulndb.cyberriskanalytics.com/api/v1/",
            "mitre": "https://cve.mitre.org/cgi-bin/cvekey.cgi"
        }
        
        # Mots-clés de surveillance
        self.keywords = [
            "zero-day", "ransomware", "apt", "malware",
            "data breach", "vulnerability", "exploit",
            "phishing", "ddos", "botnet"
        ]
        
        # Produits surveillés
        self.monitored_products = [
            "windows", "linux", "apache", "nginx",
            "mysql", "postgresql", "php", "python",
            "java", "javascript", "wordpress", "drupal"
        ]
    
    def init_database(self):
        """Initialiser la base de données SQLite"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                severity TEXT,
                source TEXT,
                published_date TEXT,
                cve_ids TEXT,
                affected_products TEXT,
                url TEXT,
                tags TEXT,
                processed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS keywords_tracking (
                keyword TEXT,
                alert_id TEXT,
                matches INTEGER,
                FOREIGN KEY (alert_id) REFERENCES alerts (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def fetch_rss_feeds(self) -> List[SecurityAlert]:
        """Récupérer les flux RSS/Atom"""
        alerts = []
        
        for source_name, feed_url in self.rss_feeds.items():
            try:
                print(f"[+] Récupération du flux {source_name}...")
                feed = feedparser.parse(feed_url)
                
                for entry in feed.entries:
                    # Extraire les CVE IDs
                    cve_pattern = r'CVE-\d{4}-\d{4,7}'
                    cve_ids = re.findall(cve_pattern, entry.title + " " + entry.get('summary', ''))
                    
                    # Détecter les produits affectés
                    affected_products = []
                    content = (entry.title + " " + entry.get('summary', '')).lower()
                    for product in self.monitored_products:
                        if product in content:
                            affected_products.append(product)
                    
                    # Calculer la sévérité basée sur les mots-clés
                    severity = self._calculate_severity(content, cve_ids)
                    
                    # Extraire les tags
                    tags = self._extract_tags(content)
                    
                    alert = SecurityAlert(
                        id=f"{source_name}_{hash(entry.link)}",
                        title=entry.title,
                        description=entry.get('summary', ''),
                        severity=severity,
                        source=source_name,
                        published_date=datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.now(),
                        cve_ids=cve_ids,
                        affected_products=affected_products,
                        url=entry.link,
                        tags=tags
                    )
                    
                    alerts.append(alert)
                    
            except Exception as e:
                print(f"[-] Erreur lors de la récupération de {source_name}: {e}")
        
        return alerts
    
    def fetch_cve_details(self, cve_id: str) -> Optional[Dict]:
        """Récupérer les détails d'une CVE"""
        try:
            url = f"https://cve.circl.lu/api/cve/{cve_id}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
                
        except Exception as e:
            print(f"[-] Erreur lors de la récupération de {cve_id}: {e}")
        
        return None
    
    def _calculate_severity(self, content: str, cve_ids: List[str]) -> str:
        """Calculer la sévérité d'une alerte"""
        high_severity_keywords = [
            "critical", "zero-day", "remote code execution",
            "privilege escalation", "ransomware", "apt"
        ]
        
        medium_severity_keywords = [
            "vulnerability", "exploit", "malware", "phishing"
        ]
        
        # Vérifier les mots-clés haute sévérité
        for keyword in high_severity_keywords:
            if keyword in content:
                return "HIGH"
        
        # Vérifier les CVE avec score CVSS élevé
        for cve_id in cve_ids:
            cve_details = self.fetch_cve_details(cve_id)
            if cve_details and cve_details.get('cvss', 0) >= 7.0:
                return "HIGH"
        
        # Vérifier les mots-clés moyenne sévérité
        for keyword in medium_severity_keywords:
            if keyword in content:
                return "MEDIUM"
        
        return "LOW"
    
    def _extract_tags(self, content: str) -> List[str]:
        """Extraire les tags d'une alerte"""
        tags = []
        
        tag_patterns = {
            "malware": r"\b(malware|trojan|virus|worm|rootkit)\b",
            "ransomware": r"\b(ransomware|crypto|locker)\b",
            "apt": r"\b(apt|advanced persistent threat)\b",
            "ddos": r"\b(ddos|denial of service)\b",
            "phishing": r"\b(phishing|spear phishing|whaling)\b",
            "vulnerability": r"\b(vulnerability|exploit|cve)\b",
            "data_breach": r"\b(data breach|leak|exposure)\b"
        }
        
        for tag, pattern in tag_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                tags.append(tag)
        
        return tags
    
    def store_alerts(self, alerts: List[SecurityAlert]):
        """Stocker les alertes en base de données"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for alert in alerts:
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO alerts 
                    (id, title, description, severity, source, published_date, 
                     cve_ids, affected_products, url, tags)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    alert.id,
                    alert.title,
                    alert.description,
                    alert.severity,
                    alert.source,
                    alert.published_date.isoformat(),
                    json.dumps(alert.cve_ids),
                    json.dumps(alert.affected_products),
                    alert.url,
                    json.dumps(alert.tags)
                ))
                
                # Tracking des mots-clés
                for keyword in self.keywords:
                    content = (alert.title + " " + alert.description).lower()
                    matches = len(re.findall(keyword, content, re.IGNORECASE))
                    if matches > 0:
                        cursor.execute('''
                            INSERT OR REPLACE INTO keywords_tracking 
                            (keyword, alert_id, matches)
                            VALUES (?, ?, ?)
                        ''', (keyword, alert.id, matches))
                
            except Exception as e:
                print(f"[-] Erreur lors du stockage de l'alerte {alert.id}: {e}")
        
        conn.commit()
        conn.close()
    
    def get_recent_alerts(self, hours: int = 24, severity: str = None) -> List[Dict]:
        """Récupérer les alertes récentes"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        since_date = (datetime.now() - timedelta(hours=hours)).isoformat()
        
        query = '''
            SELECT * FROM alerts 
            WHERE published_date >= ?
        '''
        params = [since_date]
        
        if severity:
            query += ' AND severity = ?'
            params.append(severity)
        
        query += ' ORDER BY published_date DESC'
        
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        conn.close()
        
        # Convertir en dictionnaires
        columns = [desc[0] for desc in cursor.description]
        alerts = []
        for row in results:
            alert_dict = dict(zip(columns, row))
            # Désérialiser les champs JSON
            alert_dict['cve_ids'] = json.loads(alert_dict['cve_ids'])
            alert_dict['affected_products'] = json.loads(alert_dict['affected_products'])
            alert_dict['tags'] = json.loads(alert_dict['tags'])
            alerts.append(alert_dict)
        
        return alerts
    
    def generate_daily_report(self) -> str:
        """Générer un rapport quotidien"""
        high_alerts = self.get_recent_alerts(24, "HIGH")
        medium_alerts = self.get_recent_alerts(24, "MEDIUM")
        
        report = f"""
RAPPORT QUOTIDIEN DE VEILLE SÉCURITÉ
=====================================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ALERTES HAUTE SÉVÉRITÉ ({len(high_alerts)})
{'-' * 40}
"""
        
        for alert in high_alerts[:10]:  # Top 10
            report += f"""
• {alert['title']}
  Source: {alert['source']}
  CVE: {', '.join(alert['cve_ids']) if alert['cve_ids'] else 'N/A'}
  Produits: {', '.join(alert['affected_products']) if alert['affected_products'] else 'N/A'}
  URL: {alert['url']}
"""
        
        report += f"""

ALERTES MOYENNE SÉVÉRITÉ ({len(medium_alerts)})
{'-' * 40}
"""
        
        for alert in medium_alerts[:5]:  # Top 5
            report += f"""
• {alert['title']}
  Source: {alert['source']}
  URL: {alert['url']}
"""
        
        # Statistiques
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT keyword, SUM(matches) as total_matches
            FROM keywords_tracking kt
            JOIN alerts a ON kt.alert_id = a.id
            WHERE a.published_date >= ?
            GROUP BY keyword
            ORDER BY total_matches DESC
            LIMIT 10
        ''', [(datetime.now() - timedelta(hours=24)).isoformat()])
        
        keyword_stats = cursor.fetchall()
        conn.close()
        
        report += f"""

MOTS-CLÉS LES PLUS FRÉQUENTS
{'-' * 30}
"""
        
        for keyword, count in keyword_stats:
            report += f"• {keyword}: {count} mentions\n"
        
        return report
    
    def send_email_alert(self, subject: str, content: str, recipients: List[str]):
        """Envoyer une alerte par email"""
        # Configuration SMTP (à adapter)
        smtp_server = "smtp.example.com"
        smtp_port = 587
        smtp_user = "security-watch@example.com"
        smtp_password = "password"
        
        try:
            msg = MimeMultipart()
            msg['From'] = smtp_user
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            
            msg.attach(MimeText(content, 'plain', 'utf-8'))
            
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            server.quit()
            
            print(f"[+] Email envoyé à {', '.join(recipients)}")
            
        except Exception as e:
            print(f"[-] Erreur lors de l'envoi de l'email: {e}")
    
    def run_watch_cycle(self):
        """Exécuter un cycle de veille complet"""
        print(f"[+] Démarrage du cycle de veille - {datetime.now()}")
        
        # Récupérer les nouvelles alertes
        alerts = self.fetch_rss_feeds()
        print(f"[+] {len(alerts)} alertes récupérées")
        
        # Stocker en base
        self.store_alerts(alerts)
        
        # Vérifier les alertes critiques
        critical_alerts = [a for a in alerts if a.severity == "HIGH"]
        
        if critical_alerts:
            print(f"[!] {len(critical_alerts)} alertes critiques détectées")
            
            # Envoyer une notification immédiate
            alert_summary = "\n".join([f"• {a.title} ({a.source})" for a in critical_alerts[:5]])
            self.send_email_alert(
                f"ALERTE SÉCURITÉ CRITIQUE - {len(critical_alerts)} nouvelles menaces",
                f"Nouvelles alertes critiques détectées:\n\n{alert_summary}",
                ["admin@example.com", "security@example.com"]
            )
        
        print(f"[+] Cycle de veille terminé")

# Exemple d'utilisation
if __name__ == "__main__":
    # Initialisation du système de veille
    watchdog = SecurityWatchdog()
    
    # Exécution d'un cycle de veille
    watchdog.run_watch_cycle()
    
    # Génération du rapport quotidien
    daily_report = watchdog.generate_daily_report()
    print(daily_report)
    
    # Programmation automatique (exemple avec cron)
    # 0 */6 * * * /usr/bin/python3 /path/to/security_watch.py
```
</div>

</div>

---

<div class="concept-section">
<h2 class="section-title">🆔 Identité Numérique et Réputation</h2>

<div class="definition-box">
<div class="definition-title">Identité numérique</div>
<div class="definition-content">
Ensemble des informations et traces numériques qu'une organisation laisse sur Internet, volontairement ou involontairement, qui constituent sa représentation virtuelle et influencent sa réputation.
</div>
</div>

### Composantes de l'identité numérique

<div class="identity-step">
<div class="identity-title">🌐 Présence officielle</div>
<ul>
<li><strong>Sites web :</strong> Site corporate, portails clients, intranets</li>
<li><strong>Réseaux sociaux :</strong> Comptes officiels, pages entreprise</li>
<li><strong>Domaines :</strong> Noms de domaine principaux et variantes</li>
<li><strong>Certificats :</strong> SSL/TLS, signatures numériques</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">👥 Présence des collaborateurs</div>
<ul>
<li><strong>Profils professionnels :</strong> LinkedIn, réseaux métier</li>
<li><strong>Publications :</strong> Articles, conférences, brevets</li>
<li><strong>Réseaux personnels :</strong> Traces involontaires</li>
<li><strong>Fuites d'information :</strong> Données exposées</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">🔍 Traces techniques</div>
<ul>
<li><strong>Infrastructure :</strong> Adresses IP, serveurs, services</li>
<li><strong>Métadonnées :</strong> Documents, images, emails</li>
<li><strong>Logs publics :</strong> Certificats CT, DNS, WHOIS</li>
<li><strong>Vulnérabilités :</strong> Expositions de sécurité</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">📰 Réputation externe</div>
<ul>
<li><strong>Médias :</strong> Articles de presse, communiqués</li>
<li><strong>Avis clients :</strong> Plateformes d'évaluation</li>
<li><strong>Forums :</strong> Discussions, retours d'expérience</li>
<li><strong>Incidents :</strong> Breaches, pannes, controverses</li>
</ul>
</div>

### Menaces sur l'identité numérique

<table class="compliance-table">
<thead>
<tr>
<th>Menace</th>
<th>Description</th>
<th>Impact</th>
<th>Mesures de protection</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Typosquatting</strong></td>
<td>Enregistrement de domaines similaires</td>
<td>Phishing, détournement de trafic</td>
<td>Surveillance des domaines, enregistrement préventif</td>
</tr>
<tr>
<td><strong>Usurpation d'identité</strong></td>
<td>Création de faux comptes/sites</td>
<td>Atteinte à la réputation, fraude</td>
<td>Monitoring des réseaux sociaux, signalement</td>
</tr>
<tr>
<td><strong>Défacement</strong></td>
<td>Modification malveillante du site</td>
<td>Image dégradée, perte de confiance</td>
<td>Sécurisation web, sauvegdes, monitoring</td>
</tr>
<tr>
<td><strong>Fuite de données</strong></td>
<td>Exposition d'informations sensibles</td>
<td>Sanctions RGPD, perte de clients</td>
<td>Chiffrement, contrôles d'accès, DLP</td>
</tr>
<tr>
<td><strong>Campagne de désinformation</strong></td>
<td>Diffusion de fausses informations</td>
<td>Réputation ternie, boycott</td>
<td>Veille réputation, communication de crise</td>
</tr>
<tr>
<td><strong>Social engineering</strong></td>
<td>Manipulation des collaborateurs</td>
<td>Accès non autorisé, vol d'informations</td>
<td>Formation, sensibilisation, procédures</td>
</tr>
</tbody>
</table>

### Stratégie de protection de l'identité numérique

<div class="identity-step">
<div class="identity-title">🔍 Audit de l'identité numérique</div>
<ul>
<li><strong>Cartographie :</strong> Inventaire de tous les actifs numériques</li>
<li><strong>Recherche OSINT :</strong> Informations publiquement disponibles</li>
<li><strong>Analyse des risques :</strong> Vulnérabilités et expositions</li>
<li><strong>Benchmark concurrentiel :</strong> Comparaison sectorielle</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">🛡️ Mesures de protection</div>
<ul>
<li><strong>Enregistrement défensif :</strong> Domaines variantes et typos</li>
<li><strong>Monitoring continu :</strong> Surveillance automatisée</li>
<li><strong>Authentification forte :</strong> 2FA sur tous les comptes</li>
<li><strong>Charte d'usage :</strong> Guidelines pour les collaborateurs</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">📱 Gestion des réseaux sociaux</div>
<ul>
<li><strong>Politique social media :</strong> Règles de publication</li>
<li><strong>Comptes officiels :</strong> Certification et sécurisation</li>
<li><strong>Modération :</strong> Gestion des commentaires et interactions</li>
<li><strong>Crise communication :</strong> Procédures de réponse rapide</li>
</ul>
</div>

<div class="identity-step">
<div class="identity-title">⚡ Gestion de crise</div>
<ul>
<li><strong>Plan de communication :</strong> Messages pré-rédigés</li>
<li><strong>Cellule de crise :</strong> Équipe dédiée et formée</li>
<li><strong>Canaux de communication :</strong> Médias, réseaux, site web</li>
<li><strong>Suivi post-crise :</strong> Analyse et amélioration</li>
</ul>
</div>

### Outils de monitoring de l'identité numérique

<div class="code-example">
<div class="code-title">Script de surveillance de l'identité numérique</div>
```python
#!/usr/bin/env python3
"""
Système de surveillance de l'identité numérique
Monitoring automatisé de la présence en ligne
"""

import requests
import dns.resolver
import whois
import ssl
import socket
from urllib.parse import urlparse
import re
from datetime import datetime, timedelta
import json
from typing import List, Dict, Optional
import hashlib

class DigitalIdentityMonitor:
    """Surveillance de l'identité numérique"""
    
    def __init__(self, organization_name: str, primary_domain: str):
        self.organization_name = organization_name
        self.primary_domain = primary_domain
        self.monitored_domains = []
        self.social_accounts = {}
        self.monitoring_results = {}
    
    def add_domain_variants(self):
        """Générer les variantes de domaine à surveiller"""
        base_domain = self.primary_domain.split('.')[0]
        tlds = ['.com', '.fr', '.org', '.net', '.eu', '.info']
        
        # Variantes communes
        variants = [
            base_domain,
            base_domain + 's',
            base_domain.replace('-', ''),
            base_domain.replace('_', ''),
            'www' + base_domain,
            base_domain + 'official'
        ]
        
        # Typosquatting commun
        typos = []
        for i, char in enumerate(base_domain):
            # Caractères adjacents sur clavier QWERTY
            adjacent_chars = {
                'a': 'qwsz', 'b': 'vghn', 'c': 'xdfv', 'd': 'erfcxs',
                'e': 'wrdsf', 'f': 'rtgvcd', 'g': 'tyhbvf', 'h': 'yujnbg',
                'i': 'ujklo', 'j': 'ikmnhu', 'k': 'olmji', 'l': 'pko',
                'm': 'njk', 'n': 'bhjm', 'o': 'iklp', 'p': 'ol',
                'q': 'wa', 'r': 'etdf', 's': 'awedxz', 't': 'ryfg',
                'u': 'yihj', 'v': 'cfgb', 'w': 'qase', 'x': 'zsdc',
                'y': 'tugh', 'z': 'asx'
            }
            
            if char in adjacent_chars:
                for adj_char in adjacent_chars[char]:
                    typo = base_domain[:i] + adj_char + base_domain[i+1:]
                    typos.append(typo)
        
        # Combiner variantes et TLDs
        for variant in variants + typos:
            for tld in tlds:
                self.monitored_domains.append(variant + tld)
    
    def check_domain_registration(self, domain: str) -> Dict:
        """Vérifier l'enregistrement d'un domaine"""
        result = {
            'domain': domain,
            'registered': False,
            'registrar': None,
            'creation_date': None,
            'expiration_date': None,
            'nameservers': [],
            'suspicious': False
        }
        
        try:
            # Vérification WHOIS
            domain_info = whois.whois(domain)
            
            if domain_info.domain_name:
                result['registered'] = True
                result['registrar'] = domain_info.registrar
                result['creation_date'] = domain_info.creation_date
                result['expiration_date'] = domain_info.expiration_date
                result['nameservers'] = domain_info.name_servers or []
                
                # Détection de domaines suspects
                if domain != self.primary_domain:
                    # Domaine récemment enregistré
                    if isinstance(domain_info.creation_date, datetime):
                        days_old = (datetime.now() - domain_info.creation_date).days
                        if days_old < 30:
                            result['suspicious'] = True
                    
                    # Registrar différent
                    primary_whois = whois.whois(self.primary_domain)
                    if (primary_whois.registrar and 
                        domain_info.registrar != primary_whois.registrar):
                        result['suspicious'] = True
        
        except Exception as e:
            print(f"Erreur WHOIS pour {domain}: {e}")
        
        return result
    
    def check_ssl_certificate(self, domain: str) -> Dict:
        """Vérifier le certificat SSL d'un domaine"""
        result = {
            'domain': domain,
            'has_ssl': False,
            'issuer': None,
            'subject': None,
            'expiration_date': None,
            'san_domains': [],
            'suspicious': False
        }
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    result['has_ssl'] = True
                    result['issuer'] = dict(x[0] for x in cert['issuer'])
                    result['subject'] = dict(x[0] for x in cert['subject'])
                    
                    # Date d'expiration
                    exp_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    result['expiration_date'] = exp_date
                    
                    # SAN (Subject Alternative Names)
                    if 'subjectAltName' in cert:
                        result['san_domains'] = [name[1] for name in cert['subjectAltName']]
                    
                    # Détection de certificats suspects
                    if domain != self.primary_domain:
                        # Certificat auto-signé ou émetteur suspect
                        issuer_cn = result['issuer'].get('commonName', '').lower()
                        if 'let\'s encrypt' in issuer_cn or 'self-signed' in issuer_cn:
                            result['suspicious'] = True
        
        except Exception as e:
            print(f"Erreur SSL pour {domain}: {e}")
        
        return result
    
    def check_website_content(self, domain: str) -> Dict:
        """Analyser le contenu d'un site web"""
        result = {
            'domain': domain,
            'accessible': False,
            'title': None,
            'description': None,
            'keywords': [],
            'organization_mentioned': False,
            'suspicious_content': False,
            'phishing_indicators': []
        }
        
        try:
            response = requests.get(f"https://{domain}", timeout=10, 
                                  allow_redirects=True, verify=False)
            
            if response.status_code == 200:
                result['accessible'] = True
                content = response.text.lower()
                
                # Extraction des métadonnées
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
                if title_match:
                    result['title'] = title_match.group(1).strip()
                
                desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', 
                                     content, re.IGNORECASE)
                if desc_match:
                    result['description'] = desc_match.group(1).strip()
                
                # Vérification de la mention de l'organisation
                org_variations = [
                    self.organization_name.lower(),
                    self.organization_name.lower().replace(' ', ''),
                    self.organization_name.lower().replace('-', ''),
                ]
                
                for variation in org_variations:
                    if variation in content:
                        result['organization_mentioned'] = True
                        break
                
                # Détection d'indicateurs de phishing
                phishing_patterns = [
                    r'urgent.*action.*required',
                    r'verify.*account.*immediately',
                    r'suspended.*account',
                    r'click.*here.*now',
                    r'limited.*time.*offer',
                    r'congratulations.*winner'
                ]
                
                for pattern in phishing_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        result['phishing_indicators'].append(pattern)
                        result['suspicious_content'] = True
        
        except Exception as e:
            print(f"Erreur d'accès web pour {domain}: {e}")
        
        return result
    
    def search_social_media_mentions(self, platform: str, query: str) -> List[Dict]:
        """Rechercher des mentions sur les réseaux sociaux"""
        # Note: Nécessite des APIs spécifiques pour chaque plateforme
        # Ceci est un exemple conceptuel
        
        mentions = []
        
        # Simulation de recherche (à remplacer par de vraies APIs)
        if platform == "twitter":
            # API Twitter v2
            pass
        elif platform == "facebook":
            # Graph API Facebook
            pass
        elif platform == "linkedin":
            # LinkedIn API
            pass
        
        return mentions
    
    def generate_monitoring_report(self) -> Dict:
        """Générer un rapport de surveillance"""
        report = {
            'organization': self.organization_name,
            'primary_domain': self.primary_domain,
            'scan_date': datetime.now().isoformat(),
            'summary': {
                'total_domains_checked': len(self.monitored_domains),
                'suspicious_domains': 0,
                'ssl_issues': 0,
                'phishing_attempts': 0
            },
            'findings': {
                'domain_registrations': [],
                'ssl_certificates': [],
                'website_content': [],
                'social_mentions': []
            },
            'recommendations': []
        }
        
        # Analyser tous les domaines surveillés
        for domain in self.monitored_domains:
            # Vérification d'enregistrement
            domain_info = self.check_domain_registration(domain)
            if domain_info['registered']:
                report['findings']['domain_registrations'].append(domain_info)
                
                if domain_info['suspicious']:
                    report['summary']['suspicious_domains'] += 1
                
                # Vérification SSL
                ssl_info = self.check_ssl_certificate(domain)
                report['findings']['ssl_certificates'].append(ssl_info)
                
                if ssl_info['suspicious']:
                    report['summary']['ssl_issues'] += 1
                
                # Analyse du contenu
                content_info = self.check_website_content(domain)
                report['findings']['website_content'].append(content_info)
                
                if content_info['suspicious_content']:
                    report['summary']['phishing_attempts'] += 1
        
        # Générer des recommandations
        if report['summary']['suspicious_domains'] > 0:
            report['recommendations'].append(
                "Surveiller de près les domaines suspects identifiés"
            )
        
        if report['summary']['ssl_issues'] > 0:
            report['recommendations'].append(
                "Vérifier les certificats SSL suspects"
            )
        
        if report['summary']['phishing_attempts'] > 0:
            report['recommendations'].append(
                "Signaler les tentatives de phishing aux autorités"
            )
        
        return report
    
    def run_full_scan(self) -> Dict:
        """Exécuter une analyse complète"""
        print(f"[+] Démarrage de l'analyse pour {self.organization_name}")
        
        # Générer les variantes de domaine
        self.add_domain_variants()
        print(f"[+] {len(self.monitored_domains)} domaines à surveiller")
        
        # Générer le rapport
        report = self.generate_monitoring_report()
        
        print(f"[+] Analyse terminée:")
        print(f"    - Domaines suspects: {report['summary']['suspicious_domains']}")
        print(f"    - Problèmes SSL: {report['summary']['ssl_issues']}")
        print(f"    - Tentatives de phishing: {report['summary']['phishing_attempts']}")
        
        return report

# Exemple d'utilisation
if __name__ == "__main__":
    # Configuration pour une organisation
    monitor = DigitalIdentityMonitor("MonEntreprise", "monentreprise.com")
    
    # Ajout de comptes sociaux à surveiller
    monitor.social_accounts = {
        "twitter": "@monentreprise",
        "linkedin": "company/monentreprise",
        "facebook": "monentreprise"
    }
    
    # Exécution de l'analyse
    report = monitor.run_full_scan()
    
    # Sauvegarde du rapport
    with open(f"identity_report_{datetime.now().strftime('%Y%m%d')}.json", 'w') as f:
        json.dump(report, f, indent=2, default=str, ensure_ascii=False)
    
    print("\n[+] Rapport sauvegardé")
```
</div>

</div>

---

## 🎯 Compétences BTS SIO - Bloc B3

<div class="highlight-fact">
<strong>Correspondance avec le référentiel U7 :</strong>
<ul>
<li><strong>B3.1-B3.2 :</strong> Protéger les données à caractère personnel (RGPD)</li>
<li><strong>B3.3-B3.4 :</strong> Préserver l'identité numérique de l'organisation</li>
<li><strong>B3.5 :</strong> Sécuriser les équipements et les usages des utilisateurs</li>
<li><strong>B3.6 :</strong> Garantir la disponibilité, l'intégrité et la confidentialité face aux cyberattaques</li>
</ul>
</div>

## 📚 Ressources et références

### Documentation officielle
- **CNIL :** Guide RGPD du développeur
- **ANSSI :** Guide d'hygiène informatique
- **ISO :** Norme ISO 27001:2022
- **NIST :** Cybersecurity Framework

### Outils pratiques
- **RGPD :** PIA CNIL, registre des traitements
- **Veille :** CERT-FR, CVE Details, NVD
- **Monitoring :** Google Alerts, Mention, Brand24
- **Conformité :** GRC tools, audit frameworks

---

<div class="demo-box">
<div class="demo-title">💡 Points clés à retenir</div>
<ul>
<li>La conformité RGPD est une obligation légale avec des sanctions importantes</li>
<li>Les normes de sécurité fournissent un cadre structuré pour la protection</li>
<li>La veille sécurité doit être automatisée et continue</li>
<li>L'identité numérique nécessite une surveillance proactive</li>
<li>La gestion de crise doit être préparée et testée régulièrement</li>
</ul>
</div>
# 🦊 B2.7 - Projet FoxShelter - Gestion de Refuge pour Renards



# 🦊 FoxShelter
*Système de gestion de refuge pour renards - Projet BTS SIO 1 SLAM*

## 📋 Objectifs du projet

À la fin de ce projet, vous serez capable de :
- ✅ Concevoir une application complète avec UML
- ✅ Implémenter le pattern MVC en C#
- ✅ Gérer une base de données avec Entity Framework
- ✅ Appliquer tous les concepts de POO
- ✅ Créer une interface utilisateur fonctionnelle
- ✅ Documenter et tester votre application

---

## 🎯 Cahier des charges

!!! note "📋 Contexte du projet"
    Le refuge "FoxShelter" accueille des renards blessés, orphelins ou en détresse. L'association a besoin d'un système informatique pour gérer efficacement les animaux, le personnel, les soins vétérinaires et les finances.

### 🎪 Fonctionnalités principales

- **🦊 Gestion des Renards** : Enregistrement, suivi médical, historique des soins, statut d'adoption
- **👥 Gestion du Personnel** : Vétérinaires, bénévoles, planning des équipes, gestion des rôles  
- **💊 Suivi Médical** : Dossiers vétérinaires, traitements, vaccinations, examens
- **🏠 Processus d'Adoption** : Candidatures, évaluations, suivi post-adoption
- **💰 Gestion Financière** : Dons, frais vétérinaires, budget du refuge
- **📊 Tableaux de Bord** : Statistiques, rapports, indicateurs de performance

---

## 🏗️ Architecture du projet

### 📐 Pattern MVC (Model-View-Controller)

!!! info "🎯 Structure du projet"
    - **Models :** Entités métier (Renard, Personne, SoinVeterinaire...)
    - **Views :** Interfaces utilisateur (formulaires, listes, rapports)
    - **Controllers :** Logique de traitement et coordination
    - **Data :** Accès aux données avec Entity Framework

!!! abstract "🛠️ Stack Technologique"
    - **Langage :** C# .NET 6.0
    - **Framework :** ASP.NET Core MVC
    - **Base de données :** SQL Server / SQLite
    - **ORM :** Entity Framework Core
    - **Interface :** Bootstrap + CSS personnalisé
    - **Tests :** xUnit

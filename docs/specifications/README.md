# Vue d'ensemble
## Contexte et vision
Dans le cadre de ce projet, vous serez amenés à réaliser une application web complète de gestion de stocks. Le commanditaire souhaite disposer d'une application moderne et professionnelle permettant de gérer l'inventaire de plusieurs entreprises. L'accent est mis sur la qualité du code, la sécurité et l'expérience utilisateur. Le projet doit également intégrer Github Actions pour l'intégration continue, préparant ainsi les étudiants aux exigences du monde professionnel.
## Objectifs pédagogiques
- Approfondir la maîtrise de Django : modèles, vues génériques, templates, signaux et système d'authentification
- Concevoir une architecture modulaire et évolutive : séparation par applications (catalogue, entrepôt, reporting, utilisateurs).
- Mettre l'accent sur la sécurité et les bonnes pratiques Web (système d'authentification, permissions, CSRF, etc).
- Introduire les fondements DevOps : tests d'intégration dans un pipeline GitHub Actions

# Fonctionnalité
L'application web devra proposer les fonctionnalités suivantes :
### 1. Gestion des utilisateurs et rôles
Inscription, authentification, réinitialisation de mot de passe.
### 2. Catalogue produits
CRUD complet, import/export CSV.
### 3. Multi-entreprises
Possibilité de gérer les stocks de plusieurs entreprises, chaque utilisateur étant limité à son périmètre (on peut affecter un utilisateur à une ou plusieurs entreprises).
### 4. Mouvements de stock
Entrées, sorties, historisation avec horodatage.
### 5. Alertes seuil critique
Notification dans l'application lorsque la quantité passe sous le seuil défini et possibilité pour chaque produit de définir le seuil d'alerte.
### 6. Tableau de bord et statistiques
Graphiques simples (quantités par catégorie, évolution mensuelle) rendus avec Chart.js.
### 7. Administration personnalisée
Interface admin (affichage, filtres, recherche) permettant la gestion des utilisateurs, produits, stocks, etc.
## Scénario d'usage principal
> En tant que propriétaire de plusieurs entreprises, je veux pouvoir gérer les stocks de mes différentes entreprises depuis une seule interface, afin de suivre facilement les niveaux d'inventaire et d'être alerté quand les produits atteignent un seuil critique.
## Use case 
Voici un exemple concret d'utilisation de l'application :
- Le propriétaire dispose d'un compte administrateur et peut créer des entreprises, des produits, des stocks et des utilisateurs.
- Chaque compte utilisateur dispose de droits spécifiques pour chaque entreprise.
- Un utilisateur peut créer, modifier et supprimer des produits et modifier les stocks.
- Le propriétaire a une vision d'ensemble de ses entreprises et de ses stocks sur un tableau de bord.
- Le propriétaire peut voir les alertes de seuil critique pour chaque entreprise.

# Spécifications techniques
## Architecture
- Application Django classique avec base de données.
- Langage : Python 3.11 minimum et Django 5.x.
- Dépendances tierces conseillées : pytest--django, django import/export, django cleanup, django crispy forms, django--environ.
## Modèles
- Product : SKU, nom, description, prix, seuil d'alerte
- Location : nom, adresse, type (dépôt/boutique)
- Stock : produit, lieu, quantité
- Movement : produit, lieu source/destination, quantité, date, raison
## Vues
- Vue spéciale pour les mouvements avec formulaire dynamique.
- Dashboard avec graphiques Chart.js.
## Tests
- Tests unitaires.
- Tests fonctionnels.
- Fixtures pour données de test.
## Livrables attendus
Dépôt GitHub public contenant :
- Code source complet et commenté
- Jeux de données d'exemple (fixtures/initial_data.json)
- Scripts ou instructions de lancement
- Documentation utilisateur dans le README.md (installation, commandes, exemples)
- Jeu de tests automatisés :
pytest exécutés par un workflow GitHub Actions.

# Planification & jalons
| Période suggérée | Jalon                    | Objectifs proposés                                                                                                                             |
|------------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Semaine 1        | Initialisation           | - Création du projet Django et configuration Git <br/>- Installation des dépendances de base <br/>- Configuration de la CI avec GitHub Actions |
| Semaines 2à3     | Modélisation             | - Création des modèles (User, Product, Stock) <br/>- Premières migrations et fixtures <br/>- Configuration de l'admin Django basique           |
| Semaines 4à5     | Fonctionnalités core     | - Authentification et gestion des rôles - CRUD produits avec interface web - Premiers tests avec pytest-django                                 |
| Semaines 6à7     | Fonctionnalités avancées | - Système de notifications et alertes - Tableau de bord avec graphiques - Import/export de données                                             |
| Dernière semaine | Production ready         | - Configuration Docker et déploiement - Documentation technique et utilisateur - Tests de sécurité et optimisations                            |

# Gestion des risques
| Risque                                     | Mesure préventive                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------------------------|
| Complexité de la gestion multi-entreprises | Commencer par un POC simple, valider l'architecture des modèles avec le mentor dès le début |
| Problèmes de performance BDD               | Optimiser les requêtes, utiliser select_related/prefetch_related                            |
| Difficultés avec GitHub Actions            | Partir de templates, commencer avec des tests basiques                                      |

# Ressources
Une liste de ressources sur Docstring et sur le web pour vous aider à réaliser ce projet.
- Documentation Rich https://rich.readthedocs.io/
- Votre code en ligne sur Github en 10mn https://youtu.be/76hFN6kcV04
- Les fichiers JSON https://www.docstring.fr/formations/les-fichiers-json-avec-python/
- L'orienté objet : les bases https://www.docstring.fr/formations/loriente-objet-les-bases/
- Documentation officielle Django https://docs.djangoproject.com/en/5.2/
- Guide sécurité Django https://docs.djangoproject.com/en/5.2/topics/security/
- Documentation Chart.js https://www.chartjs.org/
- Tutoriel rédaction tests pytest--django https://pytest-django.readthedocs.io/
- Tutoriel officiel GitHub Actions https://docs.github.com/en/actions/writing-workflows/quickstart

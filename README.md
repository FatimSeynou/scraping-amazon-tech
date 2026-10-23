# Projet scraping Amazon.com - Technologie

Ce projet récupère des produits technologiques sur Amazon.com.
Il enregistre les produits dans une base de données, affiche des statistiques
et crée un fichier CSV (un fichier qu'on peut ouvrir avec Excel).

## Ce que fait le programme

- Un menu s'affiche : tu choisis la catégorie, la sous-catégorie et le nombre de pages.
- Les produits sont enregistrés dans `data/produits.db`.
- Un produit n'est enregistré qu'une seule fois, même si tu relances le scraping.
- Le fichier CSV est créé dans le dossier `exports`.
- Les statistiques donnent le nombre de produits, le prix moyen, le prix le plus haut et le plus bas.

## Avant de commencer

Il te faut :
- Python 3.10 ou plus récent
- Google Chrome installé sur l'ordinateur

## Installation (à faire une seule fois)

1. Ouvre le terminal dans le dossier `AMAZON_SCRAPER`.
2. Active l'environnement virtuel :

```
.venv\Scripts\activate
```

3. Installe les outils nécessaires :

```
pip install -r requirements.txt
```

Attention : il y a bien un tiret (`-`) avant le `r`.

## Lancer le programme

Dans le terminal, toujours depuis le dossier `AMAZON_SCRAPER` :

```
python main.py
```

## Utiliser le menu

- Tape `1` pour récupérer des produits.
  Choisis une catégorie, puis une sous-catégorie, puis le nombre de pages (3 maximum).
- Tape `2` pour voir les produits, les statistiques et créer le fichier CSV.
- Tape `3` pour quitter.

Pour revenir en arrière dans un choix, tape `0`.

## Les prix

Les prix sont en **XOF** (franc CFA), la monnaie de la Côte d'Ivoire.
Amazon choisit la monnaie selon l'endroit où tu te connectes.

## Pour aller plus loin

Tu peux modifier le fichier `config.py` pour :
- ajouter une catégorie ou une sous-catégorie ;
- changer le nombre maximum de pages ;
- changer les pauses entre les requêtes.

## Important

- Les règles d'Amazon interdisent la récupération automatique de données. Ce projet est un exercice scolaire, avec peu de pages et des pauses entre les requêtes.
- Le programme s'arrête tout seul si Amazon demande une vérification (CAPTCHA). Il ne contourne pas cette protection.
- Les données ne sont pas utilisées pour gagner de l'argent.
- Si Amazon change la présentation de ses pages, le programme peut ne plus trouver les produits. Il faut alors modifier `app/scraper/parsing.py`.
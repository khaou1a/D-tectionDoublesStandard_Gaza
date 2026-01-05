# D-tection Doubles Standard Gaza

## Description
This project analyzes and detects inconsistencies in standards and policies.

## Features
- Detection algorithms
- Data analysis tools
- Reporting capabilities

## Installation
...existing code...

## Structure du projet
- [1_Webscrapping.ipynb](1_Webscrapping.ipynb) — collecte des articles (sauvegarde: e.g. [corpus/corpus_gaza_v1.json](corpus/corpus_gaza_v1.json))
- [2_Post-Scraping.ipynb](2_Post-Scraping.ipynb) — nettoyage post-scraping (utilise [`executer_pipeline_expert`](2_Post-Scraping.ipynb), produit fichiers nettoyés comme [corpus/corpus_palestine_nettoye_v1.json](corpus/corpus_palestine_nettoye_v1.json))
- [3_pretraitement.ipynb](3_pretraitement.ipynb) — prétraitement multi-vues (fonction [`traiter_corpus`](3_pretraitement.ipynb) → sorties: [corpus/corpus_gaza_pretraiter.json](corpus/corpus_gaza_pretraiter.json), [corpus/corpus_ukraine_pretraiter.json](corpus/corpus_ukraine_pretraiter.json))
- [5_analyse_sementique.ipynb](5_analyse_sementique.ipynb) — analyses sémantiques (Word2Vec : [`entrainer_modele_lab8`](5_analyse_sementique.ipynb), visualisations → dossier `images/`)
- [6_analyse_de_sentiment.ipynb](6_analyse_de_sentiment.ipynb) — analyse de tonalité ciblée
- `corpus/` — fichiers JSON produits et intermédiaires
- `images/` — graphiques générés (t-SNE, nuages de mots...)

## Comment lancer
1. Installer les dépendances (exemples) :
   - Python 3.8+, Jupyter
   - pip install jupyter pandas numpy matplotlib seaborn gensim spacy nltk wordcloud textblob

2. Exécuter les notebooks dans l'ordre recommandé (ouvrir avec JupyterLab / Notebook) :
   - Lancer Jupyter : `jupyter lab` ou `jupyter notebook`
   - Exécuter : [1_Webscrapping.ipynb](1_Webscrapping.ipynb) → [2_Post-Scraping.ipynb](2_Post-Scraping.ipynb) → [3_pretraitement.ipynb](3_pretraitement.ipynb) → [5_analyse_sementique.ipynb](5_analyse_sementique.ipynb) → [6_analyse_de_sentiment.ipynb](6_analyse_de_sentiment.ipynb)



4. Résultats :
   - Données prétraitées : [corpus/corpus_gaza_pretraiter.json](corpus/corpus_gaza_pretraiter.json)
   - Graphiques et images : dossier `images/`

Notes :
- Pour exécuter l'interface il faut demarer cette commande 

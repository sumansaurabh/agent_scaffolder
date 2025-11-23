# Agent Scaffolder

Un outil Python pour créer automatiquement des structures de projet à partir de descriptions de fichiers texte.

## Fonctionnalités

- Créer des structures complètes de répertoires de projet à partir d'un simple fichier texte
- Génère automatiquement des fichiers de substitution
- Prend en charge les structures de répertoires imbriquées
- Interface en ligne de commande facile à utiliser

## Installation

```bash
pip install -e .
```

Ou en utilisant Poetry :

```bash
poetry install
```

## Utilisation

```bash
python src/scaffolder.py <fichier_structure> <destination>
```

### Exemple

```bash
python src/scaffolder.py example.txt ./mon_nouveau_projet
```

Cela créera une structure de projet basée sur le fichier `example.txt` dans le répertoire `./mon_nouveau_projet`.

## Format du fichier de structure

Le fichier de structure doit utiliser un format arborescent :

```
nom_projet/
├── src/
│   ├── __init__.py
│   ├── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── README.md
└── setup.py
```

## Exigences

- Python 3.9+

## Licence

Voir le fichier LICENSE pour plus de détails.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre une Pull Request.

---

**Autres langues :**
- [English](README.md)
- [हिंदी (Hindi)](README.hi.md)

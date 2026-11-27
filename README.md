# Python Data Analysis Exercises

This repository contains twelve exercises for learning Python and data analysis.

## Project structure

- `exercice-01/` to `exercice-05/`: Python fundamentals, conditions, lists, dictionaries, functions, and modules.
- `exercice-06/` to `exercice-10/`: data inspection, Titanic analysis and cleaning, business questions, and joins.
- `exercice-11/`: analysis of New York taxi trips.
- `exercice-12/`: five charts about Titanic passengers and taxi trips.

## Setup

Use Python 3.12 or a compatible version. Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open the notebooks in Jupyter and run them from top to bottom. Some notebooks download public datasets from the Seaborn data repository, so an internet connection is needed for those exercises.

## Data files

Dataset files are local and excluded from Git. The notebooks create or read datasets under their exercise folders. Downloaded datasets and generated CSV, TSV, and Parquet files are ignored by `.gitignore`.

## Exercise outputs

Exercise 12 saves its charts in `exercice-12/figures/` when run from the repository root, or in `figures/` when run from the exercise directory.

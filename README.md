# IMDB Data Analysis

## Execution Order

1. **imdb_data_analysis_1.Rmd** - Processes the raw IMDB dataset, generates the first visualization, and outputs `imdb_ids.csv`

2. **fetch_episode_ratings.py** - Fetches episode ratings from TVMaze API and generates `episode_ratings.csv`

3. **imdb_data_analysis_2.Rmd** - Uses the episode ratings data to generate the final visualization

## Python Setup

Create a virtual environment with Python 3.13.7:

```bash
python3.13 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python fetch_episode_ratings.py
```

The script reads `imdb_ids.csv` and outputs `episode_ratings.csv`.

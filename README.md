# amazing-client-clustering
## Folder architecture
<pre lang="markdown">
<code>
AMAZING-CLIENT-CLUSTERING/
│
├── .env                         # Environment variables (e.g., chunk size, paths)
├── .gitignore                   # Ignore data, models, logs, etc.
├── README.md                    # Project description, setup, and usage
├── requirements.txt             # Python dependencies
├── environment.yml              # (Optional) Conda environment file
├── main.py                      # Entry point for running the pipeline
│
├── config/                      # YAML or JSON config files (hyperparameters, thresholds)
│   └── settings.yaml
│
├── data/
│   ├── raw/                     # Original large CSVs (60GB total)
│   │   └── 2020-Jan.csv         # Etc.
│   ├── processed/               # Cleaned & transformed per-user dataset (e.g., Parquet/Feather)
│   ├── external/                # External sources, lookup tables, metadata
│   └── interim/                 # Intermediate results (aggregates, filtered files)
│
├── models/                      # Saved trained models (.pkl or .joblib)
│   ├── kmeans_model.pkl
│   └── clustering_results.csv
│
├── logs/                        # Logging output during processing and training
│   └── pipeline.log
│
├── notebooks/                   # EDA, PCA, clustering visualization, and prototyping
│   └── EDA.ipynb
│
├── tests/                       # Unit tests using pytest
│   ├── test_load_data.py
│   ├── test_preprocess.py
│   └── test_features.py
│
├── src/
│   ├── __init__.py
│
│   ├── data/
│   │   ├── load_data.py         # Load CSVs in chunks, handle memory
│   │   └── preprocess.py        # Cleaning and filtering logic
│
│   ├── features/
│   │   └── build_features.py    # Create per-user metrics from event data
│
│   ├── models/
│   │   ├── train_model.py       # Clustering model training (KMeans, DBSCAN, etc.)
│   │   ├── evaluate_model.py    # Silhouette score, DB index, etc.
│   │   └── model_utils.py       # Save/load models
│
│   ├── interface/
│   │   ├── app_streamlit.py     # (Optional) Streamlit interface
│   │   └── simulate_user.py     # Predict cluster for new synthetic users
│
│   ├── utils/
│   │   ├── helper_functions.py  # Date parsing, encoding, etc.
│   │   ├── config.py            # Load .env and YAML config
│   │   └── logger.py            # Logging setup
│
│   └── visualize/
│       └── visualize.py         # Elbow plots, cluster 2D/3D projections
</code>
</pre>

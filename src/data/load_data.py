"""DocString"""
import os
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO)

def load_csv_in_chunks(file_path: str, chunk_size):
    """Docstring"""
    logging.info("Reading file in chunks: %s", file_path)

    for chunk in pd.read_csv(file_path, sep=",", chunksize=chunk_size):
        yield chunk

def load_all_months(data_folder: str, chunck_size):
    """Docstring"""
    files = sorted([file for file in os.listdir(
        data_folder) if file.endswith(".csv")])

    for file in files:
        file_path = os.path.join(data_folder, file)
        logging.info("Starting file: %s", file)
        yield from load_csv_in_chunks(file_path, chunck_size)

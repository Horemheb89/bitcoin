from google.cloud import storage
import pandas as pd

def get_data():
    """method to get the training data (or a portion of it) from local folder (or google cloud bucket)"""
    # client = storage.Client()
    # data = pd.read_csv(f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}")
    data = pd.read_csv('../raw_data/bitstampUSD.csv')
    # data = pd.read_csv('gs://bitcoin-prediction-01/data/bitstampUSD.csv')
    return data

# def clean_data():
"""method to prepare the data for analysis"""
#     pass

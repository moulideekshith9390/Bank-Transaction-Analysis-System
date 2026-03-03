from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
import pandas as pd

def spending_clusters(df):
    model = KMeans(n_clusters=3, random_state=42)
    df["Cluster"] = model.fit_predict(df[["Amount"]])
    return df

def detect_anomalies(df):
    iso = IsolationForest(contamination=0.02, random_state=42)
    df["Anomaly"] = iso.fit_predict(df[["Amount"]])
    anomalies = df[df["Anomaly"] == -1]
    return anomalies
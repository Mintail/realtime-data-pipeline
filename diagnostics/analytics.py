from data_pipeline.processor import compute_features
from data_pipeline.storage import load_all

def compute_diagnostics():
    df = load_all()
    if df.empty:
        return df
    df = compute_features( df )
    return df

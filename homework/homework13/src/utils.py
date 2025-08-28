
# src/project.py
import os, joblib, pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# path via os (repo root or notebooks/)
CWD = os.getcwd()
if os.path.exists(os.path.join(CWD, "model")) and os.path.exists(os.path.join(CWD, "data")):
    ROOT = CWD
else:
    ROOT = os.path.dirname(CWD)

DATA_DIR = os.path.join(ROOT, "data")
MODEL_DIR = os.path.join(ROOT, "model")
REPORTS_DIR = os.path.join(ROOT, "reports")
for d in [DATA_DIR, MODEL_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

def _clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates().copy()
    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].mean())
    return df

def _features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if {"feature1", "feature2"}.issubset(out.columns):
        out["f1_x_f2"] = out["feature1"] * out["feature2"]
    return out

def train_and_save(df: pd.DataFrame, target: str = "target"):
    df = _clean(df)
    df = _features(df)
    X = df[["feature1", "feature2", "f1_x_f2"]]
    y = df[target]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression().fit(Xtr, ytr)
    preds = model.predict(Xte)
    metrics = {
        "rmse": float(mean_squared_error(yte, preds, squared=False)),
        "r2": float(r2_score(yte, preds)),
    }
    joblib.dump(model, MODEL_PATH)
    return metrics

def load_model():
    return joblib.load(MODEL_PATH)

def predict_one(payload: dict) -> float:
    """payload expects keys: feature1, feature2 (server will add f1_x_f2)."""
    df = pd.DataFrame([payload])
    df = _features(df)
    model = load_model()
    return float(model.predict(df)[0])

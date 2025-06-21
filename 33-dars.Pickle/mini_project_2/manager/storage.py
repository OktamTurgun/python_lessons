import pickle
import os
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "products.pkl"

def load_mahsulotlar():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "rb") as file:
        return pickle.load(file)

def save_mahsulotlar(mahsulotlar: list):
    DATA_DIR.mkdir(exist_ok=True)
    with open(DATA_FILE, "wb") as file:
        pickle.dump(mahsulotlar, file)

from os import environ, listdir
from pickle import load

DATABASE_URI = environ.get("DATABASE_URL", "sqlite:///database/local.db")
ASSETS_DIR = environ.get("ASSETS_DIR", "assets")
MODEL_LIST = {}


"""
load all models to MODEL_LIST
"""
for file_name in listdir(f"{ASSETS_DIR}/models"):
    if not file_name.endswith(".pkl"):
        continue
    filepath = f"{ASSETS_DIR}/models/{file_name}"
    print(f"Loading model {filepath}")
    with open(filepath, "rb") as f:
        model = load(f)
    MODEL_LIST[file_name[:-4]] = model
